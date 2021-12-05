using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    public class Day5 : BaseDay
    {

        public Day5() : base(5, 2021)
        {
            
        }

        public override string SolvePartOne()
        {
            int output = 0;
            var i = Input.Read2D<int>(new string[] {" -> ", ","}, StringSplitOptions.RemoveEmptyEntries);
            Dictionary<(int, int), int> map = new Dictionary<(int, int), int>();
            foreach (var l in i)
            {
                int x1 = l[0];
                int y1 = l[1];
                int x2 = l[2];
                int y2 = l[3];
                int from, to,s;
                //C/onsole.WriteLine($"{x1},{y1}.{x2},{y2}");
                if (y1 == y2)
                {
                    from = Math.Min(x1, x2);
                    to = Math.Max(x1, x2);
                    s = y1;
                    for (int j = from; j <= to; j++)
                    {
                        if(!map.ContainsKey((j,s)))
                            map.Add((j,s),0);
                        map[(j, s)] += 1;
                    }
                }
                else if (x1 == x2)
                {
                    from = Math.Min(y1, y2);
                    to = Math.Max(y1, y2);
                    s = x1;
                    for (int j = from; j <= to; j++)
                    {
                        if(!map.ContainsKey((s,j)))
                            map.Add((s,j),0);
                        map[(s, j)] += 1;
                    }
                }
                else 
                {
                    if (x1 > x2)
                    {
                        int tmp = x1;
                        x1 = x2;
                        x2 = tmp;
                        tmp = y1;
                        y1 = y2;
                        y2 = tmp;
                    }
                    int y = y1;
                    int dy = y1 < y2 ? 1 : -1;
                    for (int x = x1; x <= x2; x+=1)
                    {
                        if(!map.ContainsKey((x,y)))
                            map.Add((x,y),0);
                        map[(x, y)] += 1;
                        y += dy;
                    }
                }


            }

            output = map.Values.Where(x => x >= 2).Count();

            return $"{output}";
        }

        public override string SolvePartTwo()
        {
            int output = 0;

            return $"{output}";
        }
    }
}