using System;
using AdventOfCode.Utilities;

namespace AdventOfCode
{
    internal class Program
    {
        public static void Main(string[] args)
        {
            var day = new _2021.Day3();
            Console.WriteLine($"Part one: {day.SolvePartOne()}");
            Console.WriteLine($"Part two: {day.SolvePartTwo()}");
            //Console.ReadKey();
        }
    }
}