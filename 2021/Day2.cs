using System;
using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    public class Day2 : BaseDay
    {

        public Day2() : base(2, 2021)
        {
            
        }

        public override string SolvePartOne()
        {
            int hor=0,dep = 0;
            var input = Input.Read2D<string>(' ');
            foreach (var line in input)
            {
                int val = Convert.ToInt32(line[1]);
                if (line[0] == "forward")
                {
                    hor += val;
                }
                else if (line[0] == "up")
                {
                    dep -= val;
                }
                else
                {
                    dep += val;
                }
            }
            return $"{dep*hor}";
        }

        public override string SolvePartTwo()
        {
            int hor=0,dep = 0,aim = 0;
            var input = Input.Read2D<string>(' ');
            foreach (var line in input)
            {
                int val = Convert.ToInt32(line[1]);
                if (line[0] == "forward")
                {
                    hor += val;
                    dep += aim * val;
                }
                else if (line[0] == "up")
                {
                    aim -= val;
                }
                else
                {
                    aim += val;
                }
            }
            return $"{dep*hor}";
        }
    }
}