import fs from "fs";

function getInput() {
  const infile = process.argv[2];
  const content = fs.readFileSync(infile, "utf8");
  return content.split("\n").filter(line => line.length > 0);
}

/** Return true if any elements overlap in the two arrays.*/
function overlaps(a, b) {
  return a.some(elem => b.includes(elem));
}

/** Return true if a contains all of b, or if b contains all of a.*/
function contains(a, b) {
  const x = a.every(elem => b.includes(elem));
  const y = b.every(elem => a.includes(elem));
  return x || y;
}

function rangeToArray(range) {
  const [a, b] = range.split("-");
  const nums = [];
  for (let x = parseInt(a); x <= parseInt(b); x++) {
    nums.push(x);
  }
  return nums;
}

function parseLine(line) {
  const [a, b] = line.split(",");
  let x = rangeToArray(a);
  let y = rangeToArray(b);
  return [x, y];
}

const lines = getInput();
const pairs = lines.map(line => parseLine(line));

const part1 = pairs
  .filter(([a, b]) => contains(a, b))
  .length;
const part2 = pairs.filter(([a, b]) => overlaps(a, b)).length;

console.log("Part 1:", part1);
console.log("Part 2:", part2);