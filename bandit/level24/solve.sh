#!/bin/bash

# alternative
# for i in {0000..9999}; do echo "gb...G8 $i"; done | nc localhost 30002 | grep -v "Wrong"

for i in {0..9999}
do
  echo "gb...G8 $(printf "%04d" $i)"
done