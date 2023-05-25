#!/bin/bash

if [[ $# -lt 2 ]]
then
    echo "Błąd. Podaj nr. dnia i miesiąca jako argumenty."
    exit 1
else
    dzien=$1
    miesiac=$2
fi

dzien_tygodnia=$(date -d "$miesiac/$dzien/2023" +"%A")

echo "Dzień tygodnia $dzien/$miesiac/2023 to $dzien_tygodnia." >>plik1.txt

if [ $? -ne 0 ]
then
    echo "Błąd: wprowadzona zła data." >> plik2.txt
    exit 1
fi
