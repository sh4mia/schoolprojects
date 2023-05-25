#!/bin/bash

silnia_petla() {
    n=$1
    wynik=1
    for (( i=1; i<=n; i++ ))
    do
        wynik=$((wynik*i))
    done
    echo $wynik
}

if [ $# -lt 4 ]
then
    read -p "Podaj imię: " imie
    read -p "Podaj naziwsko: " nazwisko
    read -p "W którym roku się urodziłeś? " rok
    read -p "Podaj nazwe pliku:(.txt)" nazwa_pliku
else
    imie=$1
    nazwisko=$2
    rok=$3
    nazwa_pliku=$4
fi

rok_teraz=$(date +%Y)
wiek=$((rok_teraz-rok))

echo "Witaj $imie $nazwisko. Masz $wiek lat."


silnia_petla=$(silnia_petla $wiek)

echo "$imie, $nazwisko, $rok, $wiek, $silnia_petla" >> "$nazwa_pliku"
