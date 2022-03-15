q = '\t'
saída = __name__ == '__main__' # quando este módulo é inicializado, por padrão, a saída de dados durante a execução das funções é permitida
falso = not saída
absolutely_no = lambda *args, **disagreements: args
absolutely_any = absolutely_no, print
escreva = lambda *coisas,**outras:absolutely_any[saída](*coisas,**outras)
escreva('''Por padrão, a saída de dados durante a execução das funções é permitida.
Caso queira desativar/ativar o print utilize a função escrever()\n''',q)

def inteiro (f):
	try:
		if f.is_integer():
			return int(f)
	except AttributeError:		
		if f == None:
			return 0
	return f

def mdcr (a,b=1,v=True):
	'''Calcula o Máximo Divisor Comum pelo algoritmo de Euclides usando recursão subtrativa'''
	if a >= b:
		if b==0:
			return a
		if v:	
			escreva('mdc(%d,%d)'%(a,b))
		return mdc(a-b,b)
	return mdc(b,a)

def modc (a,b=1,v = True):
	'''Calcula o Máximo Divisor Comum pelo algoritmo de Euclides usando recursão modular'''
	if a >= b:
		if b==0:
			return a
		if v:	
			escreva('mdc(%d,%d)'%(a,b))
		return modc(b,a%b,v)
	return modc(b,a,v)

def mdc (*n,mod=True,v=True):
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
		return mdc(mdc(*n[:2]),*n[2:],mod=mod,v=v)
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
		if v:	
			escreva('mdc(%d,%d)'%(a,b))
	
def mmc (*n,fmdc=mdc,v=True):
	'''Calcula o Mínimo Múltiplo Comum, por padrão, pelo Máximo Divisor Comum iterativo modular'''
	"""m = 1
	for p in n:
		m *= p
	return m//fmdc(*n)"""
	try:
		if len(n) < 2:
			return n[0]
		a,b = n
		n = a*b//fmdc(a,b,v=v)		
	except AttributeError:
		pass
	except IndexError:
		return
	except ValueError:
		return mmc(mmc(*n[:2],fmdc=fmdc,v=v),mmc(*n[2:],fmdc=fmdc,v=v))
	return n	

def divisores (n,t=set):
	'''Procura os divisores e retorna, por padrão, um conjunto set()'''
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
	escreva(c,'passos')
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
	'''Procura os fatores e os retorna, por padrão, numa lista list()'''
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
	escreva(c,'passos')
	if n!=1 or len(s)==0:
		try:
			s.append(n)
		except AttributeError:
			s[n] = 1
	return s

def fatorial (n, k = False, semi = True, t = inteiro):
	'''Calcula o fatorial de n, dividido pelo fatorial de k. Se semi > 1, calcula o semifatorial
	'''
	f = 1
	while n > k:
		f = t(f * n)
		n -= semi 
	return f

#maior_quadrado		= lambda n,d=1:
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
			escreva(c)
			return False
		d += 1 + abs(4 - (d%6))*(d%2)
		c += 1
	escreva(c)
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
	
def div (n, d = 1):
	d = n / d
	try:
		if d.is_integer():
			d = int(d)
	except AttributeError:
		pass
	return d

def escrever (novo_valor = -1):
	global saída
	if novo_valor < 0:
		saída = not saída
	else:
		saída = novo_valor
	escreva('saída =',saída)
	return saída	

def linha (b = True):
	while b:
		try:
			e = input(q)
			try:
				res = eval(e)
			except SyntaxError:
				res = exec(e)
				print('RES =', res)
			else:
				print('RES=',res)
		except KeyboardInterrupt:
			break
		except Exception as e:
			print('ERR:',e)
			
linha(saída)