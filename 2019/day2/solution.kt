import java.io.File
import kotlin.math.*

fun dist(x: Pair<Int, Int>, y: Pair<Int, Int>): Int {
    if (y == Pair(0,0))
        return Int.MAX_VALUE
    return abs(x.first - y.first) + abs(x.second - y.second)
}

val dirs = mapOf('R' to Pair(0,1), 'L' to Pair(0,-1), 'U' to Pair(1,0), 'D' to Pair(-1,0))
var steps: MutableMap<Pair<Int,Int>, Int> = mutableMapOf()
fun solve(data: List<List<String>>) {
    val w1 = data[0]; val w2 = data[1]
    var grid: MutableSet<Pair<Int, Int>> = mutableSetOf()
    var curr = Pair(0,0); var currSteps = 0
    for (cmd in w1) {
        val x = cmd[0]
        val dir: Pair<Int, Int> = dirs[x]!!
        val c = cmd.substring(1).toInt()
        val pos: MutableList<Pair<Int, Int>> = mutableListOf()
        (1..c).toList().forEach {x -> pos.add(Pair(curr.first + dir.first*x, curr.second + dir.second*x))}
        pos.forEach {x -> grid.add(x)}
        pos.forEach {x -> steps.put(x, ++currSteps)}
        curr = Pair(curr.first + dir.first*c, curr.second + dir.second*c)
    }

    var closest = Int.MAX_VALUE
    var minSteps = Int.MAX_VALUE
    currSteps = 0
    curr = Pair(0,0)
    for (cmd in w2) {
        val dir: Pair<Int, Int> = dirs[cmd[0]]!!
        val c = cmd.substring(1).toInt()
        val crosses = (0..c).toList().filter {x -> Pair(curr.first + dir.first*x, curr.second + dir.second*x) in grid}
        for (cr in crosses) {
            val currPos = Pair(curr.first + dir.first*cr, curr.second + dir.second*cr)
            val l = dist(Pair(0,0), currPos)
            val s = steps[currPos]!! + currSteps+cr
            if (l < closest) {
                closest = l
            }
            if (s < minSteps) {
                minSteps = s
            }

        }
        currSteps += c
        curr = Pair(curr.first + dir.first*c, curr.second + dir.second*c)
    }
    println("Closets $closest")
    println("MinSteps $minSteps")
}

fun solve2(data: List<List<String>>) {

}


fun main() {
    val data = File("2019/day3/input").useLines { it.toList() }
        .map { x -> x.split(',') }
    solve(data)
    solve2(data)

}