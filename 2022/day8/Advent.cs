namespace Advent
{
    public class Solution
    {
        private readonly Grid grid;

        public Solution(string[] lines) => grid = Grid.FromLines(lines);

        public int Part1() => grid.VisibleCount();

        public int Part2() => grid.ScenicScores();
    }

    class Grid
    {
        private readonly int[,] grid;
        readonly int nRows;
        readonly int nCols;

        public Grid(int[,] grid)
        {
            this.grid = grid;
            nRows = grid.GetLength(0);
            nCols = grid.GetLength(1);
        }

        public static Grid FromLines(string[] lines)
        {
            var tmp = lines
                .Select(line => line.Select(n => int.Parse(n.ToString())).ToArray())
                .ToArray();

            var rows = tmp.Length;
            var cols = tmp[0].Length;

            var grid = new int[rows, cols];
            for (var x = 0; x < rows; x++)
                for (var y = 0; y < cols; y++) grid[x, y] = tmp[x][y];

            return new Grid(grid);
        }

        // Part 1
        public int VisibleCount()
        {
            var edgeCount = nRows * 2 + (nCols - 2) * 2;
            return edgeCount + InteriorCoords().Where(coord => TreeVisible(coord.Item1, coord.Item2)).Count();
        }

        public int ScenicScores() => InteriorCoords()
            .Select(coord => ScenicScore(coord.Item1, coord.Item2))
            .Max(s => s);

        private int ScenicScore(int row, int col)
        {
            var treeHeight = grid[row, col];

            var above = 0;
            foreach (var h in GetCol(col, 0, row).Reverse())
            {
                above++;
                if (h >= treeHeight) break;
            }
            var below = 0;
            foreach (var h in GetCol(col, row + 1, nCols))
            {
                below++;
                if (h >= treeHeight) break;
            }

            var right = 0;
            foreach (var h in GetRow(row, col + 1, nCols))
            {
                right++;
                if (h >= treeHeight) break;
            }
            var left = 0;
            foreach (var h in GetRow(row, 0, col).Reverse())
            {
                left++;
                if (h >= treeHeight) break;
            }

            return above * below * left * right;
        }

        public bool TreeVisible(int row, int col)
        {
            var treeHeight = grid[row, col];
            if (GetCol(col, 0, row).All(h => h < treeHeight)) return true;
            if (GetCol(col, row + 1, nCols).All(h => h < treeHeight)) return true;
            if (GetRow(row, col + 1, nCols).All(h => h < treeHeight)) return true;
            if (GetRow(row, 0, col).All(h => h < treeHeight)) return true;
            return false;
        }

        private int[] GetRow(int row, int fromCol, int toCol)
        {
            var acc = new LinkedList<int>();
            for (var i = fromCol; i < toCol; i++) acc.AddLast(grid[row, i]);
            return acc.ToArray();
        }

        private int[] GetCol(int col, int fromRow, int toRow)
        {
            var acc = new LinkedList<int>();
            for (var i = fromRow; i < toRow; i++) acc.AddLast(grid[i, col]);
            return acc.ToArray();
        }

        private IEnumerable<(int, int)> InteriorCoords()
        {
            for (var x = 1; x < nRows - 1; x++)
            {
                for (var y = 1; y < nCols - 1; y++)
                {
                    yield return (x, y);
                }
            }
        }
    }
}
