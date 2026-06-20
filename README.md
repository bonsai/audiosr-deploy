# 🎧 AudioSR Deploy

**Versatile Audio Super-resolution** — 音声アップスケール & ノイズ補完

どんな音声も **48kHz 高音質** に。拡散モデルで失われた高域を復元します。

## 構成

```
audiosr-deploy/
├── colab/              # Google Colab ノートブック
│   └── AudioSR_upscale_colab.ipynb   ← 手動 + Gradio UI 両対応
├── hf-spaces/          # Hugging Face Spaces デプロイ
│   ├── app.py          # Gradio Web UI
│   ├── requirements.txt
│   ├── Dockerfile
│   └── README.md       # Space 説明
└── README.md           # このファイル
```

## 使い方

### 🅰 Colab（今すぐ試す）
1. `colab/AudioSR_upscale_colab.ipynb` を Google Colab にアップロード
2. ランタイム → T4 GPU を選択
3. 全セル実行 or 最終セルの Gradio UI モード

### 🅱 Hugging Face Spaces（本番公開）
```bash
cd hf-spaces
# Space 作成: https://huggingface.co/new-space
# → SDK: Gradio / Hardware: T4 small
git init && git add . && git commit -m "initial"
git remote add origin https://huggingface.co/spaces/<user>/audiosr-upscaler
git push origin main
```

## モデル

- **AudioSR**: [haoheliu/versatile_audio_super_resolution](https://github.com/haoheliu/versatile_audio_super_resolution) ⭐1884
- **論文**: [arXiv 2309.07314](https://arxiv.org/abs/2309.07314)
- **ライセンス**: MIT
