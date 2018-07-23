from files.instructionType import *

class Instruction(object):
    instructions = [Instruc("nop", 'r', 0, 0), Instruc("add", 'r', 32,3), Instruc("addi", 'i', 8, 3),
            Instruc("sub", 'r', 34, 3), Instruc("sll", 'r', 0, 3), Instruc("srl", 'r', 2, 3), Instruc("lui", 'i', 15, 2),
            Instruc("and", 'r', 36, 3), Instruc("andi", 'i', 12, 3), Instruc("or", 'r', 21, 3), Instruc("ori", 'i', 13, 3),
            Instruc("xor", 'r', 38, 3), Instruc("xori", 'i', 14, 3), Instruc("slt", 'r', 42, 3), Instruc("slti", 'i', 10, 3),
            Instruc("beq", 'i', 4, 3), Instruc("bne", 'i', 5, 3), Instruc("mul", 'r', 24, 3), Instruc("div", 'r', 26, 3),
            Instruc("j", 'j', 2, 1), Instruc("jal", 'j', 3, 1), Instruc("jr", 'r', 8, 1), Instruc("lw", 'i', 35, 2),
            Instruc("sw", 'i', 43, 2)]
    
    def getOpcode(self, mnem):
        look = mnem
        for instr in self.instructions:
            if look in instr._mnem:
                return instr._opfunc
        pass

    def getObjectbyMnem(self, mnem):
        look = mnem
        for instr in self.instructions:
            if look in instr._mnem:
                return instr
        pass

    def getType(self, mnem):
        look = mnem
        for instr in self.instructions:
            if look in instr._mnem:
                return instr._tipo
        pass