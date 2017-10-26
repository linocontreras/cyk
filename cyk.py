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
            
    noterminales = set()
    terminales = set()
    for key in gramatica:
        noterminales.add(key)
        for v in gramatica[key]:
            if(all(c.islower() for c in v)):
                terminales.add(v)
    
    producciones = []
    for key in gramatica:
        for p in gramatica[key]:
            if p in terminales:
            	producciones.append((key, [p])) 
            else:
                tmp = tuple(x for x in p)
                producciones.append((key, tmp))
    
    for cadena in cadenas:
        if cyk(terminales,noterminales,producciones,'A',cadena):
            print("Accepted")
        else:
            print("Rejected")
            
    
def cyk(terminales,noterminales,producciones,inicio,cadena):
	matriz=dict()
	n=len(cadena)
	for i in range(1,n+1):
		for j in range(1,n+1):
			for k in noterminales:
				matriz[(i,j,k)]=False
	for i in range(1,n+1):
		for produccion in producciones:
			if len(produccion[1])==1:
				if produccion[1][0]==cadena[i-1]:
					matriz[(i,1,produccion[0])]=True
	for i in range(2,n+1):
		for j in range(1,n-i+2):
			for k in range(1,i):
				for produccion in producciones:
					if len(produccion[1])==2:
						if matriz[(j,k,produccion[1][0])] and matriz[(j+k,i-k,produccion[1][1])]:
							matriz[(j,i,produccion[0])]=True
							
	return matriz[(1,n,inicio)]
	
main()