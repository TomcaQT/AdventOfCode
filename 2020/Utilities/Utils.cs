namespace AdventOfCode.Utilities
{
    public static class Utils
    {
        public static bool CheckBounds(int x, int l, int u) => x >= l && x <= u;
        public static bool CheckBoundsInc(int x, int l, int u) => x >= l && x <= u;
        public static bool CheckBoundsEx(int x, int l, int u) => x > l && x < u;
        public static bool CheckBoundsOut(int x, int l, int u) => x < l || x > u;
        

    }
}