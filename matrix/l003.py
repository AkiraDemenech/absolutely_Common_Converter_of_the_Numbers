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
	# como L já está escalonada, a resolução só precisa reduzir as linhas até a matriz virar a identidade
	mostrar(z)

	print('\ny')
	y = resolver(D,z)
	# sendo uma matriz diagonal, a única coisa que é feita para resolvê-la é dividir todas as linhas pelos seus pivôs
	mostrar(y)

	print('\nx\t/ Por escalonamento:')
	x = aumentar(resolver(transposta(L),y),resolver(A,B))
	# como L já está escalonada, a resolução só precisa reduzir as linhas até a matriz virar a identidade
	mostrar(x)



	

