
from numpy import array, matmul
from muldiv import mmc,mdc,div, escreva,escrever,q
from racional import frac

auto = False
def auto_salvar (s = None):
	global auto
	if s == None:
		s = not auto
	auto = s	
	escreva('Auto-salvar', q, auto)

identidade = lambda j,i: int(i == j)
entrar = lambda y,x: eval(input(f'[{y},{x}] = '))
mem = 'res.log'
res_salvo = None
def salvar (dados, arq = mem):
	global res_salvo
	res_salvo = dados
	fechar = print
	if type(arq) == str:
		arq = open(arq,'w',encoding='utf8')
		fechar = arq.close	
	print(repr(dados).encode(), file = arq)	
	fechar()

def carregar (arq = mem):	
	if type(arq) == str:
		arq = open(arq,'r',encoding='utf8')
		fechar = arq.close
	else:	
		fechar = print
	dados = arq.read()
	fechar()	
	while True:
		dados = eval(dados)
		if type(dados) != bytes:
			global res_salvo
			res_salvo = dados
			return dados
		dados = dados.decode()	


def mat (x = 4, y = None, e = entrar, t = array, r = None, v = 0):
	if y == None:
		y = x
	if r == None:
		r = []
	while len(r) < y:
		r.append([])
	j = 0
	while j < y:				
		while len(r[j]) < x:			
			try:
				r[j].append(e(j,len(r[j])))				
			except TypeError:
				if len(e) > j and len(e[j]) > len(r[j]):
					r[j].append(e[j][len(r[j])])	
					x = len(e[j])
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
	return f

def escalonar (m, diag = False, reduzir = False, fatores = None, formato = None):
	if formato == None:
		formato = frac
	escalonada = [[formato(k) for k in n] for n in m]
	
	
	cp = ln = 0
	while ln < len(escalonada): # para cada linha da matriz
		

		while cp < len(escalonada[ln]) and escalonada[ln][cp] == 0:
		#	enquanto o elemento do pivô, naquela linha, for 0

			n = len(escalonada)
			while n > ln: # busca uma linha em que o elemento da mesma coluna não for 0
				n -= 1
				if ln < len(escalonada[n]) and escalonada[n][cp] != 0:
					escreva(q,'Somar linha',n,'na',ln)
					escreva(escalonada[ln], '+=', escalonada[n])
					somar(escalonada[ln], escalonada[n]) # e soma a linha encontrada na anterior					
					escreva(escalonada[ln], '\n')
					break
			else: # se não encontrar nenhum 	
				cp += 1
				continue
			break
		else:
			if cp >= len(escalonada[ln]):
				break
			

		if ln != cp:
			escreva('A coluna pivô da linha',ln,'é',cp)		
		
		if reduzir:
			escreva(q,'Multiplicando linha',ln,'por',1/escalonada[ln][cp])
			escreva(escalonada[ln],'*',1/escalonada[ln][cp])
			c = len(escalonada[ln])
			while c > cp:			
				c -= 1
				escalonada[ln][c] = inteiro(escalonada[ln][c] / escalonada[ln][cp])
			escreva(escalonada[ln],'\n')	

		
		for v in range((ln + 1) * (not diag),len(escalonada)): # para cada linha depois (ou para todas)			

			if v != ln and len(escalonada[v]) > cp and escalonada[v][cp] != 0:
				m = eliminar(escalonada,v,ln,cp)																
				if fatores != None:
					fatores[(v,cp)] = m 
				#	escreva([v,cp],m)

		ln += 1		
		cp += 1

		escreva()

	return escalonada

def lu (a):	
	f = {}	
	u = array(escalonar(a, fatores = f))
	l = mat(len(a), e = lambda y,x: identidade(y,x) if not (y,x) in f else f[(y,x)])
	return l, u	



def lui (a):
	f = {}
	aum = aumentar(a)
	esc = escalonar(aum, fatores = f)
	u = array(esc)[:,:len(a)]
	l = mat(len(a), e = lambda y,x: identidade(y,x) if not (y,x) in f else f[(y,x)])
	i = escalonar(esc, True, True)
	return l,u,array(i)[:,len(a):]

def ld (a, formato = frac):	

	l = mat(len(a), e = identidade, t = list)
	d = mat(len(a), e = identidade, t = list) 

	for i in range(len(a)):

		d[i][i] = formato(0 if len(a[i]) <= i else a[i][i])
		for j in range(i):
			d[i][i] -= ( l[i][j] ** 2 ) * d[j][j]					

		for j in range(i + 1, min(len(a[i]), len(a))):
			c = 0 if j >= len(a) or i >= len(a[j]) else a[j][i]
			
			for k in range(i):
				c -= l[j][k] * l[i][k] * d[k][k] 	

			l[j][i] = inteiro(c / d[i][i])

	return l, d



