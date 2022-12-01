using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    public class Day8 : BaseDay
    {

        public Day8() : base(8, 2021)
        {
            
        }
        
 
        private HashSet<int> lens = new HashSet<int>() {2, 4, 3, 7};
        public override string SolvePartOne()
        {
            int output = 0;
            var input = Input.Read1D<string>('|');
            for (int i = 1; i < input.Count; i+=2)
            {
                var line = input[i].Split(new char[]{' '}, StringSplitOptions.RemoveEmptyEntries);
                foreach (var s in line)
                    if (lens.Contains(s.Length))
                        output++;
            }
            
            return $"{output}";
        }


        public HashSet<char> StrToH(string s)
        {
            HashSet<char> h = new HashSet<char>(s.ToCharArray());
            return h;
        }


        private HashSet<char>[] known;
        public void Decode(string s)
        {
            var h = StrToH(s);
            if (s.Length == 2)
                known[1] = h;
            if (s.Length == 3)
                known[7] = h;
            if (s.Length == 4)
                known[4] = h;
            if (s.Length == 7)
                known[8] = h;
            if (s.Length == 6)
            {
                if (h.Intersect(known[1]).Count() == 1)
                    known[6] = h;
                else if (h.Intersect(known[4]).Count() == 4)
                    known[9] = h;
                else
                    known[0] = h;
            }
            if (s.Length == 5)
            {
                if (h.Intersect(known[6]).Count() == 5)
                    known[5] = h;
                else if (h.Intersect(known[1]).Count() == 2)
                    known[3] = h;
                else
                    known[2] = h;
            }
        }

        private bool IsSame(HashSet<char> a, HashSet<char> b)
        {
            if (a.Count() != b.Count())
                return false;
            foreach (var x in a)
            {
                if (!b.Contains(x))
                    return false;
            }

            return true;
        }
        
        private int GetVal(string s)
        {
            var h = StrToH(s);
            for (int i = 0; i < 10; i++)
            {
                if (IsSame(h, known[i]))
                    return i;
            }
            return -1;
        }
        
        
        public override string SolvePartTwo()
        {
            int output = 0;
            //int avg = (int)Math.Round(input.Average());
            var input = Input.Read1D<string>('|');
            
            for (int i = 1; i < input.Count; i+=2)
            {
                var inp = input[i - 1].Split(new char[] {' '}, StringSplitOptions.RemoveEmptyEntries);
                known = new HashSet<char>[10];
                Decode(inp.First(x => x.Length == 2));
                Decode(inp.First(x => x.Length == 4));
                Decode(inp.First(x => x.Length == 3));
                Decode(inp.First(x => x.Length == 7));
                inp.Where(x => x.Length == 6).ToList().ForEach(x => Decode(x));
                inp.Where(x => x.Length == 5).ToList().ForEach(x => Decode(x));
                
                
                var line = input[i].Split(new char[]{' '}, StringSplitOptions.RemoveEmptyEntries);
                int num = 0;
                int o = 1000;
                for (int j = 0; j < 4; j++)
                {
                    num += o * GetVal(line[j]);
                    o /= 10;
                }
                output += num;
            }
            
            return $"{output}";
        }
    }
}