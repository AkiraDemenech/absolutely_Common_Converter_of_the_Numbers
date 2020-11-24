
from numpy import array

ast = "*"
mul = '·'

def mmc (a,b=1):
	m=c=1
	while a >1 and b > 1:
		c += 1 + abs(4 - (c&6))*(c%2)
		while a%c == b%c == 0:
			m *= c
			a /= c
			b /= c
		while b%c == 0:
			b /= c
		while a%c == 0:
			a /= c
	return m

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
	d = c = ''
	n = len(m)
	r = a = 0
	while a < n:
		c += '+'
		d += ' + '
		
		t = 1
		b = 0
		while b < n:
			v = str(m[b][(a+b)%n])
			if m[b][(a+b)%n] < 0:
				v = '('+v+')'
			elif b > 0:
				d += s
			d += v
			t *= m[b][(a+b)%n]
			if b > 0:
				c += ast
			c += v
			b += 1
		r += t
		a += 1
	
	while a > 0:
		a -= 1
		c += '-'
		d += ' – ' 
		
		b = 0
		t = 1
		while b < n:
			t *= m[b][(a-b)%n]
			v = str(m[b][(a-b)%n])
			if m[b][(a-b)%n] < 0:
				v = '('+v+')'
			elif b > 0:
				d += s
			if b > 0:
				c += ast
			c += v
			d += v
			b += 1
		r -= t
		
	return r, c, d