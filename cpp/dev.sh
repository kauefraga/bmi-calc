#!/bin/sh

#   /$$   /$$ /$$$$$$$$
#  | $$  /$$/| $$_____/
#  | $$ /$$/ | $$
#  | $$$$$/  | $$$$$
#  | $$  $$  | $$__/
#  | $$\  $$ | $$
#  | $$ \  $$| $$      Author: Kauê Fraga Rodrigues
#  |__/  \__/|__/      github.com/kauefraga/bmi-calc

# compile `main.cpp` and run the g++ output
main="cpp/main"

g++ $main.cpp -o $main -std=c++2a
$main
