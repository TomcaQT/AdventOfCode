package day7

import intcode.IntcodeCumputer
import kotlin.math.max
import java.io.File

fun heapPermutation(a: IntArray, size: Int, n: Int, all: MutableList<IntArray>) {
    // if size becomes 1 then prints the obtained
    // permutation
    if (size == 1)
        all.add(a.copyOf())

    for (i in 0 until size) {
        heapPermutation(a, size - 1, n, all)


        // if size is odd, swap 0th i.e (first) and
        // (size-1)th i.e (last) element
        if (size % 2 == 1) {
            val temp = a[0]
            a[0] = a[size - 1]
            a[size - 1] = temp
        } else {
            val temp = a[i]
            a[i] = a[size - 1]
            a[size - 1] = temp
        }
    }
}

fun solve(data: MutableList<Int>) {
    var perms: MutableList<IntArray> = mutableListOf()
    heapPermutation(intArrayOf(0, 1, 2, 3, 4), 5,5, perms)
    var maxO = Int.MIN_VALUE
    var maxSeq = ""
    for (perm in perms) {
        var lastOutput = 0
        for (input in perm) {
            val computer = IntcodeCumputer(data.toMutableList(), mutableListOf(input, lastOutput))
            computer.run()
            lastOutput = computer.output
        }
        //print("Output: ${lastOutput}")
        if (lastOutput > maxO) {
            maxO = lastOutput
            maxSeq = perm.contentToString()
        }

    }
    println("MaxO: $maxO for seq: $maxSeq")

}

fun solve2(data: MutableList<Int>) {
    var perms: MutableList<IntArray> = mutableListOf()
    heapPermutation(intArrayOf(5,6,7,8,9), 5,5, perms)
    var maxO = Int.MIN_VALUE
    var maxSeq = ""
    for (perm in perms) {
        var computers: MutableList<IntcodeCumputer> = mutableListOf()
        perm.forEach { p -> computers.add(IntcodeCumputer(data.toMutableList(), mutableListOf(p))) }
        var lastOutput = 0
        while(computers.last().status != "END")
        {
            for (computer in computers) {
                computer.addInput(lastOutput)
                computer.run()
                lastOutput = computer.output
            }
        }



        //print("Output: ${lastOutput}")
        if (lastOutput > maxO) {
            maxO = lastOutput
            maxSeq = perm.contentToString()
        }

    }
    println("MaxO: $maxO for seq: $maxSeq")

}

fun main() {
    val data = File("2019/day7/input").useLines { it.toList() }[0].split(',')
        .map { x -> x.toInt()  }.toMutableList()


    //solve(data.toMutableList())
    solve2(data.toMutableList())
    //solve(data.toMutableList(),5 )
    //solve2(data)


}