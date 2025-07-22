#!/usr/bin/bash
#
#
# 
# Build the project
#


gcc -Wall src/*.c -o out/main

flag=$?

sleep 1s

if [ $flag -eq 0 ]; then
    ./out/main $*
fi
