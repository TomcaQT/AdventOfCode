package day2

import java.io.File


//divide by three, round down, and subtract 2.
fun solve(data: MutableList<Int>, x1: Int, x2: Int): Int {

    data[1] = x1; data[2] = x2

    var pos = 0
    var curr = data[pos]
    while (curr != 99) {
        val op = curr
        val i1 = data[data[pos+1]]; val i2 = data[data[pos+2]]
        val res = if (op == 1) i1 + i2 else i1 * i2
        data[data[pos+3]] = res
        //println("Position $pos with op: $curr -> $i1 +* $i2 = $res")
        pos += 4
        curr = data[pos]
        //println("Moving to $pos with op $curr")

    }
    println("Result ${data[0]}")
    return data[0]
}

fun solve2(data: MutableList<Int>) {
    for (i in 0..99) {
        for (j in 0..99) {

            if (solve(data.toMutableList(), i, j) == 19690720) {
                println("What is 100 * noun + verb = ${100 * i + j}")
                return
            }
        }
    }
}


fun main() {
    val data = File("2019/day2/2.in").useLines { it.toList() }[0].split(',')
        .map { x -> x.toInt()  }.toMutableList()
    solve(data.toMutableList(), 12, 2)
    solve2(data)

}