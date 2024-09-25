@ECHO OFF

git tag -a "merging" -m "created tag"
git checkout prd
git merge dev
PAUSE