from Controlador.Controlador import Controlador
controlador = Controlador()

def Convert(string): 
    list1=[] 
    list1[:0]=string 
    return list1 

def block(converted):
	block = converted
	x = 0
	e = 0
	while e < len(converted):
		e = pow(2,x)
		x = x + 1
		if e < len(converted):
			block.insert(e-1,'N')
	return block

def get_exp(trama):
	e = 0
	x = 0
	fps = []
	while e < len(trama):
		e = pow(2,x)
		x = x + 1
		fps.append(e)

	if e > len(trama):
		return fps[:-1]
	else:
		return fps

def ranges(lon,step):	
	mask = []
	for x in range(0,lon,step):
		for y in range(step):
			mask.append('-')
			if len(mask) == lon:
				return mask
		if x == 0:
			mask = mask[1:]
		for y in range(step):
			mask.append('v')
			if len(mask) == lon:
				return mask
	return mask

def fpN(mask,values):
	fpn = mask
	for x in range(len(mask)):
		if mask[x] == 'v':
			fpn[x] = values[x]
	return fpn

def paridad(fpN):
	i = 0
	for x in range(len(fpN)):
		if fpN[x] == '1':
			i = i + 1
	
	for x in range(len(fpN)):
		if fpN[x] == 'N':
			if i%2 == 0:
				fpN[x] = '0'
			else:
				fpN[x] = '1'

	return fpN

def fpFinal(binario):
	converted = Convert(binario)
	exp_inserted = block(converted)
	exp = get_exp(exp_inserted)
	matriz = []

	for x in exp:
		mask = ranges(len(exp_inserted),x)
		fpX = fpN(mask,exp_inserted)
		fpXfinal = paridad(fpX)
		matriz.append(fpXfinal)

	trama_final = []
	for x in range(len(mask)):
		for y in range(0,len(exp)):
			if matriz[y][x] != '-':
				trama_final.append(matriz[y][x])
				break

	matriz.append(trama_final)
	controlador.setFPs(matriz)
	print(controlador.getFPs())
	print(''.join(trama_final))
	controlador.setTrama(''.join(trama_final))
	return matriz
		

def verify(trama):
	converted = Convert(trama)
	exp = get_exp(converted)
	matriz = []

	for x in exp:
		mask = ranges(len(converted),x)
		fpX = fpN(mask,converted)
		fpXfinal = paridad(fpX)
		matriz.append(fpXfinal)

	check = []
	for x in range(len(exp)):
		suma = 0
		for y in range(len(mask)):
			if matriz[x][y] == '1':
				suma = suma + 1
		if suma%2 == 0:
			check.append(0)
		else:
			check.append(1)
	print(check)
	controlador.setCheck(check[::-1])
	return check
