class Instruc(object):
    def __init__(self, mnem, tipo, opfunc, num): 
        self._mnem = mnem
        self._tipo = tipo
        self._opfunc = opfunc
        self._num = num

class typeR(object):
    def __init__(self, op, rs, rt, rd, shamt, funct): 
        self._op = op
        self._rs = rs
        self._rt = rt
        self._rd = rd
        self._shamt = shamt
        self._funct = funct

class typeI(object):
    def __init__(self, op, rs, rt, imm): 
        self._op = op
        self._rs = rs
        self._rt = rt
        self._imm = imm

class typeJ(object):
    def __init__(self, op, addr): 
        self._op = op
        self._addr = addr