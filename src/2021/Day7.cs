using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    public class Day7 : BaseDay
    {

        public Day7() : base(7, 2021)
        {
            
        }
        
        public override string SolvePartOne()
        {
            int output;
            var input = Input.Read2D<int>(',')[0];
            input.Sort();
            int med = input[input.Count / 2];
            output = input.Sum(i => Math.Abs(i - med));
            return $"{output}";
        }

        public override string SolvePartTwo()
        {
            int output = 0;
            var input = Input.Read2D<int>(',')[0];
            int avg = (int)Math.Round(input.Average());
            output = input.Sum(i => (Math.Abs(i - avg)*(1+Math.Abs(i - avg)))/2);
            return $"{output}";
        }
    }
}