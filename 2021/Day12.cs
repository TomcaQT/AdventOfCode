using System;
using System.Collections.Generic;
using System.IO.Compression;
using System.Linq;
using System.Runtime.InteropServices;
using AdventOfCode.Utilities;

namespace AdventOfCode._2021
{
    public class Day12 : BaseDay
    {

        public Day12() : base(12, 2021)
        {
            
        }

        public class Node
        {
            public string Name;

            public HashSet<Node> neis;
            
            public Node(string name)
            {
                Name = name;
                neis = new HashSet<Node>();
            }

            public bool IsSmall() => Name.ToList().TrueForAll(c => c >= 'a' && c <= 'z');

            public void AddNei(Node n)
            {
                neis.Add(n);
            }
            
            
        }
        


        public struct Conf
        {
            public Dictionary<string, Node> nodes;
            public HashSet<Node> visited;
            public List<Node> path;
            public bool usedDouble;
        }
        
        public override string SolvePartOne()
        {
            int output = 0;
            var input = Input.Read2D<string>('-');
            Dictionary<string,Node> nodes = new Dictionary<string, Node>();
            foreach (var line in input)
            {
                var name1 = line[0];
                var name2 = line[1];
                if(!nodes.ContainsKey(name1))
                    nodes.Add(name1,new Node(name1));
                if(!nodes.ContainsKey(name2))
                    nodes.Add(name2,new Node(name2));
                nodes[name1].AddNei(nodes[name2]);
                nodes[name2].AddNei(nodes[name1]);
            }

            Queue<Conf> qu = new Queue<Conf>();
            qu.Enqueue(new Conf()
            {
                nodes = nodes,
                path = new List<Node>(){nodes["start"]},
                visited = new HashSet<Node>(){nodes["start"]}
            });
            while (qu.Count > 0)
            {
                var conf = qu.Dequeue();
                var curr = conf.path[conf.path.Count - 1];
                if (curr.Name == "end")
                {
                    output++;
                    continue;
                }

                
                foreach (var nei in curr.neis)
                {
                    HashSet<Node> visited = new HashSet<Node>(conf.visited);
                    List<Node> path = new List<Node>(conf.path);
                    if(visited.Contains(nei))
                        continue;
                    if (nei.IsSmall())
                        visited.Add(nei);
                    path.Add(nei);
                    var newConf = new Conf()
                    {
                        nodes = conf.nodes,
                        path = path,
                        visited = visited
                    };
                    qu.Enqueue(newConf);
                }
            }
            //FindPath(nodes, new HashSet<Node>(), new List<Node>() {nodes["start"]});
            
            return $"{output}";
        }

        public override string SolvePartTwo()
        {
            int output = 0;
            var input = Input.Read2D<string>('-');
            Dictionary<string,Node> nodes = new Dictionary<string, Node>();
            foreach (var line in input)
            {
                var name1 = line[0];
                var name2 = line[1];
                if(!nodes.ContainsKey(name1))
                    nodes.Add(name1,new Node(name1));
                if(!nodes.ContainsKey(name2))
                    nodes.Add(name2,new Node(name2));
                nodes[name1].AddNei(nodes[name2]);
                nodes[name2].AddNei(nodes[name1]);
            }

            Queue<Conf> qu = new Queue<Conf>();
            qu.Enqueue(new Conf()
            {
                nodes = nodes,
                path = new List<Node>(){nodes["start"]},
                visited = new HashSet<Node>(){nodes["start"]},
                usedDouble = false
            });
            while (qu.Count > 0)
            {
                var conf = qu.Dequeue();
                var curr = conf.path[conf.path.Count - 1];
                if (curr.Name == "end")
                {
                    output++;
                    continue;
                }

                
                foreach (var nei in curr.neis)
                {
                    HashSet<Node> visited = new HashSet<Node>(conf.visited);
                    List<Node> path = new List<Node>(conf.path);
                    bool uD = conf.usedDouble;
                    if (visited.Contains(nei))
                    {

                        if (uD || nei.Name == "start")
                            continue;
                        else
                            uD = true;
                    }
                    if (nei.IsSmall())
                        visited.Add(nei);
                    path.Add(nei);
                    var newConf = new Conf()
                    {
                        nodes = conf.nodes,
                        path = path,
                        visited = visited,
                        usedDouble = uD
                    };
                    qu.Enqueue(newConf);
                }
            }
            //FindPath(nodes, new HashSet<Node>(), new List<Node>() {nodes["start"]});
            
            return $"{output}";
        }
    }
}