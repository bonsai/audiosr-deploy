# HANDOFF: AudioSR Deploy — opencode への引き継ぎ

## プロジェクト概要
MP3/WAV 音声を 48kHz 高音質にアップスケールするツール（AudioSR）のデプロイ基盤。

## 完了済み
- ✅ Colab notebook: `colab/AudioSR_upscale_colab.ipynb`（22 cells / 手動+Gradio UI）
- ✅ HF Spaces コード: `hf-spaces/app.py` + Dockerfile + requirements.txt
- ✅ GitHub Pages UI プレビュー: `docs/index.html` → https://bonsai.github.io/audiosr-deploy/
- ✅ GitHub repo: `bonsai/audiosr-deploy`（public）

## 残タスク（やること）

### ① Colab notebook のインストールエラー修正
**症状**: `pip install audiosr==0.0.7` が wheel ビルドに失敗（Python 3.12 非互換）
**原因**: audiosr の setup.py が古い
**対処案A**: `pip install git+https://github.com/haoheliu/versatile_audio_super_resolution.git` で GitHub 直インストール
**対処案B**: `transformers==4.48.0` を事前インストールしてから audiosr 入れる
**確認**: Colab で notebook 全セル実行して通るか確認

### ② HF Spaces デプロイ
**手順**:
1. https://huggingface.co/new-space で新規 Space 作成
   - Name: `audiosr-upscaler`
   - SDK: Gradio
   - Hardware: T4 small
2. 作成後、`hf-spaces/` のファイルを git push
   ```bash
   cd hf-spaces
   git init && git add -A && git commit -m "initial"
   git remote add origin https://huggingface.co/spaces/<user>/audiosr-upscaler
   git push origin main
   ```
3. 初回ビルド 5〜10分。モデルDL 〜2GB あり
4. 動作確認 → `README.md` の URL 更新

### ③ HF Space を bonsai org 下に作る（任意）
bonsai organization で Space 作るなら API トークン権限確認

### ④ 今後の展望
- **BGM フェードアウト自動検出**機能を audio 処理パイプラインに追加
- バッチ処理（複数ファイル一括）
- MP3 のノイズ低減だけ欲しい人のための RNNoise 分離オプション

## 参考資料
- AudioSR: https://github.com/haoheliu/versatile_audio_super_resolution ⭐1884
- Colab notebook: `colab/AudioSR_upscale_colab.ipynb`
- HF Spaces コード: `hf-spaces/app.py`
- UI プレビュー: https://bonsai.github.io/audiosr-deploy/

## 優先順位
1. **Colab インストール修正**（ユーザーが今すぐ試せるように）
2. **HF Spaces デプロイ**（本番公開）
3. HF Spaces の README に動くURL反映
