using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    public class Day10 : BaseDay
    {

        public Day10() : base(10, 2021)
        {
            
        }

        private Dictionary<char, char> opposite = new Dictionary<char, char>()
        {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'},
            {'<', '>'}
        };
        
        private Dictionary<char, int> score = new Dictionary<char, int>()
        {
            {')', 3},
            {'}', 1197},
            {']', 57},
            {'>', 25137},
            {'(', 1},
            {'{', 3},
            {'[', 2},
            {'<', 4}
        };
        public override string SolvePartOne()
        {
            int output = 0;
            int sc = 0;
            List<int> scores = new List<int>();
            var input = Input.Read();
            foreach (var line in input)
            {
                Stack<char> s = new Stack<char>();
                bool complete = true;
                foreach (var c in line)
                {
                    if(c == '(' || c == '{' || c == '[' || c == '<')
                        s.Push(c);
                    else
                    {
                        char x = s.Pop();
                        if (opposite[x] != c)
                        {
                            output += score[c];
                            complete = false;
                            break;
                        }
                            
                    }
                }
            }
            
            return $"{output}";
        }

        
        public override string SolvePartTwo()
        {
            int output = 0;
            Int64 sc = 0;
            List<Int64> scores = new List<Int64>();
            var input = Input.Read();
            foreach (var line in input)
            {
                Stack<char> s = new Stack<char>();
                bool complete = true;
                foreach (var c in line)
                {
                    if(c == '(' || c == '{' || c == '[' || c == '<')
                        s.Push(c);
                    else
                    {
                        char x = s.Pop();
                        if (opposite[x] != c)
                        {
                            output += score[c];
                            complete = false;
                            break;
                        }
                            
                    }
                }
                sc = 0;
                if (complete)
                {
                    while (s.Count > 0)
                    {
                        sc *= 5;
                        char c = s.Pop();
                        sc += score[c];
                        //Console.Write(c);
                    }
                    //Console.WriteLine($" : score:{sc}");
                    scores.Add(sc);
                }
            }
            scores.Sort();
            return $"{scores[scores.Count / 2]}";
        }
    }
}