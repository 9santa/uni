@ECHO OFF
D:
cd D:\santa\lab1
git tag -a "merging" -m "created tag"
git checkout prd
git merge dev
PAUSE