import fs from "fs";
import readline from "readline";

function getInput() {
  const infile = process.argv[2];
  const readInterface = readline.createInterface({
    input: fs.createReadStream(infile),
    output: process.stdout,
    console: false
  });

  const lines = [];
  readInterface.on('line', function(line) {
    lines.push(line);
  });

  return lines;
}

const lines = getInput();
console.log(lines);
