# Investigación:
# https://docs.google.com/a/itesm.mx/document/d/15gC2sLom1BWTUWHxANNiOitrXRAFweyLSq9qP_1RGdI/edit?usp=sharing

def main():
    
    gramatica = {}
    
    # Leer número de producciones
    n = int(input())
    
    #Leer producciones
    for i in range(0,n):
        
        #Lee cada producción.
        tmp = input()
        
        #Separa terminales de no terminales.
        noterminal, tmp = tmp.split('-')
        producciones = tmp.split(',')
        
        #Agrega al diccionario usando noterminal como llave y asignándole un set de producciones.
        gramatica[noterminal] = frozenset(producciones)
    
    cadena = input()
    
    cadenalen = len(cadena)
    mat = []
    for i in range(0,cadenalen):
        mat.append([])
        for k,v in gramatica.items():
            if cadena[i] in v:
                mat[i].append(k)
    
    print(mat)
main()

