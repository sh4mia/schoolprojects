#!/bin/bash
mkdir lab1
cd lab1
echo "Lorem ipsum dolor sit amet" > plik1.txt
echo "Aliquam et justo ac velit" > plik2.txt
echo "Proin venenatis lacinia mattis" > plik3.txt
mkdir folder1
mkdir folder2
mkdir folder3

mv plik1.txt folder1/
mv plik2.txt folder2/
mv plik3.txt folder3/

echo "(pwd)" > log.txt
ls -R >> log.txt

wc -lwm folder1/plik1.txt folder2/plik2.txt folder3/plik3.txt >> log.txt

cat folder1/plik1.txt folder2/plik2.txt folder3/plik3.txt > suma.txt
tac folder1/plik1.txt folder2/plik2.txt folder3/plik3.txt >> suma.txt

grep -r "Lorem\|justo" ./*/ >> log.txt
