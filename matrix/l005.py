from poli import *

a = [-2, -9, 3, -5, 1]
b = [7, -5, 2, -3, 6, 1]
c = coeficientes({0: 11, 1: -13, 2: 5, 4: 6, 5: -8, 6: 1}, racional.muldiv.inteiro)

racional.muldiv.escrever(True)

for p in a,b,c:

	print('\nPolinômio:\t', p)
	

	print('Descartes:\t', '%d positivas e %d negativas' %descartes(p))
	h = huat(p)
	if h != None:
		print('Huat:\tk =',h,'\t',p[h],'^ 2 <=',p[h-1],'*',p[h+1])	
	b, a = laguerre_thibault(p)	
	print('Laguerre-Thibault:\traízes entre %d e %d' %(b,a))	
	print('Fujiwara:\tvalor absoluto máximo de',fujiwara(p))
	q = kojima(p)
	print('Kojima:\tvalor absoluto máximo de', q[0] + q[1], '=', q[1], '+', q[0])
	print('Cauchy:\tvalor absoluto máximo de', cauchy(p))

	
	while a <= b:
		racional.muldiv.escreva(a, racional.muldiv.q, f(p, a))
		a += 1




