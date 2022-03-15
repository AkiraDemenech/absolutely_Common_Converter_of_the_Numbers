def f (coef, x):
	d = len(coef)
	c = y = False
	p = True

	while c < d:
		try:
			y += p * coef[c]
		except KeyError: # se for um dicionário		
			d = max(coef) + 1
		c += 1
		p *= x


	return y


def sinais (coef):

	d = len(coef)
	c = t = False	
	r = s = None

	while c < d:
		try:
		#	print(r,s,t,coef[c],c,d,sep='\t')
			
			if coef[c]: # se não for nulo				
				r = coef[c] > 0								
				t += s != None and r != s # soma a troca se houver uma
				s = r
		except KeyError: # se for um dicionário		
			d = max(coef) + 1
		c += 1	

	return t		

def inverter (coef):	

	c = False
	d = len(coef)
	invertido = [c] * d

	while c < d:
		try:
			invertido[c] = coef[c] * (1 - (2 * (c % 2)))
		except KeyError:	
			d = max(coef) + 1
			inv = {}
			for e in range(c):
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
		d = len(coef) - 1
	#	h = False

		while c < d:
		#	print(c)
			if huat(coef, c):
				return c				
			#	h = True
			c += 1	
		return None	
		
	
	try:
		m = coef[k - 1] * coef[k + 1]		
	except Exception:	
		m = False

	try:
		n = coef[k] ** 2
	except Exception:		
		n = False

	return n <= m	

