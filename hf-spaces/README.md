---
title: AudioSR Upscaler
emoji: 🎧
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 4.44.1
app_file: app.py
pinned: false
license: mit
short_description: MP3/WAV音声を48kHz高音質にアップスケール
suggested_hardware: t4-small
---

# 🎧 AudioSR — 音声アップスケーラー

MP3 / WAV 音声を **48kHz 高音質** にアップスケール。拡散モデルで高域復元。

- **対応**: 音楽・音声・効果音
- **MP3 自動前処理**: ローパスフィルターで AudioSR の認識精度向上
- **出力**: 48kHz / 320kbps MP3

### 使い方

1. 音声ファイルをアップロード（MP3/WAV/FLAC/OGG/M4A）
2. 「🚀 実行」をクリック
3. 処理完了後、結果をダウンロード

### 設定

| パラメータ | 標準値 | 説明 |
|---|---|---|
| DDIM steps | 50 | 多い=高品質・低速 |
| Guidance scale | 3.5 | 高い=品質UP・多様性DOWN |
| モデル | basic | basic=汎用 / speech=音声特化 |

---

**モデル**: [haoheliu/versatile_audio_super_resolution](https://github.com/haoheliu/versatile_audio_super_resolution)  
**論文**: [arXiv 2309.07314](https://arxiv.org/abs/2309.07314)
