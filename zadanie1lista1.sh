#!/bin/bash
cd ~
mkdir cw1
cd cw1
echo ""
"Lorem ipsum dolor sit amet, consectetur adipiscing \n
 elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." > plik.txt
mv plik.txt plik2.txt
mkdir test
cp plik2.txt test/test
cp -r test test2
cd ~
rm -rf cw1

