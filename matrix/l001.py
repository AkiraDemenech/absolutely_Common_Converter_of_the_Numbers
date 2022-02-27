from det import escrever, mostrar, carregar, salvar, det, lui

escrever(True)

e = 1
while e <= 6:
	
	arq = 'l1e%d' %e
	
	print('\n\n',arq)
	A = carregar(arq)
	mostrar(A)
	
	
	
	
	L, U, Ai = lui(A)
	print('\nInversa')
	salvar(Ai, arq + '-1')
	mostrar(Ai)
	
	print('\nInferior (fatores)')
	mostrar(L)
	
	print('\nSuperior (escalonada)')
	mostrar(U)		
	
	print('\tDeterminante =',det(U))
	
	
	
	
	e += 1



