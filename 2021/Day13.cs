using System;
using System.Collections.Generic;
using System.IO;
using System.IO.Compression;
using System.Linq;
using System.Runtime.InteropServices;
using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    
    public class Day13 : BaseDay
    {

        public Day13() : base(13, 2021)
        {
            
        }

        private int[,] grid;
        public override string SolvePartOne()
        {
            int output = 0;
            var input = Input.Read2D<int>(',');
            var _path = $"..\\..\\input\\2021\\13_2.txt";
            var folds =File.ReadAllLines(_path).ToList();

            int heigth = 0, width = 0;
            bool first_fold = true;
            
            for (int i = 0; i < input.Count; i++)
            {
                if (input[i][0] > width)
                    width = input[i][0];
                if (input[i][1] > heigth)
                    heigth = input[i][1];
            }
            
            grid = new int[width+1, heigth+1];
            foreach (var point in input)
            {
                grid[point[0], point[1]] = 1;
            }

            int[,] new_grid = new int[0,0];
            //fold
            foreach (var fold in folds)
            {
                var spl = fold.Split(new char[] {' ', '='});
                var dir = spl[2];
                int val = int.Parse(spl[3]);
                if (dir == "y")
                {
                    new_grid = new int[grid.GetLength(0), val];
                    for (int x = 0; x < grid.GetLength(0); x++)
                    {
                        for (int y = 0; y < val; y++)
                        {
                            if(2*val - y < grid.GetLength(1))
                                new_grid[x, y] = grid[x, y] + grid[x, 2*val - y];
                        }
                    }
                }
                else if (dir == "x")
                {
                    new_grid = new int[val, grid.GetLength(1)];
                    for (int x = 0; x < val; x++)
                    {
                        for (int y = 0; y < grid.GetLength(1); y++)
                        {
                            if(2*val - x < grid.GetLength(0))
                                new_grid[x, y] = grid[x, y] + grid[2*val - x, y];
                        }
                    }
                }

                grid = new_grid;

                if (first_fold)
                {
                    foreach (var p in grid)
                    {
                        if (p > 0)
                            output++;
                    }

                    first_fold = false;
                }
            }

            
            return $"{output}";
        }

        public override string SolvePartTwo()
        {
            int output = 0;
            Console.WriteLine($"x{grid.GetLength(0)},y{grid.GetLength(1)}");
            for (int i = 0; i < grid.GetLength(1); i++)
            {
                for (int j = 0; j < grid.GetLength(0); j++)
                {
                    string s = grid[j, i] > 0 ? "#" : ".";
                    Console.Write(s);
                }
                Console.WriteLine();
            }
            return $"{output}";
        }
    }
}