#!/bin/bash
# diffs=$(git diff --numstat ticker.txt)
diffs=$(git diff --numstat .github/workflows/sync.yml)
# 这里使用的是 master 分支，根据需求自行修改
echo $diffs
if [ "$diffs" == "" ];then
  echo "nothing to commit, working tree clean"
  exit 0
fi

changes=$(awk '{split($diffs,a," "); print(a[1]+a[2] < 100)}')

if ["$changes" == "1"]; then
    echo "error data"
    exit 0
else
    git add .&&git commit -m "sync latest data" && git push origin main
fi

