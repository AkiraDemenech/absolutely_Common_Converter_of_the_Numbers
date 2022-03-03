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

a = carregar('l42a'), carregar('l42ab')
b = carregar('l42b'), carregar('l42bb')
c = carregar('l42c'), carregar('l42cb')
d = carregar('l42c'), carregar('l42db')



for A,B in (a, b, c, d):

	escrever(True)

	print('\n\nMatriz:')
	mostrar(A)
	mostrar(B)

	print('\nJacobi')
	mostrar(gauss(A,B,jacobi))

	print('\nSeidel')
	mostrar(gauss(A, B))

	escrever(False)

	print('\npor escalonamento')
	mostrar(resolver(A, B))

	

