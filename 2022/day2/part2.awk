BEGIN {
  draw["A"] = 1
  draw["B"] = 2
  draw["C"] = 3
  loses["A"] = 3
  loses["B"] = 1
  loses["C"] = 2
  wins["A"] = 2
  wins["B"] = 3
  wins["C"] = 1
  total = 0
}

{
  switch ($2) {
    case "X": # lose
      total += loses[$1]
      break
    case "Y": # draw
      total += draw[$1] + 3
      break
    case "Z": # win
      total += wins[$1] + 6
      break
  }
}

END { print(total) }
