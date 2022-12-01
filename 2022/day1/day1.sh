#!/usr/bin/env bash

lines=$(cat $1)
lines=($lines)

numfile=$(tempfile)
resfile=$(tempfile)

calories=()
curr=0
while read line; do
  if [[ -z $line ]]; then
    echo $curr >> $numfile
    calories+=($curr)
    curr=0
  else
    curr=$((curr+line))
  fi
done < $1
calories+=($curr)
echo $curr >> $numfile

cat $numfile | sort -gr > $resfile

echo "Part 1: $(head -n 1 $resfile)"

top=$(head -n 3 $resfile)
top=($top)
sum=0
for n in ${top[@]}; do
  sum=$((sum+n))
done
echo "Part 2: $sum"

rm $numfile $resfile