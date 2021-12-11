using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    public class Day11 : BaseDay
    {

        public Day11() : base(11, 2021)
        {
            
        }

        public class Octopus
        {
            public Octopus(int value, int x, int y)
            {
                Value = value;
                flashed = 0;
                X = x;
                Y = y;
            }

            public bool Inc()
            {
                Value++;
                if (Value > 9 && isFlash == false)
                {
                    Flash();
                    return true;
                }
                return false;
            }

            public void Flash()
            {
                isFlash = true;
                flashed++;
            }

            public void Reset()
            {
                Value = 0;
                isFlash = false;
            }
            
            public int Value;
            public int X;
            public int Y;
            public bool isFlash = false;

            public int flashed;

        }

        private int PartTwo = 0;
        public override string SolvePartOne()
        {
            int output = 0;
            var inp = Input.Read();
            List<List<Octopus>> input = new List<List<Octopus>>();
            for (int i = 0; i < inp.Count; i++)
            {
                var line = inp[i];
                List<Octopus> row = new List<Octopus>();
                for (int j = 0; j < line.Length; j++)
                {
                    row.Add(new Octopus(int.Parse(line[j].ToString()),i,j));
                }
                input.Add(row);
            }

            int maxStep = 10000;
            for (int a = 0; a < maxStep; a++)
            {
                
                for (int i = 0; i < input.Count; i++)
                {
                    for (int j = 0; j < input[i].Count; j++)
                    {
                        input[i][j].Inc();
                    }
                }

                HashSet<Octopus> worked = new HashSet<Octopus>();
                Queue<Octopus> toWork = new Queue<Octopus>();
                input.ForEach(line => line.Where(x => x.isFlash).ToList().ForEach(o => toWork.Enqueue(o)));
                input.ForEach(line => line.Where(x => x.isFlash).ToList().ForEach(o => worked.Add(o)));

                while (toWork.Count > 0)
                {
                    var curr = toWork.Dequeue();
                    int i = curr.X;
                    int j = curr.Y;
                    for (int x = Math.Max(0,i-1); x <= Math.Min(i+1,input.Count-1); x++)
                    {
                        for (int y = Math.Max(0,j-1); y <= Math.Min(j+1,input[x].Count-1); y++)
                        {
                            input[x][y].Inc();

                            if (input[x][y].isFlash && !worked.Contains(input[x][y]))
                            {
                                toWork.Enqueue(input[x][y]);
                                worked.Add(input[x][y]);
                            }
                        }
                    }
                }
                
                input.ForEach(line => line.Where(x => x.isFlash).ToList().ForEach(o => o.Reset()));
                
                //Part1
                if(a == 100-1)
                    input.ForEach(line => line.ForEach(o => output += o.flashed));
                //Part2
                var p2 = input.TrueForAll(line => line.TrueForAll(o => o.Value == 0));
                if (p2)
                {
                    PartTwo = a+1;
                    break;
                }
            }
            
            
            return $"{output}";
        }

        
        public override string SolvePartTwo()
        {
            int output = PartTwo;
            
            return $"{output}";
        }
    }
}