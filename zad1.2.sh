#!/bin/bash

if [ $# -lt 1 ]
then
    read -p "Podaj nazwę pliku: " plik
else
    plik=$1
fi

if [ ! -f $plik ]
then
    echo "Plik $plik nie istnieje."
    exit 1 
fi

path=$(echo $PATH | grep -o *":$PWD:")

if [ -z "$path" ]
then
    export PATH=$PATH:$PWD
fi

katalog=daneUsera

if [ -d $katalog ]
then
    rm -rf $katalog
fi

mkdir $katalog
cp $plik $katalog/$plik

ls -l >> $katalog/$plik
