open System
open System.IO

exception Error of string

let subroutine (s:string) (size:int) =
    let allUnique (chars:char list) =
        let s = Set.ofList chars
        chars.Length = s.Count
    let rec loop (chars:char list) count =
        match (allUnique (List.take size chars)) with
        | true -> count + size
        | false -> loop (List.tail chars) (count + 1)
    loop [for ch in s -> ch] 0

let readLines (filePath:string) = seq {
    use sr = new StreamReader (filePath)
    while not sr.EndOfStream do
        yield sr.ReadLine()
}

let lines =
    match Environment.GetCommandLineArgs() with
    | [| _; name |] -> readLines name |> Seq.toList
    | _ -> raise (Error("usage: dotnet run <input file>"))

let line = List.head lines
printfn "Part 1: %d" (subroutine line 4)
printfn "Part 2: %d" (subroutine line 14)
