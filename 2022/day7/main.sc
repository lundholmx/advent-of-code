import scala.io.Source

@main def main(filepath: String): Unit = 
  val lines = Source.fromFile(filepath).getLines.toList

  val fs = build(lines)
  val total = 70000000
  val updateSize = 30000000

  val dirs = findDirs(fs)
  val rootSize = recSize(fs)
  val sizes = for (d <- dirs) yield recSize(d)

  // Part 1
  val small = for (s <- sizes if s < 100000) yield s
  val part1 = small.reduce(_ + _)
  println(s"Part 1: $part1")

  // Part 2
  val unused = total - rootSize
  val selections = for (
    size <- sizes
    if size+unused > updateSize
  ) yield size
  val part2 = selections.min
  println(s"Part 2: $part2")


val cdPattern = """^\$ cd (.+)$""".r
val lsPattern = """^\$ ls""".r
val dirPattern = """^dir ([a-z]+)$""".r
val filePattern = """^(\d+) (.+)$""".r

type Entry = Dir | File

class File(val name: String, val size: Int) {
  def print(prefix: String) = {
    println(s"$prefix - file: $name")
  }
}

class Dir(
  val name: String,
  val parent: Option[Dir],
  var contains: List[Entry]
) {
  def push(entry: Entry) = {
    contains = entry :: contains
  }
}

def findDirs(root: Dir): List[Dir] = {
  var acc: List[Dir] = List()

  def rec(dir: Dir): Unit = {
    acc = dir :: acc
    for (case (d:Dir) <- dir.contains) {
      rec(d)
    }
  }

  rec(root)
  acc
}

def recSize(dir: Dir): Int = {
  var total = 0

  for (child <- dir.contains) {
    val size = child match {
      case f:File => f.size
      case d:Dir => recSize(d)
    }
    total += size
  }

  total
}

def build(lines: List[String]): Dir = {
  var current: Option[Dir] = None
  
  for {
    line <- lines
  } {
      line match {
        case lsPattern() => {}
        case dirPattern(name) => {}
        case cdPattern(d) => d match {
          case ".." => {
            current = current.get.parent
          }
          case other => current match {
            case Some(dir) => {
              var curr = dir
              var temp = Dir(other, Some(dir), List())
              dir.push(temp)
              current = Some(temp)
            }
            case None => {
              current = Some(Dir(other, None, List()))
            }
          }
        }
        case filePattern(size, name) => {
          current match {
            case Some(dir) => dir.push(File(name, size.toInt))
            case None => println("-- UNREACHABLE --")
          }
        }
      }
  }

  while (!current.get.parent.isEmpty) {
    current = current.get.parent
  }

  current.get
}
