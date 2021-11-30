using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;

namespace AdventOfCode.Utilities
{
    public class InputReader
    {
        private string _path;

        public InputReader(int day, int year)
        {
            string dayS = day.ToString().Length == 1 ? $"0{day.ToString()}" : day.ToString();
            _path = $"..\\..\\input\\{year}\\{dayS}.txt";
        }

        public List<string> Read() => File.ReadAllLines(_path).ToList();
        
        public List<T> Read<T>()
        {
            List<T> input = new List<T>();
            var lines = Read();
            foreach (var line in lines)
                input.Add((T)Convert.ChangeType(line, typeof(T)));
            return input; 
        }

        public List<List<T>> Read2D<T>(char[] sep, StringSplitOptions options = StringSplitOptions.None)
        {
            List<List<T>> input = new List<List<T>>();
            var lines = Read();
            foreach (var line in lines)
            {
                List<T> row = new List<T>();
                foreach (var s in line.Split(sep,options))
                    row.Add((T)Convert.ChangeType(s, typeof(T)));
                input.Add(row);
            }

            return input;
        }
        public List<List<T>> Read2D<T>(char sep)
        {
            List<List<T>> input = new List<List<T>>();
            var lines = Read();
            foreach (var line in lines)
            {
                List<T> row = new List<T>();
                foreach (var s in line.Split(sep))
                    row.Add((T)Convert.ChangeType(s, typeof(T)));
                input.Add(row);
            }

            return input;
        }
        public List<List<T>> Read2D<T>(string[] sep, StringSplitOptions options = StringSplitOptions.None)
        {
            List<List<T>> input = new List<List<T>>();
            var lines = Read();
            foreach (var line in lines)
            {
                List<T> row = new List<T>();
                foreach (var s in line.Split(sep,options))
                    row.Add((T)Convert.ChangeType(s, typeof(T)));
                input.Add(row);
            }

            return input;
        }
        
        
    }
}