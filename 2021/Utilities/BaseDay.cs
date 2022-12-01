namespace AdventOfCode.Utilities
{
    public abstract class BaseDay
    {

        public int Day;
        public int Year;

        public InputReader Input;
        
        public BaseDay(int day, int year)
        {
            Day = day;
            Year = year;

            Input = new InputReader(day, year);
        }
        
        public abstract string SolvePartOne();
        public abstract string SolvePartTwo();
    }
}