using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    public class Day3 : BaseDay
    {

        public Day3() : base(3, 2021)
        {
            
        }

        public override string SolvePartOne()
        {
            var input = Input.Read<string>();
            int[] ones = new int [input[0].Length];
            int h = input.Count / 2;
            string g = "", e = "";
            foreach (var line in input)
            {
                for (int i = 0; i < line.Length; i++)
                {
                    ones[i] += int.Parse(line[i].ToString());
                }
            }

            foreach (var o in ones)
            {
                if (o > h)
                {
                    g += "1";
                    e += "0";
                }
                else
                {
                    e += "1";
                    g += "0";
                }
            }

            return $"{Convert.ToInt32(g,2)*Convert.ToInt32(e,2)}";
        }

        public override string SolvePartTwo()
        {
            string output = "";
            var input = Input.Read<string>();
            int h = input.Count / 2;
            
        

            int index = 0;
            var i1 = new List<string>(input);
            while (i1.Count != 1)
            {
                h = i1.Count / 2;
                if (GetCount(i1,index,'1') >= GetCount(i1,index,'0'))
                    i1.RemoveAll(x => x[index] == '0');
                else
                    i1.RemoveAll(x => x[index] == '1');
                Console.WriteLine(i1.Count);
                index++;
            }
            Console.WriteLine($"-----{1/2}");
            index = 0;
            var i2 = new List<string>(input);
            while (i2.Count != 1)
            {
                if (GetCount(i2,index,'0') > GetCount(i2,index,'1'))
                    i2.RemoveAll(x => x[index] == '0');
                else
                    i2.RemoveAll(x => x[index] == '1');
                    
                Console.WriteLine(i2.Count);
                index++;
            }
            
            
            
            return $"{Convert.ToInt32(i1[0],2)},{Convert.ToInt32(i2[0],2)} --{Convert.ToInt32(i1[0],2) * Convert.ToInt32(i2[0],2)}";
        }

        public int GetCount(List<string> input, int index,char val)
        {
            int o = 0;
            foreach (var line in input)
            {
                if (line[index] == val)
                    o++;
            }
            return o;
        }
    }
}