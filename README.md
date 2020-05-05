# Python Assembler

Converts an Assembly code to Machine code following the especificacaoMontador.pdf schematics.

FEDERAL UNIVERSITY OF SÃO FRANCISCO VALLEY - UNIVASF

MAX SANTANA

## Getting Started  

First of all, open Command Line in \Assembler folder and then type:

**WITHOUT QUOTES**

Windows:
```
.\Assembler "INPUT_FILE_NAME.asm" "OUTPUT_FILE_NAME.mif"
```

Linux:
```
python assembler.py "INPUT_FILE_NAME.asm" "OUTPUT_FILE_NAME.mif"
```

for example:

```
python assembler.py EXAMPLE.asm memory.mif
```

Running the code without the output filename also works:

```
python assembler.py EXAMPLE.asm
```

In this case, a file named "Memoria.mif" will be created

2 more files will be generated automatically. "ArquivoLimpoTemp.txt" and "instrucoes.txt"

    -- ArquivoLimpoTemp.txt stores the clean assembly code (without the comments, \n and spaces)

    -- instrucoes.txt stores a general info of all the instructions, such as memory address and immediate. 

## Screenshots

<img src="https://github.com/jonascsantos/PythonAssembler/blob/master/src/files/UI/1.png" alt="Home" width="400"/> 

<img src="https://github.com/jonascsantos/PythonAssembler/blob/master/src/files/UI/2.png" alt="Home" width="800"/> 

## Authors

* **Jonas dos Santos** - [Jonascsantos](https://github.com/jonascsantos)
* **Matheus dos Anjos** - [MatanjosM](https://github.com)

## License

GNU



