BEGIN {
  arr[0] = 1
  arr[1] = 2
  arr[2] = 3
}

END {
  for (x = 0; x < length(arr); x++) {
    print(arr[x])
  }
}
