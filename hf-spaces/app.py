import os, subprocess, tempfile
import gradio as gr
import librosa, soundfile as sf, numpy as np
from scipy.signal import butter, sosfilt
import torch


def lowpass_filter(audio, sr, cutoff_hz=8000, order=6):
    sos = butter(order, cutoff_hz, btype="low", fs=sr, output="sos")
    if audio.ndim == 1:
        return sosfilt(sos, audio)
    return np.array([sosfilt(sos, audio[c]) for c in range(audio.shape[0])])


def process_audio(input_path, model_name, ddim_steps, guidance_scale):
    if input_path is None:
        return None, "❌ ファイルを選んでください"
    out = tempfile.mkdtemp(prefix="asr_")
    try:
        a, r = librosa.load(input_path, sr=None, mono=False)
        ext = os.path.splitext(input_path)[1].lower()
        if ext in (".mp3", ".m4a"):
            a = lowpass_filter(a, r)
        wav = os.path.join(out, "in.wav")
        sf.write(wav, a, r)
        d = "cuda" if torch.cuda.is_available() else "cpu"
        p = subprocess.run(
            ["audiosr", "-i", wav, "-s", out, "--model_name", model_name,
             "--ddim_steps", str(ddim_steps), "-gs", str(guidance_scale), "-d", d],
            capture_output=True, text=True, timeout=600)
        if p.returncode != 0:
            return None, f"❌ {p.stderr[:200]}"
        of = [f for f in os.listdir(out) if f.endswith(".wav")]
        if not of:
            return None, "❌ 出力なし"
        mp3 = os.path.join(out, "out.mp3")
        subprocess.run(["ffmpeg", "-i", os.path.join(out, of[0]),
                        "-codec:a", "libmp3lame", "-b:a", "320k", mp3, "-y"],
                       capture_output=True, timeout=60)
        return mp3, f"✅ {r/1000:.0f}kHz→48kHz [{d.upper()}] {model_name}"
    except subprocess.TimeoutExpired:
        return None, "⏰ タイムアウト"
    except Exception as e:
        return None, f"❌ {str(e)[:200]}"


css = "footer{display:none!important}.gradio-container{max-width:800px!important;margin:0 auto!important}"
with gr.Blocks(title="AudioSR Upscaler", theme=gr.themes.Soft(primary_hue="blue"), css=css) as demo:
    gr.Markdown("# 🎧 AudioSR — 音声アップスケーラー\nどんな音声も **48kHz 高音質** に。MP3自動前処理対応。")
    with gr.Row():
        with gr.Column():
            i = gr.Audio(label="📁 ファイル", type="filepath", sources=["upload", "microphone"])
            with gr.Accordion("⚙ 詳細設定", open=False):
                m = gr.Radio(["basic", "speech"], value="basic", label="モデル", info="basic=汎用 / speech=音声")
                s = gr.Slider(15, 100, 50, 5, label="DDIM ステップ")
                g = gr.Slider(1.0, 10.0, 3.5, 0.5, label="ガイダンス")
            b = gr.Button("🚀 実行", variant="primary", size="lg")
        with gr.Column():
            st = gr.Textbox(label="ステータス", interactive=False)
            o = gr.Audio(label="✨ 結果 (48kHz)", type="filepath", interactive=False)
    b.click(fn=process_audio, inputs=[i, m, s, g], outputs=[o, st])
    gr.Markdown("---\n[AudioSR](https://github.com/haoheliu/versatile_audio_super_resolution) — [arXiv 2309.07314](https://arxiv.org/abs/2309.07314)")

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
