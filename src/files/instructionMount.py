class instrucAddress(object):
    def __init__(self, address, linha, label, typeIns): 
        self._address = address
        self._linha = linha
        self._label = label
        self._typeIns = typeIns

class InstructionAddress(object):
    address = [] 
    def appendAdress(self, addressN, linha, label, typeIns):
        self.address.append(instrucAddress(addressN, linha, label, typeIns))
        pass

    def labels(self, addressN):
        for addr in self.address:
            if addr._address == addressN and addr._label != "":
                return True
        return False    
        pass
    
    def haveLabel(self, addr):
        if addr._label != "":   return True
        else: return False 
        pass
    def getAddress(self, address):
        look = address
        for element in self.address:
            if look in element.addressN:
                return element.addressN
        pass
        
    def extractLabel(self, linha):
        pos = linha.find(":")
        if pos != -1:
            return linha[0:pos]
        else:
            return ""
        pass
    
    def extractLabel2(self, linha):
        pos = linha.find(":")
        if pos != -1:
            return linha[pos+1:]
        else:
            return ""
        pass
        
class instFull(object):
    def __init__(self, mnem, address, instruc, tipo): 
        self._mnem = mnem
        self._address = address
        self._instruc = instruc
        self._tipo = tipo

class InstructionFull(object):
    instrucFull = [] 
    def appendInstruc(self, mnem, address, instruction, typeIns):
        self.instrucFull.append(instFull(mnem, address, instruction, typeIns))
        pass

    def printAll(self, instrucFull, instructionFile):
        buffer = ""
        for instr in instrucFull:
            linha = ("| Address: " + instr._address + " | Mnem: " + format(instr._mnem, '4') + " | Tipo: " + instr._tipo + " | ")
            if instr._tipo == 'i':
                linha += ("Imm: " + instr._instruc._imm)
                linha +=  (" | op: " + instr._instruc._op)
                linha += (" | rs: " + instr._instruc._rs)
                linha += (" | rt: " + instr._instruc._rt)
            elif instr._tipo == 'j':
                linha += ("Target:  " + instr._instruc._addr)
                linha += (" | op: " + instr._instruc._op)
            elif instr._tipo == 'r':
                linha += ("funct: " + instr._instruc._funct)
                linha += (" | op: " + instr._instruc._op)
                linha += (" | rd: " + instr._instruc._rd)
                linha += (" | rs: " + instr._instruc._rs)
                linha += (" | shamt: " + instr._instruc._shamt)
            buffer += linha + "\n"
        buffer = buffer.rstrip('\n')
        outputfile = open(instructionFile, "w")
        outputfile.write(buffer)
        outputfile.close()