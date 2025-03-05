#!/bin/bash
git add .
if [ -n "$(git status --porcelain)" ]; then
    git commit -m "$(TZ=Asia/Shanghai date '+%Y-%m-%d %H:%M')"
    git pull --rebase origin main
    git push origin main
else
    echo "No changes to commit"
fi