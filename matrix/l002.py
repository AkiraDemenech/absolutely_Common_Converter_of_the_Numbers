from det import * 

a = carregar('l2e1'), carregar('l2e1a')
b = carregar('l2e2'), carregar('l2e2b')
c = carregar('l2e3'), carregar('l2e3c')
d = carregar('l2e4'), carregar('l2e4d')

escrever(False)

for e,r in (a,b,c,d):

	print('\n\nMatriz:')
	mostrar(e)
	mostrar(r)

	g = cholesky(e)
	

	print('\nG * Gt')
	mostrar(matmul(g,transposta(g)))

	print('\nG')
	mostrar(g)

	print('\ny')
	y = resolver(g,r,inteiro)
#	y = [[y[0].real] for y in resolver(g,r)]
#	print(y)
	mostrar(y)

	print('\nx\t/ Por escalonamento:')
	x = aumentar(resolver(transposta(g),y,inteiro),resolver(e,r,inteiro))
	mostrar(x)



	

