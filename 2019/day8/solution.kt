package day8

import intcode.IntcodeCumputer
import java.io.File

fun layerInfo(layer: String): Pair<Int, Int> {
    var charMap: MutableMap<Char, Int> = mutableMapOf()
    layer.forEach { c -> if (charMap.contains(c)) charMap[c] = (charMap[c]!! + 1) else charMap[c] = 1 }
    return Pair(charMap.getOrDefault('0', Int.MAX_VALUE), charMap.getOrDefault('1', 0) * charMap.getOrDefault('2', 0))
}

fun solve(data: String, w: Int, l: Int) {
    val pixelInLayers = w * l
    val totalLayers = data.length / pixelInLayers

    var minZeros = Int.MAX_VALUE
    var minValue = -1
    for (i in 0..<totalLayers) {
        val layer = data.substring(pixelInLayers*i, pixelInLayers*i + pixelInLayers)
        val layerInfo = layerInfo(layer)
        //println("Layer ${i+1}: $layer -> $layerInfo")
        if (layerInfo.first < minZeros) {
            minZeros = layerInfo.first
            minValue = layerInfo.second
        }
    }
    println("Checksum: $minValue")
}

fun solve2(data: String, w: Int, l: Int) {
    val pixelInLayers = w * l
    val totalLayers = data.length / pixelInLayers
    var finalImage = data.substring(0, pixelInLayers)

    for (i in 1..<totalLayers) {
        val layer = data.substring(pixelInLayers*i, pixelInLayers*i + pixelInLayers)
        var newFinalImage = ""
        for (c in layer.indices) {
            newFinalImage += if (finalImage[c] == '2')
                layer[c]
            else
                finalImage[c]
        }
        finalImage = newFinalImage
    }

    //Print
    val totalRows = pixelInLayers / w
    finalImage = finalImage.replace('1', '#')
    finalImage = finalImage.replace('0', '.')
    (0..<totalRows).forEach {r -> println(finalImage.substring(w*r, w*r + w))}


}

fun main() {
    val data = File("2019/day8/input").useLines { it.toList() }[0]


    //solve("123456789012", 3,2)
    //solve(data.toMutableList())
    solve(data, 25, 6)
    solve2(data, 25, 6)
    //solve(data.toMutableList(),5 )
    //solve2("0222112222120000", 2, 2)


}