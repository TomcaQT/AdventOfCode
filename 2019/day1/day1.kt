package day1

import java.io.File
import kotlin.math.*

fun calcFuel(x: Double): Double {
    return if (x > 6) floor(x/3) - 2 else 0.0
}

//divide by three, round down, and subtract 2.
fun solve(data: List<String>) {
    val sum =data.map {x -> floor(x.toDouble()/3) - 2}
            .reduce {x,y -> x + y}
    println("Part1: $sum")

}

fun solve2(data: List<String>) {
    var sum = 0.0
    for (i in 0..<data.count()) {
        var x = data[i].toDouble()
        while (x > 0) {
            x = calcFuel(x)
            sum += x
        }
    }
    println("Part2: $sum")
}


fun main() {
    val data = File("2019/data/1.in").useLines { it.toList() }
    solve(data)
    solve2(data)

}