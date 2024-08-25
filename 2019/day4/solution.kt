package day4



var passwords: MutableSet<String> = mutableSetOf()
//divide by three, round down, and subtract 2.
fun rec(passwd: String) {
    if (passwd.length > 6) {
        return
    }
    if (check(passwd)) {
        passwords.add(passwd)
        return
    }
    val lastNumber = passwd.last().toString().toInt()
    (lastNumber..9).forEach {x -> rec(passwd + "$x")}
}

fun check(passwd: String): Boolean {
    var hasDouble = false
    if (passwd.length != 6) return false

    var prev = passwd.slice(0..0).toInt()
    for (c in passwd.slice(1..<passwd.length)) {
        val value = c.toString().toInt()
        if (value < prev)
            return false
        if (value == prev)
            hasDouble = true
        prev = value
    }
    return hasDouble
}

fun solve(from: Int, to: Int) {

    (0..9).forEach {x -> rec("$x") }
    val x = passwords.filter { x -> x.toInt() in (from + 1)..<to }
    println("total passwords: ${x.count()}")

    val x2 = x.filter { p -> check2(p) }
    println("total passwords2: ${x2.count()}")
}

fun check2(passwd: String): Boolean {
    var doubleLen = 1
    var prev = passwd[0]
    for (c in passwd.slice(1..<passwd.length)) {
        if (c == prev) {
            doubleLen++
        }
        else {
            if (doubleLen == 2) return true
            doubleLen = 1
        }
        prev = c
    }
    return if (doubleLen == 2) return true else false
}



fun main() {
    solve(from=245318, to=765747)
    //solve2(data)
    println(check2("111122"))

}