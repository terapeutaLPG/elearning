#!/bin/bash
mkdir -p moj1
touch moj1/dokument.txt
ps aux > moj1/dokument.txt
df -h >> moj1/dokument.txt
du -sm * | sort -n >> moj1/dokument.txt