def cholesky (a, formato = inteiro):	
	g = []
	z = formato(0)
	while len(g) < len(a): 
		h = []
		while len(h) < len(a[len(g)]):
			d = formato(a[len(g)][len(h)])
			if len(h) == len(g):				
				for c in range(len(h)):
					d -= h[c] ** 2 
				h.append(formato(d ** 0.5))	
			elif len(h) < len(g): 					
				for c in range(len(h)):
					d -= h[c] * g[len(h)][c]
				h.append(formato(d / g[len(h)][len(h)]))	
			else:		
				h.append(z)
		g.append(h)

	g[0][0] = formato(a[0][0] ** 0.5)



	return g


def thomas (m, d, formato = frac):

	a, b, c = diagonais(m, 3)

	gama = []
	beta = []

	ag = ab = 0
	for k in range(len(m)):					
		
		beta.append([formato(formato((0 if len(d[k]) <= 0 else d[k][0]) - ab) / formato(b[k] - ag))])
		if k < len(m) - 1:
			gama.append([formato(c[k] / formato(b[k] - ag))])	
			ab = a[k + 1] * beta[k][0]
			ag = a[k + 1] * gama[k][0]

	x = [None] * len(beta)		
	x[-1] = list(beta[-1])
			
	while k > 0:
		k -= 1

		x[k] = [beta[k][0] - x[k + 1][0] * gama[k][0]]

	return x, beta, gama	

def jacobi (a, b, formato = frac, aprox = 10, inicial = False):

	x_ = [formato(inicial)] * len(a)
	x = list(x_)

	while aprox != 0:
		aprox -= 1
	
		for i in range(len(a)):

			p = b[i][0]

			for j in range(len(a[i])):

				if i != j:
					p -= a[i][j] * x_[j]

			x[i] = formato(p / a[i][i])		

		escreva(x_)
		x_ = list(x)

	return [[s] for s in x]	



def diagonais (m, diam = True):

	diag = [[0] * len(m) for s in range(diam)]
	raio = len(diag) // 2
	
	for i in range(len(m)):

		for j in range(len(m[i])):

			if abs(i - j) <= raio:

				diag[raio + j - i][i] = m[i][j]

	return diag			

 

	




def transposta (m): 
	t = []	
	for l in range(len(m)):	
		for c in range(len(m[l])):
			while len(t) <= c:
				t.append([0]*l)					
			t[c].append(m[l][c])
	return t			


def inversa (a):			
	return array(escalonar(aumentar(a),True,True))[:,len(a):]		

def aumentar (a, b = identidade):	
	i = mat(len(a), e = b, t = tuple)
	for l in range(len(a)):
		for c in range(len(a[l])):
			i[l].insert(c, a[l][c])			
	return i		

def mostrar (a, d = 6):	
	for ln in a:
		for c in ln:
			print(inteiro(round(c.real, d)),end=q)
		print(q)	

def simetria (m):		
	
	for i in range(len(m) - 1):
		for j in range(i + 1, len(m[i])):
			if m[i][j] != m[j][i]:
				return False
	return True	

def triangular (m):
	l = u = True
	for i in range(len(m)):
		for j in range(len(m[i])):
			if m[i][j]:
				if i > j:
					if not l:
						return None 
					u = False	
				elif i < j:	
					if not u:
						return None
					l = False								  
	return u - l				 
def diagonal (a, diam = True):
	raio = abs(diam)//2
	for i in range(len(a)):
		for j in range(len(a[i])):
			if a[i][j] and abs(i - j) > raio:
				return False
	return True			


def triangular_superior (a):
	return triangular(a) in {0,1}

def triangular_inferior (a):
	return triangular(a) in {0,-1}

def resolver (a, b, formato = None):   	
	m = escalonar(aumentar(a, b),True,True,formato = formato)
	n = 0
	for l in a:
		if len(l) > n:
			n = len(l)
	s = []
	for l in m:		
		if len(l) > n:
			s.append(l[n:])
		else:	
			s.append(l[:-1])
	return s		



while __name__ == '__main__':
	try:
		linha = input(q)
		try:
			res = eval(linha)			
		except SyntaxError:
			r = exec(linha)
			if r != None:
				print('RES =', r)
				res = r
				continue
		else:
			print('RES='+(repr(res) if type(res) == str else str(res)))
		if auto:	
			escreva('Auto-salvando....')
			salvar(res)
	except KeyboardInterrupt:
		break
	except Exception as e:
		print('ERRO:',e)
		err = e