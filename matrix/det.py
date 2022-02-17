
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
			try:
				r[j][i] = e('[%d,%d] = '%(j,i))
				i += 1
			except Exception:	
				continue
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

def determinante (x):

	det = True
	d = escalonar(x)

	for i in range(len(d)):
		if i < len(d[i]):
			det *= d[i][i]
		#	print(det,d[i][i])
		else:	
			return False 
	return det		
det = determinante	
def inteiro (f):
	try:
		if f.is_integer():
			return int(f)
	except AttributeError:		
		pass
	return f	

def somar (a, b, c = 1):	
	for x in range(min(len(a), len(b))):
		a[x] += inteiro(c * b[x])				
		
	while len(a) < len(b): 				
		a.append(inteiro(b[len(a)] * c))	
	return a	

def eliminar (m,a,b,c): 	
	f = inteiro(m[a][c] / m[b][c])					
	escreva(q + 'Subtrair',f,'vezes a linha', b, 'em', a)
	escreva(m[a], '-=', f, '*', m[b])
	escreva(somar(m[a], m[b], -f), '\n') 

def escalonar (m, diag = False):
	escalonada = [list(n) for n in m]
	
	
	for ln in range(len(escalonada)): # para cada linha da matriz

		while ln < len(escalonada[ln]) and escalonada[ln][ln] == 0:
		#	enquanto o elemento da diagonal, naquela linha, for 0

			n = len(escalonada)
			while n > 0: # busca uma linha em que o elemento da mesma coluna não for 0
				n -= 1
				if ln < len(escalonada[n]) and escalonada[n][ln] != 0:
					escreva(q,'Somar linha',n,'na',ln)
					escreva(escalonada[ln], '+=', escalonada[n])
					somar(escalonada[ln], escalonada[n]) # e soma a linha encontrada na anterior					
					escreva(escalonada[ln], '\n')
					break
			else: # se não encontrar nenhum 	
				break

			for c in range(ln): # para cada coluna antes da diagonal principal 		

				if c < len(escalonada[c]) and escalonada[c][c] != 0 and escalonada[ln][c] != 0:
					eliminar(escalonada,ln,c,c)			

		for v in range((ln + 1) * (not diag),len(escalonada)): # para cada linha depois (ou para todas)			

			if v != ln and len(escalonada[v]) > ln and escalonada[v][ln] != 0:
				eliminar(escalonada,v,ln,ln)																

	return escalonada

while __name__ == '__main__':
	try:
		linha = input(q)
		try:
			res = eval(linha)			
		except SyntaxError:
			res = exec(linha)
			if res != None:
				print('RES =', res)
		else:
			print('RES='+str(res))
	except KeyboardInterrupt:
		break
	except Exception as e:
		print('ERRO:',e)