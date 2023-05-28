from argparse import ArgumentParser
from sys import argv, exit
import csv
from tree import ID3, print_decision_tree


def main():
    parser = ArgumentParser(description='Decision Trees ID3, please use the following arguments')

    parser.add_argument('-d', '--Data', type=str, help='Data to analyze from .csv table.')
    parser.add_argument('-p', '--print', action='store_true', help='Print the tree.')

    args = parser.parse_args()

    if len(argv) == 1:
        parser.print_help()
        exit(0)
    
    with open(args.Data ,'rt') as fd:

        dataBuffer= csv.reader(fd) # read a pointer example: <_csv.reader object at 0x7f2779bb9460>
        firstRow = dataBuffer.__next__() # reads the titles of the csv table in string: ['Title1','title2','title3',...]

        data=[]  # Stores by line the atributions. Example: [[arg1, arg2, arg3, ...], [arg1, arg2, arg3, ...], ...] 
        for i in dataBuffer:
            data.append(i)

        atributos = {}  # for each title associate a index dict(str,int): {'title1':0, 'title2':1, 'title3':2, ...}

        for i in range(len(firstRow)):
            atributos[firstRow[i]] = i

        classe = firstRow[-1]
        fd.close()

    arvore = ID3(data, atributos, classe)

    if args.print:
        print_decision_tree(arvore)


if __name__ == '__main__':
    main()