for f in ./scripts/*.py ; do [ -x "$f" ] && [ ! -d "$f" ] && echo $f && time python3 $f ; done

rm -rf .git && git config --global init.defaultBranch main && git init . && git remote add origin git@github.com:genkin-he/sec_ticker.git