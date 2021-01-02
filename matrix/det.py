
from numpy import array
from muldiv import mmc,escreva,escrever

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
			r[j][i] = e()
			i += 1
		j += 1
	if type(r) != t:
		return t(r)
	return r

def det (m, s = mul):
	
		
	return r, c, d

escrever()
print(mmc(10,10,10,11))