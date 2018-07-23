# Python Assembler

Converts an Assembly code to Machine code following the especificacaoMontador.pdf schematics.

FEDERAL UNIVERSITY OF SÃO FRANCISCO VALLEY - UNIVASF

MAX SANTANA

## Getting Started

First of all, open Command Line in \Assembler folder and then type:

**WITHOUT QUOTES**

```
.\Assembler "INPUT_FILE_NAME.asm" "OUTPUT_FILE_NAME.mif"
```

for example:

```
.\Assembler EXAMPLE.asm memoria.mif
```

Typing without output file name also works:

```
.\Assembler "INPUT_FILE_NAME.asm"
```
In this case, a file named "Memoria.mif" will be created

2 Aux files will be created. "ArquivoLimpoTemp.txt" and "instrucoes.txt"

    -- ArquivoLimpoTemp.txt stores the clean assembly code (without the comments, \n and spaces)

    -- instrucoes.txt stores a general info of all the instructions, such as memory address and immediate. 

## Authors

* **Jonas dos Santos** - [JonasCassiano](https://github.com/jonascassiano)
* **Matheus dos Anjos** - [MatanjosM](https://github.com)

## License

NON-COMMERCIAL 



