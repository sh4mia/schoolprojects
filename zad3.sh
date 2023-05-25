#!/bin/bash
mkdir zad3
touch zad3/plik.txt
ps -f > zad3/plik.txt
df -h >> zad3/plik.txt
du -m ./ | sort -n >> zad3/plik.txt
