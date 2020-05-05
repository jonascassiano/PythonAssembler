# -*- coding: utf-8 -*-

import os
import os.path
import sys
import os.path
import operator

from files.instructionType import *  #Importa os outros arquivos
from files.instructionMount import *
from files.regs import *
from files.mnems import *

class Montador(object):
    finalFile = ""
    instrucFull = []
    def lastLinha(self, nomeArquivo):
        file = open(nomeArquivo, "r")
        lineList = file.readlines()
        finalFile = lineList[-1]
        file.close()
        return finalFile
        pass

    def limp(self, nomeArquivo, targetFile):
        buffer = ""  #var q armazena as linhas limpas
        quebraLinha = ""
        global finalFile
        if os.path.exists(nomeArquivo):
            file = open(nomeArquivo, "r")
            finalFile = self.lastLinha(nomeArquivo)
            for linha in file:                     
                codigoExiste = True # linha possui codigo executavel 
                commentPos = linha.find("#")  # verifica se linha possui comentario
                if commentPos == 0: codigoExiste = False  # se achou o Hashtag no começo da linha entao n tem cod executavel
                elif commentPos > 0:              # se achou o Hashtag no meio entao tem codigo executavel ate commentpos -1.
                    tmp = linha[0:commentPos-1]
                    tmp = tmp.strip()        # .strip remove tudo q eh desnecessario no comeco e no final da linha. remove os espacos e tabs
                    if tmp == "":
                        codigoExiste = False
                    else:
                        linha = tmp
                        
                tmp = linha.strip(" ")
                tmp = tmp.strip("\t")         
                tmp = tmp.strip("\n")
               
                if tmp == "": codigoExiste = False  # verifica se linha ta vazia
       
                linha = tmp

                labelPos = 0
                labelPos = linha.find(":") 
                if labelPos != -1:
                    if len(linha.strip()) == labelPos+1 and linha.strip() != finalFile.strip():
                        quebraLinha = linha
                        continue
                if codigoExiste:
                    if quebraLinha != "":
                        quebraLinha += linha
                        buffer += quebraLinha + "\n"
                        quebraLinha = ""
                    else:
                        buffer += linha + "\n"  # escreve a linha no buffer

            buffer = buffer.rstrip('\n')          
                
            # escreve o arquivo final em outro .asm
            outputfile = open(targetFile, "w")
            outputfile.write(buffer)
            outputfile.close()
               
        else: # if file not found
            raise IOError(0, nomeArquivo, "Arquivo '"+nomeArquivo+"' nao foi encontrado.")
        pass    

    def address(self, nomeArquivo):
        contLinhas = 0
        if os.path.exists(nomeArquivo):
            file = open(nomeArquivo, "r")
            addrs = InstructionAddress()
            for linha in file:
                hexa = format(contLinhas * 4, '#05X')
                addrs.appendAdress(hexa,linha,addrs.extractLabel(linha),"")
                contLinhas = contLinhas + 1
            return addrs
            file.close()                       
        else: # if file not found
            raise IOError(0, nomeArquivo, "Arquivo '"+nomeArquivo+"' nao foi encontrado.")
        pass

    def operacaoR(self, mnemObj, linhaVector):
        regBank = Regs()
        op, rs, rt, rd, shamt, funct = 0,0,0,0,0,0
        if mnemObj._mnem == "sll" or  mnemObj._mnem == "srl": #
            rd = regBank.searchReg(linhaVector[0])
            rt = regBank.searchReg(linhaVector[1])
            shamt = int(linhaVector[2])
        elif mnemObj._mnem == "jr": 
            rs = regBank.searchReg(linhaVector[0])
        else: 
            rd = regBank.searchReg(linhaVector[0])
            rs = regBank.searchReg(linhaVector[1])
            rt = regBank.searchReg(linhaVector[2])
        funct = mnemObj._opfunc        
        op = bin(op)[2:].zfill(6)
        rs = bin(rs)[2:].zfill(5)
        rt = bin(rt)[2:].zfill(5)
        rd = bin(rd)[2:].zfill(5)
        shamt = bin(shamt)[2:].zfill(5)
        funct = bin(funct)[2:].zfill(6)

        instrucao = typeR(op, rs, rt, rd, shamt, funct)
        return instrucao
        pass

    def operacaoI(self, currentAddr,mnemObj, linhaVector):
        regBank = Regs()
        op, rs, rt, imm = 0,0,0,0
        if mnemObj._mnem == "sw": 
            rt = regBank.searchReg(linhaVector[0])
            posBegin = linhaVector[1].find('(')
            posEnd = linhaVector[1].find(')')
            imm = linhaVector[1][0:posBegin]
            if imm != '':
                imm = bin(int(imm,10))[2:].zfill(16)
            else:
                imm = bin(0)[2:].zfill(16)
            rs = regBank.searchReg(linhaVector[1][posBegin+1:posEnd])
        elif mnemObj._mnem == "lw":
            rs = regBank.searchReg(linhaVector[0])
            posBegin = linhaVector[1].find('(')
            posEnd = linhaVector[1].find(')')
            imm = linhaVector[1][0:posBegin]
            if imm != '':
                if imm.find("x") == -1 :
                    imm = bin(int(imm,10))[2:].zfill(16)
                else: 
                    imm = bin(int(imm,16))[2:].zfill(16)
            else:
                imm = bin(0)[2:].zfill(16)
            rt = regBank.searchReg(linhaVector[1][posBegin+1:posEnd])
        elif mnemObj._mnem == "bne" or  mnemObj._mnem == "beq": 
            imm = self.offsetCalc(currentAddr,linhaVector[2])
            rs = regBank.searchReg(linhaVector[0])
            rt = regBank.searchReg(linhaVector[1])
        elif mnemObj._mnem == "lui" : 
            imm = bin(int(linhaVector[1], 16))[2:].zfill(16)
            rs = 0
            rt = regBank.searchReg(linhaVector[0])
        else: 
            rt = regBank.searchReg(linhaVector[0])
            rs = regBank.searchReg(linhaVector[1])
            if int(linhaVector[2]) < 0:
                imm = self.bindigits(int(linhaVector[2]),16) 
            else:
                imm = bin(int(linhaVector[2],10))[2:].zfill(16)
        op = mnemObj._opfunc 
        
        op = bin(op)[2:].zfill(6)
        rs = bin(rs)[2:].zfill(5)
        rt = bin(rt)[2:].zfill(5)
        
        
        instrucao = typeI(op, rs, rt, imm)
        return instrucao
        pass
    
    def offsetCalc(self,addrS,addrD):
        op1 = int(addrS, 16) + 0x4
        op2 = int(addrD, 16) - op1
        op3 = int(op2/4)
        op3 = bin(op3)
        return self.bindigits(int(op3,2),16)  #retorna complemento de 2


    def bindigits(self, n, bits):
        s = bin(n & int("1"*bits, 2))[2:]
        return ("{0:0>%s}" % (bits)).format(s)

    def operacaoJ(self, mnemObj, linhaVector):
        regBank = Regs()
        op, addr = 0,0
        op = mnemObj._opfunc        
        addr = bin(int(linhaVector[0], 16))[2:].zfill(32)
        op = bin(op)[2:].zfill(6)
        instrucao = typeJ(op, addr)
        return instrucao
        pass
         
    def attrbType(self, instrVec, targetFile):
        mnemVector = Instruction()
        instrVector = InstructionFull()
        buffer = ""
        for addr in instrVec.address:
            if instrVec.haveLabel(addr):
                linha = instrVec.extractLabel2(addr._linha)
                addr._linha = linha.strip()
            else:
                addr._linha = addr._linha.strip()

            pos = addr._linha.find(" ")
            mnem = addr._linha[0:pos]
            addr._linha = addr._linha[pos+1:]
            mnemObj = mnemVector.getObjectbyMnem(mnem)
            addr._linha = [x.strip() for x in addr._linha.split(',')]
            for i in range(mnemObj._num):
                if addr._linha[i].find("$") == -1:
                    for busca in instrVec.address:
                        if busca._label == addr._linha[i]:
                            addr._linha[i] = busca._address
            if(mnemObj._mnem == "nop"):
                break
            if mnemObj._tipo == 'r':
                instrucao = self.operacaoR(mnemObj,addr._linha)
                instrVector.appendInstruc(mnemObj._mnem, addr._address ,instrucao,'r')
                op = instrucao._op
                rs = instrucao._rs
                rt = instrucao._rt
                rd =instrucao._rd
                shamt = instrucao._shamt
                funct = instrucao._funct
                instr0 = shamt[3:] + funct
                instr0Hex = (format(int(instr0,2), '#04X'))
                instr1 = rd + shamt[0:3]
                instr1Hex = (format(int(instr1,2), '#04X'))
                instr2 = rs[2:] + rt
                instr2Hex = (format(int(instr2,2), '#04X'))
                instr3 = op + rs[0:2]
                instr3Hex = (format(int(instr3,2), '#04X'))
               
            elif mnemObj._tipo == 'i':
                instrucao = self.operacaoI(addr._address,mnemObj,addr._linha)
                instrVector.appendInstruc(mnemObj._mnem, addr._address ,instrucao,'i')
                op = instrucao._op
                rs = instrucao._rs
                imm = instrucao._imm
                rt = instrucao._rt
                instr0 = imm[8:]
                instr0Hex = (format(int(instr0,2), '#04X'))
                instr1 = imm[0:8] 
                instr1Hex = (format(int(instr1,2), '#04X'))
                instr2 = rs[2:5] + rt
                instr2Hex = (format(int(instr2,2), '#04X'))
                instr3 = op + rs[0:2]
                instr3Hex = (format(int(instr3,2), '#04X'))
                
            elif mnemObj._tipo == 'j':
                instrucao = self.operacaoJ(mnemObj,addr._linha)
                instrVector.appendInstruc(mnemObj._mnem, addr._address ,instrucao,'j')
                cropAddr = instrucao._addr[4:30]
                op = instrucao._op
                instr0 = cropAddr[18:26] 
                instr0Hex = (format(int(instr0,2), '#04X'))
                instr1 = cropAddr[10:18]
                instr1Hex = (format(int(instr1,2), '#04X'))
                instr2 = cropAddr[2:10]
                instr2Hex = (format(int(instr2,2), '#04X'))
                instr3 = op + cropAddr[0:2]
                instr3Hex = (format(int(instr3,2), '#04X'))
            
            addr0 = int(addr._address 	, 16 )
            addr1 = addr0 + 1
            addr2 = addr0 + 2
            addr3 = addr0 + 3
            linha0 = (format(addr0 , '#05X') + " " + instr0Hex)
            linha1 = (format(addr1 , '#05X') + " " + instr1Hex)
            linha2 = (format(addr2 , '#05X') + " " + instr2Hex)
            linha3 = (format(addr3 , '#05X') + " " + instr3Hex)
            buffer += linha0 + "\n"  # escreve a linha no buffer
            buffer += linha1 + "\n"  # escreve a linha no buffer
            buffer += linha2 + "\n"  # escreve a linha no buffer
            buffer += linha3 + "\n"  # escreve a linha no buffer
        
        buffer = buffer.rstrip('\n')
        outputfile = open(targetFile, "w")
        outputfile.write(buffer)
        outputfile.close()

        return instrVector
   
if __name__ == "__main__":
    args = len(sys.argv)
    if args == 1:
        print("Informe o arquivo de entrada! ")
        sys.exit()
    elif args == 3:
        targetFile = str(sys.argv[2])
    elif args == 2:
        targetFile = "memoria.mif"
    else:
        print("Argumentos demais! ")
        sys.exit()

    passo1 = Montador() 
    passo1.limp(str(sys.argv[1]), "ArquivoLimpoTemp.txt")
    passo2 = passo1.address("ArquivoLimpoTemp.txt")
    instrucoes = passo1.attrbType(passo2 , targetFile)
    instrucoes.printAll(instrucoes.instrucFull, "instrucoes.txt")
    print("Arquivos Criados com Sucesso!")
