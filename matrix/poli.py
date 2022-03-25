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

def df (p):	
	d = {}
	for c in resumir(p):		
		try:
			b = p[c] * c
			if b:
				d[c - 1] = b 
		except KeyError:	
			continue
	return d
		
	

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
			p = soma(p, mul(q, {e: -d[e]}, formato), formato)


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


def resumir (coef):
	if type(coef) == dict:
		return dict(coef)

	r = {}
	for c in range(len(coef)):	
		if coef[c]:	
			r[c] = coef[c]
	return r		


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

def inverter (coef, mod = True, freq = 2):	

	c = False
	d = grau(coef) + 1
	invertido = [c] * d

	while c < d:
		try:
			invertido[c] = coef[c] * (1 - (2 * (c % freq == mod)))
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

def laguerre (coef, formato = racional.frac):

	m = -1
	d = [0, 1]
	
	try:
		while True:

			d[0] = m

			q,r = div(coef, d, formato)

			racional.muldiv.escreva(m, racional.muldiv.q, q, racional.muldiv.q, r)

			for e in q:
				if q[e] < 0:
					if e < max(q):
						break
					return False # nunca será possível encontrar cota se o coeficiente de maior grau for negativo
			else:	
				if r[0] > 0:
					return -m
					

			m -= 1	
	except KeyboardInterrupt:		
		return False # 0 significa que não foi encontrada cota superior para as raízes positivas
	
	

def laguerre_thibault (p, formato = racional.muldiv.inteiro):
	g = grau(p)
	if g <= 0:
		return False, False
	if p[g] < 0:	
		p = mult(p, -1)
	return laguerre(p, formato), -laguerre(inverter(p, not (g % 2)), formato)

def kojima (p, formato = racional.muldiv.inteiro):	
	
	q = raio_complexo(p, formato)
	q.sort()

	return q[-2:]

def fujiwara (p, formato = racional.muldiv.inteiro):			

	return 2 * max(raio_complexo(p, formato))

def cauchy (p, x = 0, k = 10):	

	n = grau(p)
	p = cotas(p)
	

	for i in range(k):
		racional.muldiv.escreva(i, racional.muldiv.q, x)
		x = f(p, x) ** (1 / n)

	return x

def cotas (coef, formato = racional.muldiv.inteiro):

	coef = coeficientes(coef, formato)
	
	return [formato(abs(coef[a] / coef[-1])) for a in range(grau(coef))]
		

def raio_complexo (coef, formato = racional.muldiv.inteiro):	

	q = cotas(coef, formato)
	n = len(q)

	for a in range(len(q)):
		q[a] = formato(q[a] ** (1 / n))
		n -= 1

		racional.muldiv.escreva(a, racional.muldiv.q, q[a])

	return q

def chebyshev (coef, x = 0, k = 10):

	d_ = df(coef)
	d__ = df(d_)

	for i in range(k):
		racional.muldiv.escreva(i, racional.muldiv.q, x)
		d1 = f(d_, x)
		d = f(coef, x) / d1
		x -= d + d * d * f(d__, x) / (2 * d1)

	return x

def newton_raphson (coef, x = 0, k = 10):

	d = df(coef)

	for i in range(k):
		racional.muldiv.escreva(i, racional.muldiv.q, x)
		x -= f(coef, x) / f(d, x)

	return x	



hist = []
while __name__ == '__main__':
	try:
		linha = input(racional.muldiv.q)
		try:
			res = eval(linha)			
		except SyntaxError:
			r = exec(linha)
			if r == None:
				continue
			print('RES =', r)
			res = r
				
		else:
			print('RES='+(repr(res) if type(res) == str else str(res)))		
		hist.append(res)
	except KeyboardInterrupt:
		break
	except Exception as e:
		print('ERRO:',e)
		err = e