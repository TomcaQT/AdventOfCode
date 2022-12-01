using AdventOfCode.Utilities;

namespace AdventOfCode._2020
{
    public class Day1 : BaseDay
    {

        public Day1() : base(1, 2020)
        {
            
        }

        public override string SolvePartOne()
        {
            int output = 0;
            var input = Input.Read<int>();
            for (int i = 0; i < input.Count-1; i++)
            {
                for (int j = i+1; j < input.Count; j++)
                {
                    if (input[i] + input[j] == 2020)
                    {
                        output = input[i] * input[j];
                        return $"{output}";
                    }
                }
            }
            return $"{output}";
        }

        public override string SolvePartTwo()
        {
            int output = 0;
            var input = Input.Read<int>();
            for (int i = 0; i < input.Count-2; i++)
            {
                for (int j = i+1; j < input.Count-1; j++)
                {
                    for (int k = j+1; k < input.Count; k++)
                    {
                        if (input[i] + input[j] + input[k] == 2020)
                        {
                            output = input[i] * input[j] * input[k];
                            return $"{output}";
                        }
                    }
                }
            }
            return $"{output}";
        }
    }
}