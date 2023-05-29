# DecisionTree ID3
Terceiro trabalho para a cadeira de Inteligência Artificial, FCUP-CC2006-2022/2023

Autores: [Francisco Ribeiro](https://github.com/franciscoribeiro2003), [Matheus Bissacot](https://github.com/MatheusBissacot) e [Sérgio Coelho](https://github.com/sergioccoelho).

Link do Github do projeto: [DecisionTree ID3](https://github.com/franciscoribeiro2003/DecisionTree-ID3)

## Requisitos
Para executar o programa é necessário ter instalado o [Python3](https://www.python.org/downloads/).

## Como executar
Para executar o programa, basta executar o seguinte comando:
```bash
python3 main.py
```
O programa irá pedir o nome do ficheiro *.csv* que contém os dados a serem analisados.

Para facilitar mais a como executar o programa, executa-se o seguinte comando:
```bash
python3 main.py -h
```
o que irá imprimir o seguinte:
```bash
usage: main.py [-h] [-d DATA] [-p]

Decision Trees ID3, please use the following arguments

options:
  -h, --help            show this help message and exit
  -d DATA, --Data DATA  Data to analyze from .csv table.
  -p, --print           Print the tree.
```
Ou seja, para imprimir a ajuda do programa corre-se o seguinte comando:
```bash
$ python3 main.py -d ficheiro.csv -p
```
