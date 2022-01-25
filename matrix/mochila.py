
minuto = 60
hora = 60*minuto
tempo_limite = 2*hora
relogio = lambda t,m=minuto,h=hora: '%02.f:%02.f:%f'%((t//h),(t%h)//m,(t%h)%m)
import time,math,random

FALSO = lambda*args:None
limitante_superior = lambda maior_interesse,interesse_parcial,razao_prec,capac_resta: ((maior_interesse - interesse_parcial) > (razao_prec * capac_resta))
'''def limitante_superior (maior_interesse,interesse_parcial,razao_prec,capac_resta): 
	try:
		return maior_interesse <= interesse_parcial + (razao_prec*capac_resta)
	except TypeError:
		return maior_interesse == None'''


def gerar (t = True,n = 5,i = 10,f = 100):
		
	r = []
	w = []
	while t > 0:
		t -= 1
		f = i + n*(1+math.ceil(i*random.random()))
		g = range(i,f,math.ceil((f-i)/n))
		a = math.floor((f-i)/n)
		r.extend(g)
		w.append([[r.pop(int(len(r)*random.random())),a+i] for i in g])
	return w

def capacidade (o):
	c = 0
	m = None
	for i in o:
		c += i[1]
		try:
			if i[1] > m:
				m = i[1]
		except TypeError:
			m = i[1]	
	c /= 2	
	if c <= m:
		c += m		
	if c.is_integer:
		return int(c)
	return c

def por_preciosidade (o):
	for i in o:
		i.insert(0,i[0]/i[1])
	o.sort()
	o.reverse()
	for i in o:
		i.append(i.pop(0)) 
	#	caso já tivesse a preciosidade adicionada, ela será somente repetida

def melhor (limite, obj, ramo = None, otimizar_poda = False, otimizar_proporcao = True, limitante=FALSO,tempo_maximo=tempo_limite): # 
	'''obj é a lista de pares (interesse,peso), ramo é o ramo inicial (None para o mais alto)'''

	if limite == None:
		limite = capacidade(obj)
	
	print('\tCapacidade da mochila:',limite)
	if otimizar_proporcao:
		por_preciosidade(obj)
		print('\tItens otimizados por interesse/peso:',*obj)
	



	# começaremos colocando o máximo possível do primeiro
	if ramo == None or not len(ramo):
		ramo = [int(limite//obj[0][1])]   	
	c = a = n = 0	
	resta = limite	
	maior_v = menor_r = None
#	TESTE = open('testando.txt'.upper(),'w')
	while c < len(ramo):
		if ramo[c]:
			try:
				resta -= ramo[c]*obj[c][1]
				if resta >= 0:
					a = c				
			#	print(resta,ramo[c],c,a)
			except TypeError:
				pass
		c += 1 		
	
	print(ramo[:a+1],resta)
	while len(ramo) < len(obj):
		ramo.append(None)
	try:
		ti = time.time()
		while a >= 0:
			resta = limite 
			valor = 0
			c = a
			a += 1
			while c >= 0:
				if ramo[c]:
					resta -= ramo[c] * obj[c][1] # subtraindo do limite a quantidade vezes o peso do que já tem
					valor += ramo[c] * obj[c][0]
				c -= 1
			
			

			while a < len(ramo): 
				ramo[a] = int(resta // obj[a][1]) # adicionamos o máximo possível do próximo objeto
				if ramo[a]:
					resta %= obj[a][1] # e deixamos só o que sobra do que restava
					valor += obj[a][0] * ramo[a]
				a += 1

			try:
				if (maior_v == valor and resta > menor_r) or maior_v < valor:
					maior_v = valor
					menor_r = resta
					maior = list(ramo)
					print(relogio(time.time()-ti),'(%d)\tMaior até agora:'%n,valor,resta,ramo)
			#	elif menor_v >= valor:
				#	menor_v = valor
				#	menor = list(ramo)
				#	print('Menor até agora:',ramo,'(',valor,')')
			except TypeError:
				maior_v = valor
				menor_r = resta
				maior = list(ramo)
				print(valor,'\t',resta,'\t',ramo)
		#	print(ramo,file=TESTE)
				
				
				
			
			
			n += 1
			a -= 1# + otimizar_poda
			if otimizar_poda:
				valor -= ramo[a]*obj[a][0]
				resta += ramo[a]*obj[a][1]
				a -= 1
			while a >= 0: 
				if ramo[a] > 0: # ramo[a] < 0 não deve ser decrementado  e seu tratamento é indefinido		
					if time.time() - ti > tempo_maximo:
						print('\t\tTempo limite atingido.')
					else:
						try:							
						#	print(valor - obj[a][0],obj[a+1][2],resta,valor-obj[a][0]+(obj[a+1][2]*(resta + obj[a][1])))
							if limitante(maior_v,valor - obj[a][0],obj[a+1][2],resta + obj[a][1]):
								valor -= obj[a][0] * ramo[a]
								resta += obj[a][1] * ramo[a]
								
							#	print(a,'podado')
								a += -1 
								continue
						except IndexError:
							pass
						ramo[a] -= 1
						break
				a -= 1
		#	print('Finalizada a verificação de todos os ramos inferiores')
		#	break
	except KeyboardInterrupt:
		print('\t\tVerificação interrompida!')
	tf = time.time()
	
	print('\tÚltimo ramo testado:',ramo)
	print('\tVerificados',n,'ramos em',relogio(tf-ti))
	if ti < tf:
		print('\tMédia de',n/(tf-ti),'ramos por segundo =',minuto*n/(tf-ti),'por minuto =',hora*n/(tf-ti),'por hora.')
		if n:
			print((tf-ti)/n,'segundos por ramo, aproximadamente, então projetando',n*tempo_maximo/(tf-ti),'durante o tempo limite.')

	return maior_v,limite-menor_r,maior#, [menor_v,menor] # pode ocorrer NameError caso não tenha havido nenhuma execução completa






