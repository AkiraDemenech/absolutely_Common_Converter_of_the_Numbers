from det import * 

a = carregar('l3e1'), carregar('l3e1a')
b = carregar('l3e2'), carregar('l3e2b')
c = carregar('l3e3'), carregar('l3e3c')
d = carregar('l3e4'), carregar('l3e4d')

escrever(False)

for A,B in (a,b,c,d):

	print('\n\nMatriz:')
	mostrar(A)
	mostrar(B)

	L,D = ld(A)
	

	print('\nL * D * Lt')
	mostrar(matmul(matmul(L,D),transposta(L)))

	print('\nL')
	mostrar(L)

	print('\nD')
	mostrar(D)



	print('\nz')
	z = resolver(L,B)
	mostrar(z)

	print('\ny')
	y = resolver(D,z)
	mostrar(y)

	print('\nx\t/ Por escalonamento:')
	x = aumentar(resolver(transposta(L),y),resolver(A,B))
	mostrar(x)



	

