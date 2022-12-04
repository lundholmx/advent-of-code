if length(ARGS) != 1
    println("usage: julia main.jl <input file>")
    exit(1)
end

lines = readlines(ARGS[1])

for line in lines
    a, b = split(line, ",")
    println(a, b)
end

########################
# Testing stuff in Julia

mymap = [:a => 1, :b => 2]

# Unmutable composite type
struct Movie
    title :: String
    tags # implicitly :: Any
end

lotr = Movie("Lord of the Rings", mymap)
println(lotr.title)

# Mutable composite type
mutable struct Mutant
    const id :: String
    count :: Integer
end

leo = Mutant("123-456", 0)
println(leo.count)
leo.count += 10
println(leo.count)


# Composite type with type parameter (generics)
struct Generic{T}
    field :: T
end

println(Generic(1), " - ", Generic("hehe"))

xs = 1:10 # range
# Piping as in Elixir! Good stuff.
piping = xs |> sum |> sqrt |> println


# begin ... end - just larger expressions (like {...} in rust)

z = begin
    x = 2
    y = 3
    x * y
end
println(z)

# Ternary
println(z < 10 ? "indeed" : "nope")

# Anonymous
doubler = x -> x * x
println(doubler(4))
