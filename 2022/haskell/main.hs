import System.Environment 
import System.IO

main :: IO()
main = do
  (inputFilepath:_) <- getArgs
  lines <- readLines inputFilepath
  output lines


readLines :: FilePath -> IO [String]
readLines filepath = do
  content <- readFile filepath
  return $ lines content


output :: [String] -> IO ()
output [] = return ()
output (xs:tail) = do
  putStrLn xs
  output tail
