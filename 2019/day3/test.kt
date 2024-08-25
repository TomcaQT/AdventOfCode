fun main() {
    var m: MutableMap<Int, Int> = mutableMapOf()
    m.put(1,1)
    if (1 in m.keys) {} else m.put(1,2)
    print(m)
}