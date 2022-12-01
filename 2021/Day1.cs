using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    public class Day1 : BaseDay
    {

        public Day1() : base(1, 2021)
        {
            
        }

        public override string SolvePartOne()
        {
            int output = 0;
            var input = Input.Read<int>();
            int prev = input[0];
            for (int i = 1; i < input.Count; i++)
            {
                if (input[i] > prev)
                    output++;
                prev = input[i];
            }
            return $"{output}";
        }

        public override string SolvePartTwo()
        {
            int output = 0;
            var input = Input.Read<int>();
            int prev = input[0] + input[1] +  input[2];
            for (int i = 3; i < input.Count; i++)
            {
                if ((prev - input[i-3] + input[i]) > prev)
                    output++;
                prev = prev - input[i-3] + input[i];
            }
            return $"{output}";
        }
    }
}