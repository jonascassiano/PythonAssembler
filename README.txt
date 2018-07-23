# Python Assembler

UNIVERSIDADE FEDERAL DO VALE DO SÃO FRANCISCO - UNIVASF

Dr. MAX SANTANA

## Iniciando

Primeiramente, Abra uma janela do CMD na pasta \PythonAssembler e digite:

**Sem aspas**

```
.\Assembler "INPUT_FILE_NAME.asm" "OUTPUT_FILE_NAME.mif"
```

Por exemplo:

```
.\Assembler EXAMPLE.asm memoria.mif
```

Digitando sem o nome do arquivo de saida também funciona:

```
.\Assembler "INPUT_FILE_NAME.asm"
```
Nesse caso, um arquivo com o nome "Memoria.mif" vai ser criado.

2 arquivos auxiliares também serão gerados, como o "ArquivoLimpoTemp.txt" e o "instrucoes.txt"

    -- ArquivoLimpoTemp.txt armazena o código em assembly sem os comentarios, "\n" e espaços.

    -- instrucoes.txt ele armazena a informação de todas as instruções, como endereço de memória, imm, 
    mnemonicos e etc. 


## Autores

* **Jonas dos Santos** - [JonasCassiano](https://github.com/jonascassiano)
* **Matheus dos Anjos** - [MatanjosM](https://github.com)

## Licença

NÃO-COMERCIAL



