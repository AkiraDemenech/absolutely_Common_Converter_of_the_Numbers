def sinais (coef):

	d = len(coef)
	c = t = False	
	r = s = None

	while c < d:
		try:
		#	print(r,s,t,coef[c],c,d,sep='\t')
			
			if coef[c]: # se não for nulo				
				r = coef[c] > 0								
				t += s != None and r != s # soma a troca se houver uma
				s = r
		except KeyError: # se for um dicionário		
			d = max(coef) + 1
		c += 1	

	return t		

print(sinais([-2, -9, 3, -5, 1]))
print(sinais([7, -5, 2, -3, 6, 1]))
print(sinais({0: 11, 1: -13, 2: 5, 4: 6, 5: -8, 6: 1}))