defmodule Helper do
  def repeat(item, n), do: for(_ <- 1..n, do: item)
end

defmodule Input do
  def get_lines() do
    case System.argv() do
      [filepath] ->
        File.read!(filepath)
        |> String.split("\n")
        |> Enum.filter(fn line -> String.length(line) > 0 end)
        |> Enum.map(&parse_line/1)
        |> List.flatten()

      _ ->
        {:error, "must specify input file as first argument"}
    end
  end

  defp parse_line(line) do
    [direction, steps] = String.split(line)
    Helper.repeat(direction, String.to_integer(steps))
  end
end

defmodule Mover do
  def move("R", {hx, hy}), do: {hx + 1, hy}
  def move("L", {hx, hy}), do: {hx - 1, hy}
  def move("U", {hx, hy}), do: {hx, hy + 1}
  def move("D", {hx, hy}), do: {hx, hy - 1}

  def step({hx, hy} = head, {tx, ty} = tail) do
    if close(head, tail) do
      tail
    else
      update(hx - tx, hy - ty, tx, ty)
    end
  end

  defp close({hx, hy}, {tx, ty}) do
    abs(hx - tx) < 2 and abs(hy - ty) < 2
  end

  # up, down, right, left
  defp update(2, 0, tx, ty), do: {tx + 1, ty}
  defp update(-2, 0, tx, ty), do: {tx - 1, ty}
  defp update(0, 2, tx, ty), do: {tx, ty + 1}
  defp update(0, -2, tx, ty), do: {tx, ty - 1}

  defp update(1, 2, tx, ty), do: {tx + 1, ty + 1}
  defp update(-1, 2, tx, ty), do: {tx - 1, ty + 1}
  defp update(1, -2, tx, ty), do: {tx + 1, ty - 1}
  defp update(-1, -2, tx, ty), do: {tx - 1, ty - 1}
  defp update(2, 1, tx, ty), do: {tx + 1, ty + 1}
  defp update(2, -1, tx, ty), do: {tx + 1, ty - 1}
  defp update(-2, 1, tx, ty), do: {tx - 1, ty + 1}
  defp update(-2, -1, tx, ty), do: {tx - 1, ty - 1}

  # diagonal
  defp update(2, 2, tx, ty), do: {tx + 1, ty + 1}
  defp update(2, -2, tx, ty), do: {tx + 1, ty - 1}
  defp update(-2, 2, tx, ty), do: {tx - 1, ty + 1}
  defp update(-2, -2, tx, ty), do: {tx - 1, ty - 1}
end

defmodule Part1 do
  import Mover

  def run(instructions) do
    reduce(instructions, {0, 0}, {0, 0}, MapSet.new())
    |> Enum.count()
  end

  defp reduce([], _, _, visited), do: visited

  defp reduce(
         [direction | rest],
         head,
         tail,
         visited
       ) do
    head = move(direction, head)
    tail = step(head, tail)
    reduce(rest, head, tail, MapSet.put(visited, tail))
  end
end

defmodule Part2 do
  import Mover

  def run(instructions) do
    rope = Helper.repeat({0, 0}, 10)

    reduce(instructions, rope, MapSet.new())
    |> Enum.count()
  end

  defp reduce([], _, visited), do: visited

  defp reduce(
         [direction | rest],
         rope,
         visited
       ) do
    [head | rope] = rope
    head = move(direction, head)
    new_rope = reduce_rope(rope, head, [])

    visited = MapSet.put(visited, List.last(new_rope))
    reduce(rest, new_rope, visited)
  end

  defp reduce_rope([], last, new), do: new ++ [last]

  defp reduce_rope([child | rope], parent, new) do
    tail = step(parent, child)
    reduce_rope(rope, tail, new ++ [parent])
  end
end

instructions = Input.get_lines()
Part1.run(instructions) |> IO.puts()
Part2.run(instructions) |> IO.puts()
