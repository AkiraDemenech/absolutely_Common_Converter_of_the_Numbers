
from krypton import *
import time, random

define_t = time.time()	
print('Começando cronometragem de base em %.3f' %define_t)

escala = 256
lista_primos = integers()
lista_primos.load('ListaPrimos.txt') # carrega a lista complementada pelos cálculos de teste
if 65537 in lista_primos.inteiros:
	lista_primos.inteiros.pop(lista_primos.inteiros.index(65537))
	print('Removido o expoente público padrão da lista de %d primos' %len(lista_primos.inteiros))
print('Ordenando lista de primos...')
lista_primos.inteiros.sort()
print('Classificando primos da lista....')
dicio_primos = lista_primos.rank(escala) # organiza os primos pelas potências da escala
escalas = [e for e in dicio_primos]
escalas.sort()
print('Tamanhos máximos das classes de primos:',*escalas)

define_t = time.time() - define_t
print('Ciclo de referência: %fms' %(1000*define_t))

sorteste = lambda chaves = escalas: [chaves[int(len(chaves)*random.random())] for c in range(5)]
popteste = lambda classe, dicio: [dicio[c].pop(int(random.random()*len(dicio[c]))) for c in classe]

class testempo:
	dicio_t = {}
	dicio_p = dicio_primos
	decifra = mprime()
	cifra = mprime()
	casos = {}

	def __init__ (self, f):
		self.log = open(f, 'a')
		self.aberto = True
		self.fechar = self.log.close

	def carregar (self, d = None):
		if d == None:
			d = self.dicio_p
		self.dicio_p = d # salva o último dicionário usado para carregamento em caso de carregamento involuntário
		for c in d:
			if c in self.dicio_t:
				self.dicio_t[c].clear()
				self.dicio_t[c].extend(d[c])
			else:
				self.dicio_t[c] = list(d[c])

	def testar (self, caso=None):
		t_a = time.time()
		problemas = False
		while self.aberto:
			try:
				caso = popteste(caso,self.dicio_t)
				break
			except TypeError:
				caso = sorteste()
			except IndexError:
				self.carregar()
				problemas += 1	# carrega de emergência no máximo 1 vez
				if problemas > 1:
					print("Números insuficientes")
					return 
		

		self.cifra.public(*self.decifra.private(caso))
		t_b = time.time()
		m = int(self.cifra.produto * random.random())
		c = self.cifra.encrypt(m)
		d = self.decifra.decrypt(c)
		t_c = time.time()

		print(m, d,c,'\t',len(caso),*caso,'\t',self.cifra.expoente,'\t',1000*(t_b - t_a),1000*(t_c - t_b), (time.time() - t_c)*1000,file=self.log)
		return m-d





t = testempo('Testes.py.log')
t.carregar()
try:
	while True:
		r = t.testar()
		if r:
			print(r)
except KeyboardInterrupt:
	t.fechar()


'''
matplotlib.pyplot
.boxplot(conjunto de conjuntos)
.plot(x,y)
.show
'''