package day6

import java.io.File
import kotlin.io.path.Path

fun calcOrbits(planet: String, orbits: MutableMap<String, String>): Int {
    if (!orbits.containsKey(planet))
        return 0
    val prev = orbits[planet]!!
    return 1 + calcOrbits(prev, orbits)
}

fun getPath(planet: String, orbits: MutableMap<String, String>): MutableList<String> {
    var path: MutableList<String> = mutableListOf()
    var curr = planet
    while (orbits.containsKey(curr)) {
        path.add(orbits[curr]!!)
        curr = orbits[curr]!!
    }
    return path
}

fun solve(data: MutableList<String>) {
    var orbits: MutableMap<String, String> = mutableMapOf()
    var planets: MutableSet<String> = mutableSetOf()

    for (rec in data) {
        val p = rec.split(')')
        val p1 = p[0]; val p2 = p[1]
        orbits[p2] = p1
        planets.add(p1)
        planets.add(p2)
    }

    val sum = planets.fold(0) {sum, p -> sum + calcOrbits(p, orbits) }
    println("Total orbits: $sum")

    val pathYou = getPath("YOU", orbits)
    val pathSan = getPath("SAN", orbits)

    for (p in pathYou.toMutableList()) {
        if (p in pathSan) {
            pathYou.remove(p)
            pathSan.remove(p)
        }
    }
    println("Total orbital transfers: ${pathYou.count() + pathSan.count()}")
}

fun main() {
    val data = File("2019/day6/input").useLines { it.toList() }
    solve(data.toMutableList())

    //solve2(data)


}