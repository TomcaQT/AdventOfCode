package intcode

class IntcodeCumputer(var memory: MutableList<Int>, val inputs :MutableList<Int>, val verbose: Boolean = false) {
    var currentPosition: Int = 0
    var lastOp = ""
    var output: Int = Int.MIN_VALUE
    var currentInput: Int = 0
    var status = ""
    var currentOffset: Int = 0

    fun dump() = println(memory)

    fun get(position: Int): Int = memory[position]

    fun getFromAddr(position: Int, parameterMode: Int = 0): Int {
      return if (parameterMode == 1) memory[position] else memory[memory[position]]
    }

    fun set(position: Int, value: Int) {memory[position] = value}

    fun setFromAddr(position: Int, value: Int) {memory[memory[position]] = value}

    fun addInput(input: Int) {inputs.add(input)}

    fun run() {

        while (true) {

            val parsed = parse_insruction(memory[currentPosition].toString())
            val ins = parsed.first; val modes = parsed.second
            if (ins == "99") {
                status = "END"
                break
            }

            if (verbose)
                println("OP: $ins -> with modes: $modes")
            val step = when(ins) {
                "01" -> ins1(modes)
                "02" -> ins2(modes)
                "03" -> ins3(modes)
                "04" -> ins4(modes)
                "05" -> ins5(modes)
                "06" -> ins6(modes)
                "07" -> ins7(modes)
                "08" -> ins8(modes)
                "09" -> ins9(modes)
                else -> ins1(modes)
            }

            currentPosition += step
            if (ins == "04")
                break

            if (verbose)
                println("Moving +$step steps with")
        }
    }

    fun parse_insruction(opcode: String): Pair<String, String> {
        val opcodeFull = opcode.padStart(5, '0')
        val opcodeLen = opcodeFull.length
        val ins = opcodeFull.slice(opcodeLen-2..<opcodeLen)
        val modes = opcodeFull.slice(0..<opcodeLen-2).reversed()
        return Pair(ins, modes)
    }

    fun ins1(modes: String): Int{
        val value = getFromAddr(currentPosition+1, modes[0].digitToInt()) + getFromAddr(currentPosition+2, modes[1].digitToInt())
        setFromAddr(currentPosition+3, value)
        return 4
    }

    fun ins2(modes: String): Int {
        val value = getFromAddr(currentPosition+1, modes[0].digitToInt())  * getFromAddr(currentPosition+2, modes[1].digitToInt())
        setFromAddr(currentPosition+3, value)
        return 4
    }


    fun ins3(modes: String): Int {
        val value = inputs[currentInput]
        setFromAddr(currentPosition+1, value)
        currentInput++
        return 2
    }

    fun ins4(modes: String): Int {
        val value = getFromAddr(currentPosition+1, modes[0].digitToInt())
        if (verbose)
            println("Ins4 $value")
        output = value
        return 2
    }

    fun ins5(modes: String): Int {
        val toCheck = getFromAddr(currentPosition+1, modes[0].digitToInt())
        val jump = getFromAddr(currentPosition+2, modes[1].digitToInt())
        if (toCheck != 0) {
            currentPosition = jump
            return 0
        }
        return 3
    }

    fun ins6(modes: String): Int {
        val toCheck = getFromAddr(currentPosition+1, modes[0].digitToInt())
        val jump = getFromAddr(currentPosition+2, modes[1].digitToInt())
        if (toCheck == 0) {
            currentPosition = jump
            return 0
        }
        return 3
    }

    fun ins7(modes: String): Int {
        val toCheck1 = getFromAddr(currentPosition+1, modes[0].digitToInt())
        val toCheck2 = getFromAddr(currentPosition+2, modes[1].digitToInt())

        if (toCheck1 < toCheck2) {
            setFromAddr(currentPosition+3, 1)
        }
        else
            setFromAddr(currentPosition+3, 0)
        return 4
    }

    fun ins8(modes: String): Int {
        val toCheck1 = getFromAddr(currentPosition+1, modes[0].digitToInt())
        val toCheck2 = getFromAddr(currentPosition+2, modes[1].digitToInt())

        if (toCheck1 == toCheck2) {
            setFromAddr(currentPosition+3, 1)
        }
        else
            setFromAddr(currentPosition+3, 0)
        return 4
    }

    fun ins9(modes: String): Int {
        val value = getFromAddr(currentPosition+1, modes[0].digitToInt())
        currentOffset += value
        return 2
    }
}