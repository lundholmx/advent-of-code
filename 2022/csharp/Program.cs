// See https://aka.ms/new-console-template for more information

using Advent;

if (args.Length != 1)
{
    Console.WriteLine("must provide input file as argument");
    Environment.Exit(1);
}

var lines = new string[] { };
foreach (string line in File.ReadLines(args.First()))
{

    lines.Append(line);
}

var solution = new Solution(lines);

Console.WriteLine($"Part 1: {solution.Part1()}");
Console.WriteLine($"Part 2: {solution.Part2()}");
