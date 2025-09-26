# Lucky10（4/7のみ・10桁）— N番目の数を出力

**問題**  
4 と 7 だけからなる 10 桁の整数を小さい順に並べたとき、N（1 ≤ N ≤ 1024）番目を出力します。  
本リポジトリは **標準入力で N を受け取り**、Docker 上で実行できます。

## 必要環境
- Docker（推奨）

## 使い方
プロジェクト直下に `p1.py` と `Dockerfile` を置いた状態で：

### ビルド
```bash
docker build -t lucky10 .
```

### 実行

```
echo 1 | docker run --rm -i lucky10
echo 5 | docker run --rm -i lucky10
echo 1024 | docker run --rm -i lucky10
```
