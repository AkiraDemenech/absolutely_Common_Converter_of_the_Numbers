from poli import *

a = [-2, -9, 3, -5, 1]
b = [7, -5, 2, -3, 6, 1]
c = coeficientes({0: 11, 1: -13, 2: 5, 4: 6, 5: -8, 6: 1})

for p in a,b,c:

	print('\nPolinômio:\t', p)
	print('Descartes:\t', '%d positivas e %d negativas' %descartes(p))
	h = huat(p)
	if h != None:
		print('Huat:\tk =',h,'\t',p[h],'^ 2 <=',p[h-1],'*',p[h+1])

		