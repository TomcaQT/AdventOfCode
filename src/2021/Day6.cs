using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    public class Day6 : BaseDay
    {

        public Day6() : base(6, 2021)
        {
            
        }

        private void PrintArr(List<int> a, int i )
        {
            Console.Write($"After day {i}: ");
            foreach (var x in a)
            {
                Console.Write($"{x},");
                
            }
            Console.WriteLine();
        }
        
        public override string SolvePartOne()
        {
            int output = 0;
            this.target = 80;
            var fish = new int[9];
            var input = Input.Read2D<int>(',')[0];
            
            for (int i = 0; i < 9; i++)
                fish[i] = input.Count(x => x == i);

            for (int i = 0; i < target; i++)
            {
                var new_fish = new int[9];
                for (int j = 0; j < 9; j++)
                {
                    if (j == 0)
                    {
                        new_fish[6] += fish[0];
                        new_fish[8] += fish[0];
                    }
                    else
                    {
                        new_fish[j-1] += fish[j];
                    }
                }

                fish = new_fish;
                //Console.WriteLine($"Day{i}");
                //PrintArr(input,i+1);
            }
            fish.ToList().ForEach(x => output += x);
            return $"{output}";
        }

        private int target = 0;

        public int Next(int x)
        {
            x -= 1;
            if (x < 0)
                return 8;
            return x;
        }
        
        public override string SolvePartTwo()
        {
            UInt64 output = 0;
            this.target = 256;
            UInt64 tar = 256;
            var fish = new UInt64[9];
            var input = Input.Read2D<UInt64>(',')[0];
            
            for (UInt64 i = 0; i < 9; i++)
                fish[i] = (UInt64)input.Count(x => x == i);

            for (UInt64 i = 0; i < tar; i++)
            {
                var new_fish = new UInt64[9];
                for (int j = 0; j < 9; j++)
                {
                    if (j == 0)
                    {
                        new_fish[6] += fish[0];
                        new_fish[8] += fish[0];
                    }
                    else
                    {
                        new_fish[j-1] += fish[j];
                    }
                }

                fish = new_fish;
                //Console.WriteLine($"Day{i}");
                //PrintArr(input,i+1);
            }
            fish.ToList().ForEach(x => output += x);
            return $"{output}";
        }
    }
}