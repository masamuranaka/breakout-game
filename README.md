# ブロック崩し (Pygame)

[![Tests](https://github.com/masamuranaka/breakout-game/actions/workflows/test.yml/badge.svg)](https://github.com/masamuranaka/breakout-game/actions/workflows/test.yml)

Pygame で作ったブロック崩しゲームです。TDD（テスト駆動開発）で開発しています。

## 動作環境
- Python 3.10 以上
- [pygame-ce](https://pyga.me/)（Pygame のコミュニティ版。`import pygame` で利用できます）

## セットアップ
```bash
git clone https://github.com/masamuranaka/breakout-game.git
cd breakout-game
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 実行
```bash
python main.py
```

## 操作
| キー | 動作 |
|---|---|
| ← / → (A / D) | パドル移動 |
| SPACE | ボール発射 |
| P | 一時停止 / 再開 |
| R | ゲームオーバー・クリア後にリトライ |
| ESC | 終了 |

## テスト
```bash
pytest
```
