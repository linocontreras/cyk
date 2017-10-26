import fileinput

def main():
    
    gramatica = {}

    lines = []
    cadenas = []
    
    for line in fileinput.input():
       lines.append(line)
    
    #Lee cada producción.
    for i,line in enumerate(lines):
        tmp = line.rstrip().split(' ')
        size = len(tmp)
        if(size > 1):
            gramatica[tmp[0]] = tmp[1:]
        else:
            cadenas.append(line.rstrip())
            
    print(gramatica)
    print(cadenas)
    
    for cadena in cadenas:
        matriz = []
        for i,letter in enumerate(cadena):
            arr = []
            for key in gramatica:
                if letter in gramatica[key]:
                    arr.append(key)
            matriz.append(arr)
        print(matriz)
    
    

main()

