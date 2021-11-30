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
        
        protected abstract string SolvePartOne();
        protected abstract string SolvePartTwo();
    }
}