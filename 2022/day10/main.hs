import System.Environment
import System.IO

main :: IO ()
main = do
  (inputFilepath : _) <- getArgs
  lines <- readLines inputFilepath
  let instructions = map parseLine lines
      results = runProgram instructions []
      p1 = part1 results
      screen = part2 results
  print p1
  putStrLn (screenToString screen)

join :: [String] -> String -> String
join ls token = loop ls ""
  where
    loop [] _ = ""
    loop [last] str = str ++ last
    loop (head : tail) str = loop tail (str ++ head ++ token)

screenToString screen = join (loop screen []) "\n"
  where
    pixelToStr 0 = " "
    pixelToStr _ = "."
    row2str row = foldl (\acc n -> acc ++ pixelToStr n) [] row
    loop [] acc = acc
    loop (row : tail) acc = loop tail (acc ++ [row2str row])

part1 :: [(Int, Int)] -> Int
part1 results = sumStrengths targets
  where
    targets = filterTargets results

stepCRT (39, 5) = (0, 0)
stepCRT (x, y) = case x' of
  40 -> (0, (y + 1) `mod` 6)
  _ -> (x', y)
  where
    x' = x + 1

charAt x regx
  | a <= x && x <= b = 1
  | otherwise = 0
  where
    a = regx - 1
    b = regx + 1

draw (x, y) regx screen = replace screen y new
  where
    pixel = charAt x regx
    row = screen !! y
    new = replace row x pixel

part2 :: [(Int, Int)] -> [[Int]]
part2 results = loop2 results (0, 0) initscreen
  where
    initscreen = replicate 6 (replicate 40 0)

loop2 :: [(Int, Int)] -> (Int, Int) -> [[Int]] -> [[Int]]
loop2 [] _ screen = screen
loop2 (head : tail) crt screen = loop2 tail newCRT newScreen
  where
    (cycle, regx) = head
    newScreen = draw crt regx screen
    newCRT = stepCRT crt

readLines filepath = do
  content <- readFile filepath
  return $ lines content

parseLine line = (cmd, value)
  where
    cmd = take 4 line
    value = case cmd of
      "addx" -> read (drop 5 line) :: Int
      _ -> 0

-- Process the instructions and return a list
-- of a tuple consisting of (# cycle, value of x).
runProgram :: [(String, Int)] -> [(Int, Int)] -> [(Int, Int)]
runProgram [] acc = reverse acc
runProgram ins [] = runProgram ins [(1, 1)]
runProgram ((ins, value) : tail) acc@((cycle, regx) : rest) =
  case ins of
    "addx" -> runProgram tail (b : a : acc)
      where
        a = (cycle + 1, regx)
        b = (cycle + 2, regx + value)
    "noop" -> runProgram tail ((cycle + 1, regx) : acc)
    _ -> error "unreachable"

isTargetCycle cycle
  | cycle > 220 = False
  | cycle == 20 = True
  | (cycle - 20) `mod` 40 == 0 = True
  | otherwise = False

filterTargets :: [(Int, Int)] -> [(Int, Int)]
filterTargets = filter (\(c, _) -> isTargetCycle c)

sumStrengths results = sum nums
  where
    nums = map (uncurry (*)) results

replace list index item = head ++ [item] ++ tail
  where
    (head, _ : tail) = splitAt index list
