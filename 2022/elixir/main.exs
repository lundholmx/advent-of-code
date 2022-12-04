defmodule Input do
  def get_lines() do
    case System.argv() do
      [filepath] ->
        File.read!(filepath)
        |> String.split("\n")
      _ -> {:error, "must specify input file as first argument"}
    end
  end
end

Input.get_lines()
|> IO.inspect()
