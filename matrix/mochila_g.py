
from mochila_t import mochila, escrever, rodar, sys

def geraroda():
	for t in [10,100,1000]:
		a = open('%d..txt'%t,'w')
		b = open('%d_.txt'%t,'w')
		for c in mochila.gerar(10,t):
			print('\nnx',file=escrever(a,c))
			print('\n',  file=escrever(b,c))
		a.close()
		b.close()

rodar()
print('Acabou!',file=sys.stderr)
input()