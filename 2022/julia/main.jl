if length(ARGS) != 1
    println("usage: julia main.jl <input file>")
    exit(1)
end

lines = readlines(ARGS[1])

for line in lines
    a, b = split(line, ",")
    println(a, b)
end
