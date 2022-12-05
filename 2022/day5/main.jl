if length(ARGS) != 1
    println("usage: julia main.jl <input file>")
    exit(1)
end

lines = readlines(ARGS[1])

stackLines = collect(Iterators.takewhile(
    line -> !occursin(r"^\s1\s+2.*\d\s?$", line),
    lines))

a, b = length(stackLines) + 3, length(lines)
instructionLines = lines[a:b]

function parseStackLine(line :: String) :: Array{Union{Nothing, String}}
    cargos = []
    i = 1
    while i <= length(line)
        if i+2 <= length(line)
            s = strip(line[i:i+2])
            if s != ""
                push!(cargos, line[i:i+2])
            else
                push!(cargos, nothing)
            end
            i += 4
        else
            break
        end
    end
    cargos
end

stackLines = map(parseStackLine, stackLines)

stacks = []
for col in 1:length(stackLines[1])
    stack = [stackLines[c][col] for c in 1:length(stackLines)]
    stack = filter(v -> v !== nothing, stack) |> collect
    push!(stacks, stack)
end

struct Instruction
    from :: Int
    to :: Int
    count :: Int
end

function parseInstructionLine(line :: String) :: Instruction
    s = split(line)
    from = parse(Int, s[4])
    to = parse(Int, s[6])
    count = parse(Int, s[2])
    Instruction(from, to, count)
end

instructions = map(parseInstructionLine, instructionLines)

# Solving the problem

function part1(ins :: Instruction, stacks :: Vector)
    for _ in 1:ins.count
        crate = popfirst!(stacks[ins.from])
        pushfirst!(stacks[ins.to], crate)
    end
end

function part2(ins :: Instruction, stacks :: Vector)
    crates = [popfirst!(stacks[ins.from]) for _ in 1:ins.count]
    prepend!(stacks[ins.to], crates)
end

function 🎅(stacks :: Vector) :: String
    map(s -> s[1][2], stacks) |> join
end

for ins in instructions
    part2(ins, stacks)
end
stacks |> 🎅 |> println
