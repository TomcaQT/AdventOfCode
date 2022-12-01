using System;
using System.Collections.Generic;

namespace AdventOfCode.Utilities
{
    /// <summary>
    /// Compact static class for printing
    /// </summary>
    public static class c
    {
        /// <summary>
        /// Console.WriteLine
        /// </summary>
        /// <param name="s"></param>
        public static void wl(string s) => Console.WriteLine(s);
        /// <summary>
        /// Console.Write
        /// </summary>
        /// <param name="s"></param>
        public static void w(string s) => Console.Write(s);
        /// <summary>
        /// Print IEnumerable to multiple lines
        /// </summary>
        /// <param name="list"></param>
        /// <typeparam name="T"></typeparam>
        public static void dbg<T>(IEnumerable<T> list)
        {
            wl("===");
            foreach (var x in list)
                wl(x.ToString());
            wl("===");
        }
        /// <summary>
        /// Print IEnumarable to one line separated by " ; "
        /// </summary>
        /// <param name="list"></param>
        /// <typeparam name="T"></typeparam>
        public static void dbgl<T>(IEnumerable<T> list)
        {
            foreach (var x in list)
                w(x.ToString() + " ; ");
            wl("");
        }
        
    }
}