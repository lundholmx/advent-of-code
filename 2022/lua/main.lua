local lines  = {}
for line in io.lines() do
  table.insert(lines, line)
end

for index, line in ipairs(lines) do
  print(index, line)
end
