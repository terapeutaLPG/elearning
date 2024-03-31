#!/bin/bash
echo "Lorem ipsum dolor sit amet do" > plik1.txt
echo "Siema co tam" > plik2.txt
echo "dobranoc" > plik3.txt
mkdir folder1 folder2 folder3
mv plik1.txt folder1/
mv plik2.txt folder2/
mv plik3.txt folder3/
tree -a > log.txt
wc * >> log.txt
du -h * >> log.txt
cat folder1/plik1.txt folder2/plik2.txt folder3/plik3.txt > suma.txt
tac folder1/plik1.txt folder2/plik2.txt folder3/plik3.txt >> suma.txt
grep "Lorem" * >> log.txt
grep "innego_słowa" * >> log.txt

cd root
