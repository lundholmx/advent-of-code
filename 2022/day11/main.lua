local lines = {}
for line in io.lines() do
  table.insert(lines, line)
end

local function find_numbers(line)
  local words = {}
  string.gsub(line, "(%d+)", function(w)
    table.insert(words, tonumber(w))
  end)
  return words
end

local function parse_operation(line)
  local a, b, c = string.match(line, [[new = (.+) (.) (.+)]])
  return function(old)
    local left
    local right
    if a == "old" then
      left = old
    else
      left = tonumber(a)
    end

    if c == "old" then
      right = old
    else
      right = tonumber(c)
    end

    if b == "+" then
      return left + right
    elseif b == "*" then
      return left * right
    else
      error(string.format("unexpected operator: %s", b))
    end
  end
end

local common_mod = 1

local function parse_test(a, b, c)
  local divisor = tonumber(string.match(a, [[by (%d+)$]]))
  common_mod = common_mod * divisor
  local if_true = string.match(b, [[monkey (.+)$]])
  local if_false = string.match(c, [[monkey (.+)$]])
  return function(n)
    if math.fmod(n, divisor) == 0 then
      return if_true
    else
      return if_false
    end
  end
end

local function parse_group(group)
  local id = string.match(group[1], [[Monkey (%d):]])
  local items = find_numbers(string.match(group[2], [[.+: (.+)$]]))
  local operation = parse_operation(group[3])
  local test = parse_test(group[4], group[5], group[6])
  return {
    id = id,
    items = items,
    operation = operation,
    test = test,
    count = 0,
  }
end

-- Group lines into each monkey
local groups = {}
local current = {}
for _, line in ipairs(lines) do
  if line == "" then
    table.insert(groups, current)
    current = {}
  else
    table.insert(current, line)
  end
end
table.insert(groups, current)

local monkeys = {}
local references = {}
for _, group in ipairs(groups) do
  local m = parse_group(group)
  monkeys[m.id] = m
  table.insert(references, m.id)
end

local function part1(monkey)
  monkey.count = monkey.count + #monkey.items
  for _, item in ipairs(monkey.items) do
    local x = monkey.operation(item)
    local n = math.floor(x / 3)
    local next_monkey = monkey.test(n)
    table.insert(monkeys[next_monkey].items, n)
  end
  monkey.items = {}
end

local function part2(monkey)
  if #monkey.items == 0 then
    return
  end

  monkey.count = monkey.count + #monkey.items

  for _, item in ipairs(monkey.items) do
    local value = math.fmod(item, common_mod)
    local n = monkey.operation(value)
    local next_monkey = monkey.test(n)
    table.insert(monkeys[next_monkey].items, n)
  end

  monkey.items = {}
end

local function handle_round(handle_func)
  for _, id in ipairs(references) do
    handle_func(monkeys[id])
  end
end

local function find_most_active()
  local counts = {}
  for _, monkey in pairs(monkeys) do
    table.insert(counts, monkey.count)
  end
  table.sort(counts, function(a, b) return a > b end)
  return counts[1] * counts[2]
end

--[[
README!
Uncomment to part you want to run.
Cannot run both because of mutating the state (monkeys table).
]]

-- Part 1
for _ = 1, 20 do
  handle_round(part1)
end

-- Part 2
-- for _ = 1, 10000 do
--   handle_round(part2)
-- end

print(find_most_active())
