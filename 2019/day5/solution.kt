package day5

import java.io.File
import intcode.IntcodeCumputer

fun solve(data: MutableList<Int>, input: Int) {
    val computer = IntcodeCumputer(data, mutableListOf(input))
    computer.run()
    computer.dump()
    print("Output: ${computer.output}")
}

fun main() {
    val data = File("2019/day5/input").useLines { it.toList() }[0].split(',')
        .map { x -> x.toInt()  }.toMutableList()
    solve(data.toMutableList(),1)
    solve(data.toMutableList(),5 )
    //solve2(data)


}