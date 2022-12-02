BEGIN {
  draw["X"] = "A" # rock
  draw["Y"] = "B" # paper
  draw["Z"] = "C" # scissor
  score["X"] = 1
  score["Y"] = 2
  score["Z"] = 3
  total = 0
}

{
  opponent = $1
  self = $2
  if (self == "X" && opponent == "C") {
    total += 6
  } else if (self == "Y" && opponent == "A") {
    total += 6
  } else if (self == "Z" && opponent == "B") {
    total += 6
  } else if (draw[self] == opponent) {
    total += 3
  }
  total += score[self]
}

END { print(total) }
