import racional 


def f (coef, x):
	d = grau(coef)
	c = y = False
	p = True

	while c <= d:
		try:
			y += p * coef[c]
		except KeyError: # se for um dicionário		
			pass
		c += 1
		p *= x


	return y

def soma (a, b, formato = racional.muldiv.inteiro):

	a = coeficientes(a, formato)
	b = coeficientes(b, formato)
	c = len(b)
	while c > 0:
		c -= 1
		a[c] = formato(a[c] + b[c])

	return a	



def sub (a, b, formato = racional.muldiv.inteiro):	

	return soma(a, mul(b, -1, formato), formato)


def mul (a, b, formato = racional.frac):
	p = coeficientes(a, formato)
	q = coeficientes(b, formato)
	r = {}

	for a in range(len(p)):

		for b in range(len(q)):

			g = a + b
			v = 0 if not g in r else r[g]

			r[g] = formato(v + p[a] * q[b])	

	return r

mult = mul
add = soma	

def div (p, q, formato = racional.frac):
	p = coeficientes(p, formato)
	q = coeficientes(q, formato)

	d = {}

	g = grau(p)
	h = grau(q)
	

	while g >= h:

		if p[g]:			 
			e = g - h
			d[e] = formato(p[g] / q[h])
			p = sub(p, mul(q, {e: d[e]}, formato), formato)


		g -= 1

	return d, p

def grau (p):
	try:
		g = len(p)	
	except TypeError:	
		return False
	m = h = 0
	while h < g:
		try:
			if p[h]:
				m = h			
		except KeyError:	
			g = max(p) + 1
		h += 1	
	return m		
			

def coeficientes (coef, formato = racional.frac):

	d = grau(coef)
	c = 0
	b = []
	z = formato(0)

	while c <= d:

		try:
			b.append(formato(coef[c]) if coef[c] else z)
		except KeyError:	
			b.append(z)
		except TypeError:	
			b.append(formato(coef))
			break

			

		c += 1

	return b	

def sinais (coef):

	d = grau(coef)
	c = t = False	
	r = s = None

	while c <= d:
		try:
		#	print(r,s,t,coef[c],c,d,sep='\t')
			
			if coef[c]: # se não for nulo				
				r = coef[c] > 0								
				t += s != None and r != s # soma a troca se houver uma
				s = r
		except KeyError: # se for um dicionário		
			pass
		c += 1	

	return t		

def inverter (coef):	

	c = False
	d = grau(coef) + 1
	invertido = [c] * d

	while c < d:
		try:
			invertido[c] = coef[c] * (1 - (2 * (c % 2)))
		except KeyError:				
			if type(invertido) != dict:
				inv = {}
				for e in range(d):
					inv[e] = invertido[e]
				invertido = inv
		c += 1

	return invertido	

def descartes (coef):	

	return sinais(coef), sinais(inverter(coef))

def bolzano (coef, a, b):	
	return f(coef, a) * f(coef, b) <= 0

def huat (coef, k = None):	

	if k == None:

		c = 1
		d = grau(coef)
	#	h = False

		while c < d:
		#	print(c)
			if huat(coef, c):
				return c				
			#	h = True
			c += 1	
		return 	
		
	
	try:
		m = coef[k - 1] * coef[k + 1]		
	except Exception:	
		m = False

	try:
		n = coef[k] ** 2
	except Exception:		
		n = False

	return n <= m	

while __name__ == '__main__':
	print(eval(input()))