#!/bin/bash


FILENAME="$1.py"

touch $FILENAME

printf "#!/usr/bin/python3\n\n\n" > $FILENAME
printf "f = open('test.txt', 'rt')\n\nf.close()" >> $FILENAME
