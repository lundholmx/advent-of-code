// Sample project for F#.
// Solution to day 1 as an example.

open System
open System.IO

exception Error of string

let sum (nums: list<int>) =
    let rec loop xs acc =
        match xs with
        | [] -> acc
        | head::tail -> loop tail (head+acc)
    loop nums 0

let countCalories (input: list<string>) =
    let rec loop ls calories curr =
        match ls with
        | [] -> raise (Error("impossible"))
        | [last] -> ((int last)+curr::calories)
        | head::tail ->
            match head with
            | "" -> loop tail (curr::calories) 0
            | n -> loop tail (calories) (int n + curr)
    loop input [] 0 |> List.sort |> List.rev

let readLines (filePath:string) = seq {
    use sr = new StreamReader (filePath)
    while not sr.EndOfStream do
        yield sr.ReadLine()
}

let handle =
    match Environment.GetCommandLineArgs() with
    | [| _; name |] -> readLines name |> Seq.toList |> countCalories
    | _ -> raise (Error("usage: dotnet run <input file>"))

let items = handle

printfn "Part 1: %A" (items |> List.head)
printfn "Part 2: %A" (Seq.take 3 items |> Seq.sum)
