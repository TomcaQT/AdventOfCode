using System;
using System.Collections.Generic;
using System.Linq;
using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    public class Day9 : BaseDay
    {

        public Day9() : base(9, 2021)
        {
            
        }


        private bool CheckLower(List<string> input,int i, int j)
        {
            int num = int.Parse(input[i][j].ToString());
            bool flag = true;
                    
                    
            if(i-1 >= 0)
                if(num >= int.Parse(input[i-1][j].ToString()))
                    flag = false;
                    
            if(i+1 < input.Count)
                if(num >= int.Parse(input[i+1][j].ToString()))
                    flag = false;
                    
            if(j-1 >= 0)
                if(num >= int.Parse(input[i][j-1].ToString()))
                    flag = false;
                    
            if(j+1 < input[i].Length)
                if(num >= int.Parse(input[i][j+1].ToString()))
                    flag = false;
            return flag;
        }
        
        public override string SolvePartOne()
        {
            int output = 0;
            //int avg = (int)Math.Round(input.Average());
            var input = Input.Read<string>();
            for (int i = 0; i < input.Count; i++)
            {
                for (int j = 0; j < input[i].Length; j++)
                {
                    int num = int.Parse(input[i][j].ToString());

                    if (CheckLower(input,i,j))
                    {
                        //Console.WriteLine($"y:{i},x:{j}, num : {num}");
                        output += num + 1;
                    }
                }
            }
            
            return $"{output}";
        }

      
        
        public override string SolvePartTwo()
        {
            int output = 0;
            //int avg = (int)Math.Round(input.Average());
            
            
            return $"{output}";
        }
    }
}