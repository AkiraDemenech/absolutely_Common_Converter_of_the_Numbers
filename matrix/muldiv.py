

def mdcr (a,b=1):
	'''Calcula o Máximo Divisor Comum pelo algoritmo de Euclides usando recursão subtrativa'''
	if a >= b:
		if b==0:
			return a
		print('mdc(%d,%d)'%(a,b))
		return mdc(a-b,b)
	return mdc(b,a)

def modc (a,b=1):
	'''Calcula o Máximo Divisor Comum pelo algoritmo de Euclides usando recursão modular'''
	if a >= b:
		if b==0:
			return a
		print('mdc(%d,%d)'%(a,b))
		return modc(b,a%b)
	return modc(b,a)

def mdc (*n,mod=True):
	'''Calcula o Máximo Divisor Comum pelo algoritmo de Euclides usando iteração'''
	try:
		if len(n) < 2:
			return n[0]
		a,b=n
		if a<0:
			a = -a
		if b<0:
			b = -b
	except ValueError:
		return mdc(mdc(*n[:2]),*n[2:])
	except IndexError:
		return
	while True:
		if b>a:
			a,b=b,a
		if b==0:
			return a
		if mod:
			a %= b
		else:
			a -= b
		print('mdc(%d,%d)'%(a,b))
	
def mmc (*n,fmdc=mdc):
	'''Calcula o Mínimo Múltiplo Comum pelo Máximo Divisor Comum iterativo modular'''
	"""m = 1
	for p in n:
		m *= p
	return m//fmdc(*n)"""
	try:
		a,b = n
		return a*b//fmdc(a,b)
	except ValueError:
		if len(n) < 2:
			return ((0,)+n)[len(n)]
		return mmc(mmc(*n[:2]),mmc(*n[2:]))

def divisores (n,t=set):
	if n == 0:
		return t()
	try:
		neg = n < 0
		n = abs(n)
		
		if n.is_integer:
			n = int(n)
	except TypeError:
		pass
	except AttributeError:
		pass
	c = 0
	d = 2
	m = n#1 + n**(1/2)
	s = t((1,n))
	while d<m:
		m = n/d
		if n%d==0:
			if m.is_integer:
				m = int(m)
			try:
				s.add(d)
				s.add(m)
			except AttributeError:
				s.append(d)
				if d != m:
					s.append(m)
				s.sort()
		d += 1
		c += 1
	print(c,'passos')
	if neg:
		neg = []
		for c in s:
			neg.append(-c)
		try:
			return s + t(neg)
		except TypeError:
			return s.union(s,neg)
	return s

def fatores (n,t=list):
	c = 0
	d = e = 2
	try:
		s = t()
	except TypeError:
		s = t
	t = type(n)
	while abs(n)>=2:#n!=1
		try:
	#	if abs(n)%d==0:
			while abs(n)%d==0:
				try:
					s.append(d)
				except AttributeError:
					try:
						s[d] += 1
					except KeyError:
				#	if not d in s:
						s[d] = 1
				n /= d
	#		e = d = 2
	#	else:
			if d > abs(n)/d:
	#			d = t(n)
				if n.real == 0:
					d = n.imag
				else:
					d = n.real
				d = abs(d)
				if d.is_integer():
					d = int(d)
			else:
				d += e//(d%3) # 1 + abs(4 - (d%6))*(d%2)
		except ZeroDivisionError:
			d += 2
			e = 4
		#	d += 1 + d%2
		except AttributeError:
			pass
		except TypeError:
			break
		c+=1
	print(c,'passos')
	if n!=1 or len(s)==0:
		try:
			s.append(n)
		except AttributeError:
			s[n] = 1
	return s

#maior_quadrado 		= lambda n,d=1:
primeiro_quadrado	= lambda n,d=1:((n/d)+d)/2
quadrado_divisor	= lambda n: {(primeiro_quadrado(n,d),d) for d in divisores(n)}
intdifquad	= lambda n: [(type(a),type(b)) for a,b in difquad(n)].count((int,int))
def difquad (n,t=set):
	t = t()
	for a,d in quadrado_divisor(n):
		a,b = abs(a),abs(a-d)
		if a.is_integer():
			a = int(a)
		if b.is_integer():
			b = int(b)
		try:
			t.add((a,b))
		except AttributeError:
			t.append((a,b))
	return t

def primo (n):
	'''	try:
		if len(divisores(n,tuple))>1:
			return n*n!=1
	except AttributeError:
		return False'''
	d = 2
	c = 0
	n = abs(n)
	while d <= n/d:
		if n%d == 0:
			print(c)
			return False
		d += 1 + abs(4 - (d%6))*(d%2)
		c += 1
	print(c)
	return n>=2

def composto (n):
	return (not primo(n)) and n*n>1
		#	n*n>1 and not primo(n)
		
def compor (p):
	d =type(p)==dict
	r =1
	for f in p:
		if d:
			r *= f**p[f]
		else:
			r *= f
	return r
	
def div (n,d=1):
	return n//d,n%d

while True:
	try:
		q = input('\t')
		try:
			print('RES=',eval(q))
		except SyntaxError:
			print('RES =',exec(q))
	except KeyboardInterrupt:
		break
	except Exception as e:
		print('ERR:',e)