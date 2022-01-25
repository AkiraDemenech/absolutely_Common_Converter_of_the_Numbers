
from numpy import array
from muldiv import mmc,mdc,div, escreva,escrever,q

ast = "*"
mul = '·'


def mat (x = 4, y = None, e = lambda s='': eval(input(s)), t = array, r = None, v = 0):
	if y == None:
		y = x
	if r == None:
		r = []
	while len(r) < y:
		r.append([])
	j = 0
	while j < y:
		i = 0
		while len(r[j]) < x:
			r[j].append(v)
		while i < x:
			r[j][i] = e('[%d,%d] = '%(i+1,j+1))
			i += 1
		j += 1
	if type(r) != t:
		return t(r)
	return r

def dif (m, v = 0):
	c = 0
	while c < len(m):
		if m[c] != v:
			break
		c += 1
	return c

def somar (a, b, c = 1):	
	for x in range(min(len(a), len(b))):
		a[x] += c * b[x]				
	while len(a) < len(b): 				
		a.append(b[len(a)]*c)	
	return a	

def escalonar (m, t = array, v = print):
	escalonada = [list(n) for n in m]
	

	for ln in range(len(escalonada)): # para cada linha da matriz

		if ln < len(escalonada[ln]) and escalonada[ln][ln] == 0:
		#	se o elemento da diagonal, naquela linha, for 0

			for n in range(len(escalonada)): # busca uma linha em que o elemento da mesma coluna não for 0
				if ln < len(escalonada[n]) and escalonada[n][ln] != 0:
					escreva('\n\t','Somar linha',n,'na',ln)
					escreva(escalonada[ln], '+=', escalonada[n])
					somar(escalonada[ln], escalonada[n]) # e soma a linha encontrada na anterior					
					escreva(escalonada[ln])
					break

		for c in range(min(len(escalonada[ln]), ln)): # para cada coluna antes da diagonal principal 		

			if c < len(escalonada[c]) and escalonada[c][c] != 0 and escalonada[ln][c] != 0:
				f = escalonada[ln][c] / escalonada[c][c]
				if f.is_integer():
					f = int(f)
				escreva('\n\tSubtrair',f,'vezes a linha', c, 'em', ln)
				escreva(escalonada[ln], '-=', f, '*', escalonada[c])
				escreva(somar(escalonada[ln], escalonada[c], -f)) 

				





	return t(escalonada)

while __name__ == '__main__':
	try:
		res = input(q)
		try:
			res = eval(res)
		except SyntaxError:
			res = exec(res)
			if res != None:
				print('RES =', res)
		else:
			print('RES='+str(res))
	except KeyboardInterrupt:
		break
	except Exception as e:
		print('ERRO:',e)