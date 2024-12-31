#!/bin/bash
# diffs=$(git diff --numstat ticker.txt)
diffs=$(git diff)
# 这里使用的是 master 分支，根据需求自行修改
echo $diffs
if [ "$diffs" == "" ];then
  echo "nothing to commit, working tree clean"
  exit 0
fi

changes=$(git diff --numstat company_ticker.json | awk '{split($0,a," "); print(a[1]+a[2] < 100)}')
echo $changes
if [ "$changes" == "1" ]; then
    echo "submit"
    git add .&&git commit -m "sync latest company_ticker data" && git push origin main
else
    echo "data error"
    exit 0
fi

changes=$(git diff --numstat ticker.txt | awk '{split($0,a," "); print(a[1]+a[2] < 100)}')
echo $changes
if [ "$changes" == "1" ]; then
    echo "submit"
    git add .&&git commit -m "sync latest ticker data" && git push origin main
else
    echo "data error"
    exit 0
fi

