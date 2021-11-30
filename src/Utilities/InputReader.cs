using System;
using System.Collections.Generic;
using System.IO;

namespace AdventOfCode.Utilities
{
    public class InputReader
    {
        private string _path;

        public InputReader(int day, int year)
        {
            _path = $"input\\{year}\\{day}.txt";
        }
        
        public List<T> Read<T>()
        {
            List<T> input = new List<T>();

            return input;
        }
        
        
    }
}