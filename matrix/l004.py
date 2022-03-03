from det import * 

a = carregar('l41a'), carregar('l41ad')
b = carregar('l41b'), carregar('l41bd')
c = carregar('l41c'), carregar('l41cd')
d = carregar('l41c'), carregar('l41dd')

escrever(False)

for A,B in (a,b,c,d):

	print('\n\nMatriz:')
	mostrar(A)
	mostrar(B)

	x,b,g = thomas(A, B)

	print('\nBeta')
	mostrar(b)
	print(b)

	print('\nGama')
	mostrar(g)
	print(g)

	print('\nx\t/ Por escalonamento:')	 
	mostrar(aumentar(x, resolver(A, B)))
	print(x)



	

