import det
#det.escrever(True)

def particionar (a, xb, xn):

	pb = []
	pn = []
	for i in range(len(a)):
		pb.append([])
		pn.append([])
		
		for j in range(len(xn)):
			pn[-1].append(a[i][xn[j]])
		
		for j in range(len(xb)):
			pb[-1].append(a[i][xb[j]])	



	return pb, pn			


def primal (A, b, c):

	m = len(A)
	n = len(A[0])
	print('n =', n)
	print('m =', m)

	p = list(range(n-m,n))
	q = list(range(n-m))
	cB, cN = particionar(c, p, q)
	B, N = particionar(A, p, q) 
	Bi = det.inversa(B)
	xB = det.matmul(det.transposta(b), Bi)[0]
#	xB = det.transposta(det.resolver(B, b))[0]
#	l = det.transposta(det.resolver(det.transposta(B), det.transposta(cB)))
	l = det.matmul(cB, Bi)
#	print(Bi)
	
	print('Partição básica inicial:\t',p)
	#print(q)
	
	while True:
		try:
			print('\nPartição básica:\t',p,q)			
			print('B =',B)
			print('N =',N)
			
			print(xB)

			v = min(xB)
			print(v)
			if v < 0: # se houver valor negativo
				print('não factível') 
			else: 
				print(end='Solução factível ')
				if v: # se todos forem positivos	
					print(end='não ')
				print('degenerada\n')

			print('Custos:\t',cB,cN)

			print('Multiplicador:\t',l)			

			ln = det.matmul(l,N)
		#	print(ln)
			cNr = det.somar(cN[0],ln[0],-1)
			print('Custos relativos:\t',cNr)
			v = min(cNr) 
			print(v)

			if v >= 0: # solução ótima
				if v:
					print('Solução ótima única')
				else:
					print('Múltiplas soluções ótimas')
				break

			k = cNr.index(v)
			aNk = particionar(N,[k],[])[0]

		#	y = det.resolver(B, aNk)
			y = det.matmul(Bi, aNk)
			print('Direção:\t',y)
			print('k =',q[k])

			e = min([(xB[i]/y[i][0], i) for i in range(m) if y[i][0] > 0])
			print('Passo:\t',e[0],'\tanula',p[e[1]])

			xB = det.somar(xB, det.transposta(y)[0], -e[0])
			print(xB)
			
			xB[e[1]] = e[0]
			
			p[e[1]], q[k] = q[k], p[e[1]]
			cB[0][e[1]], cN[0][k] = cN[0][k], cB[0][e[1]] 

			yield 
		except KeyboardInterrupt:
			break 	
		except ValueError:
			print('Solução ilimitada')
			break

		B, N = particionar(A, p, q) 
	#	Bi = det.inversa(B) # atualizar inversa
	#	'''
		vl = Bi[e[1]]/y[e[1]][0]
	#	print(vl)
		for i in range(m):
			if i != e[1]:
				v = y[i][0] * vl
	#			print(v, Bi[i])
				Bi[i] -= v 					
		Bi[e[1]] = vl		

		l += cNr[k] * vl
	#	print('Inversa:\n',det.inversa(B))
	#	print('Inversa atualizada:\n',Bi)
	#	print('Multiplicador atualizado:\t',l)#'''
	x = [0] * n
	for k in range(len(p)):
		x[p[k]] = xB[k]
	yield det.transposta([x])		
simplex = primal	 

	





s = simplex([[2,1,1,0],[4,5,0,1]], [[5000],[15000]], [[-10,-7,0,0]])
s = simplex([[1,2,3,0],[2,1,5,0],[1,2,1,1]],[[15],[20],[10]],[[-1,-2,-3,0]])
s = simplex([[-4, 1, 1, 0], [2, -3, 0, 1]], [[4], [6]], [[-1, -2, 0, 0]])
s = simplex([[1,1,1,0,0],[1,-1,0,1,0],[-1,1,0,0,1]],[[6],[4],[4]],[[-1,-1,0,0,0]])	
while True:
	print(next(s))
	input()