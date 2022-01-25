

def mdc_ext (a, b):
	'''Algoritmo estendido de Euclides'''
	m = nj = 1
	n = mj = not m
#	print(a, b, m, n)
	while a != 0:
	#	y,x = x,y - (x*(b//a))
		q = b//a
		mi = mj
		ni = nj
		nj = n
		mj = m
		m = mi - mj*q
		n = ni - nj*q
		a,b = b%a, a
	#	print(a, b, m, n)
	return b, mj, nj

def pot_mod (b, exp, m):
	'''Potência modular b**exp mod m'''
	p = 1
	if exp < 0:
	#	exp *= 1 - phi(m) # o expoente é invertido e multiplicado pela antecessora da totiente de m 
		exp = - exp
		b = mdc_ext(b,m)[1] # inverso do b (primeiro argumento) é o primeiro coeficiente (depois do MDC)
	#	b = (1 - (m*(m%b)))/b
	#	if b.is_integer():
	#		b = int(b)
	while p != 0 and exp > 0:
		if exp%2:
			p = (p*b)%m
		exp //= 2
		b = (b*b)%m
	return p
	
def produto (f):
	'''Retorna o produto dos fatores.'''
	m = 1
	for n in f:
		m *= n
	return m


def phi (p) -> int:
	'''Função totiente de Euler (quantidade de inteiros positivos relativamente primos ao número composto por primo(s) sem repetição) 
	Retorna o produto dos antecessores dos fatores primos.'''
	m = 1
	for pi in p:
		m *= pi - 1
	return m

def tcr (a, m, m_comp = 0):
	if m_comp == 0:
		m_comp = produto(m)
	i = x = 0
	while i < len(a):
		mi = m_comp//m[i]
		x += a[i]*mi*pot_mod(mi,-1,m[i])
		i += 1
	return x%m_comp

prox = lambda d: 1 + abs(4 - (d%6))*(d%2) # função de incremento para o próximo primo em potencial
def primo (p, incr = prox) -> bool:
	'''Retorna se p é um número primo positivo, 
	incrementando os divisores de teste conforme a função incr.'''
	
	r = p**0.5
	c = 2
#	q = c * c
#	i = c + c + 1 
#	while c <= p//c:
	while c <= r:
		if p % c == 0:
			return p == c
		c += incr(c)
	#	q += i
	#	i += 2

	return p > 1


class integers:

	inteiros = None
	tamanhos = {}

	def load (self, file="ListaPrimos.txt"):
		"""Carrega os inteiros do arquivo para a lista e retorna-a"""
		arq = open(file,'r')
		if self.inteiros == None:
			self.inteiros = []
		for ln in arq:
			try:
				self.inteiros.append(int(ln))
			except KeyboardInterrupt:
				break
			except ValueError as v:
				print("ERR:",v, "@" + ln)
	#	self.inteiros = [eval(ln) for ln in arq]
		arq.close()
		return self.inteiros

	def save (self, file: str, l = None):
		"""Registra os inteiros da lista no arquivo"""
		if l == None:
			l = self.inteiros 
		arq = open(file,'w')
		for n in l:
			print(n,file=arq)
		arq.close()

	def rank (self, base = 2, l = None, s=None):
		"""Organiza a lista de números pelas ordens de grandeza (quantidade de dígitos da base)
		Para economizar processamento, consideramos a lista de inteiros e ordenada desde o início
		Caso não haja lista nem nos argumentos nem na instância da classe, haverá erro, 
		mas se tudo der certo, escreve no arquivo solicitado
		 e então guarda ou sobrescreve o dicionário criado com a base como chave antes de retorná-lo.
		"""
		if l == None:
			l = self.inteiros
		tamanhos = {}
		t = 1
		for p in l:
			while t < p:
				t *= base
				tamanhos[t] = []
			tamanhos[t].append(p)
		if s != None:
			s = open(s,'w')
			print(tamanhos, file=s)
			s.close()
		self.tamanhos[base] = tamanhos
		return tamanhos

	def find (self, limit = -1, start = None, step = prox):
		"""Encontra os próximos primos até o limite decrementado ser igual a 0 (caso ele nunca seja exatamente nulo, fará até ser interrompido),
		por padrão, começa no último elemento da lista (se houver) ou então em 2, testando somente os prováveis primos.
		Retorna o último número testado e o valor final do limite ao final da busca"""
		if start == None:
			start = 2
			try:
				start = self.inteiros[len(self.inteiros) - 1]	
			except IndexError:
				pass
			except TypeError:
				self.inteiros = []
		
		try:
			while limit != 0:
				limit -= 1
				if primo(start):
				#	print(start)
					self.inteiros.append(start)
				start += step(start)
		except KeyboardInterrupt:
			pass
		return start, limit

class mprime:
	
	def public (self, k = None, e = None):
		"""Retorna a chave pública, seta seu valor para k caso não seja nulo
		Chave válida: par indexado N,e do produto dos múltiplos primos N e do expoente público coprimo a phi(N)"""
		if k != None:
			if e != None:
				self.expoente = e
			self.produto = k
		return self.produto, self.expoente

	def private (self, N = None, e = 65537):
		"""Seta a chave privada e retorna a pública referente, caso a entrada não seja nula
		Chave válida: par indexado N,e do conjunto de primos secretos e do expoente público desejado, coprimo a phi(N)."""  
		if N == None:
			return self.primos, self.inverso
		coprimos = phi(N)
		self.primos = N
		self.inverso = self.pow(e,-1,coprimos)
		return self.public(produto(N),e)

	def encrypt (self, M: int) -> int:
		return self.pow(M, self.expoente, self.produto)
	def decrypt (self, C: int) -> int:
		return tcr([pot_mod(C, self.inverso%(p - 1), p) for p in self.primos], self.primos, self.produto)
	#	return pot_mod(C, self.inverso, self.produto)

	def __init__ (self, potenciar = pot_mod):
		self.pow = potenciar 

'''
b = 105
a = 2
e = pot_mod(a,-1,b)
print(a,'^-1 mod',b,'=',e)
print(a*e%b, a*e, (a*e//b)*b)



c = mprime()
c.private((3,5,7),5)
d = c.encript(75)
print(d, c.decript(d), c.inverso, c.produto, phi(c.primos))
for m in range(c.produto): 
	if c.decript(c.encript(m)) != m:
		print(c.decript(c.encript(m)), m)





print('Carregando primos....')
p = integers()
p.load()
print('Procurando mais primos....')
print(p.find(1))
#p.save('ListaPrimos.log')
print('Classificando....')
p = p.rank(256)
for k in p:
	if len(input('\t< %d [%d]' %(k,len(p[k])))) > 0:
		for n in p[k]:
			print(n)
	
print(primo(6741563))
print(primo(6804583))
print(primo(65537)) # o maior inteiro com potencial de ser divisor de 65537 é 256 (a raíz quadrada de 65537 é pouco mais de 2^8). ''' 