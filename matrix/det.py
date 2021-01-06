
from numpy import array
from muldiv import mmc,mdc,div, escreva,escrever,q

ast = "*"
mul = '·'
'''
def mmc (a,b=1):
	m=c=1
	if b < 0:
		b = -b
	if a < 0:
		a = -a
	while a >1 and b > 1:
		c += 1 + abs(4 - (c&6))*(c%2)
		while a%c == 0 or b%c == 0:
			m *= c
			if b%c == 0:
				b /= c
			if a%c == 0:
				a /= c
	return m*b*a
'''

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

escrever()
def escalonar (m):
	escalonada = []
	c = 0
	while c < len(m):
		escalonada.append([dif(m[c]),list(m[c]),c])
	#	escalonada[c].insert(0,dif(m[c]))
		c += 1
	escalonada.sort()
	while c > 0:
		c += -1
		escalonada[c].append(array(m[escalonada[c].pop()]))
		arr = len(escalonada[c])-1 
	while c < len(escalonada):
		while escalonada[c][0] < c:
			b = 0
			while escalonada[c][0] != escalonada[b][0]:
				b += 1
				b += b == c
			if b >= len(escalonada):
				break
			k = mmc(escalonada[c][arr][escalonada[c][0]],escalonada[b][arr][escalonada[b][0]])
			escalonada[c][arr] *= div(k,escalonada[c][arr][escalonada[c][0]])
			if escalonada[c][arr][escalonada[c][0]] > 0:
				k = -k
			escalonada[c][arr] += div(k,escalonada[b][arr][escalonada[b][0]])*escalonada[b][arr]
			escalonada[c][arr] //= mdc(*escalonada[c][arr])
			escalonada[c][1].clear()
			escalonada[c][1].extend(escalonada[c][arr])
			escalonada[c][0] = dif(escalonada[c][arr])
		c += 1
	return array([c[arr] for c in escalonada])

while __name__ == '__main__':
	try:
		res = input(q)
		try:
			res = eval(res)
		except SyntaxError:
			res = exec(res)
			print('RES =', res)
		else:
			print('RES='+str(res))
	except KeyboardInterrupt:
		break
	except Exception as e:
		print('ERRO:',e)