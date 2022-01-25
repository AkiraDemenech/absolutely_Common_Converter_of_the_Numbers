
def arvore (limite, obj, otimizar_poda = True, otimizar_interesse = True, otimizar_por_peso = True): # obj é a lista de pares (interesse,peso)

	if otimizar_interesse:
		if otimizar_por_peso:
			for o in obj:
				o.insert(0,o[0]/o[1])
		obj.sort()
		obj.reverse()
		if otimizar_por_peso:
			for o in obj:
				o.pop(0)

	# começaremos colocando o máximo possível do primeiro
	ramos = [[limite//obj[0][1]]]   
	a = b = 0
	c = not b
	while c != b:
		resta = limite 
	#	valor = 0
		c = a
		while c >= 0:
			resta -= ramos[b][c] * obj[c][1] # subtraindo do limite a quantidade vezes o peso do que já tem
		#	valor += ramos[b][c] * obj[c][0]
			c -= 1

		while len(ramos[b]) < len(obj):
			ramos[b].append(resta//obj[len(ramos[b])][1]) # adicionamos o máximo possível do próximo objeto
			resta %= obj[len(ramos[b])-1][1] # e deixamos só o que sobra do que restava
		#	valor += obj[len(ramos[b])-1][0] * ramos[len(ramos[b])-1]
			
			
		c = b
		a = len(ramos[b]) - otimizar_poda
		while a > 0: 
			a -= 1
			if ramos[b][a] > 0:
				ramos.append(ramos[b][:a])
				ramos[len(ramos) - 1].append(ramos[b][a] - 1)
				b += 1
				break

	return ramos


def interesse (qtd, obj):
	total = 0
	c = len(obj)
	if len(qtd) < c:
		c = len(qtd)
	while c > 0:
		c += -1
		total += qtd[c]*obj[c][0]
	return total

'''
#for r in arvore(210, [[52,35], [51,50], [50,41], [49,20], [48,41]]): print(r);
b = [[52,35], [51,50], [50,41], [49,20], [48,41]]#[[5,14],[15,44],[14,36],[10,24]]#[[1,5],[2,4],[3,3]]#[[19,29], [29,39], [9,49], [39,59], [43,69]]#
a = arvore(210,b)
maior = 0,0
for r in a: 	print(a.index(r),interesse(r,b),'\t',r);
for r in a:
	i = a.index(r), interesse(r,b) 
	if i[1] > maior[1]:
		maior = i
	print(*i,'\t',r, end=['\n','\tMaior até agora\n'][i == maior])
print(len(a))#print(len(arvore(210, [[52,35], [51,50], [50,41], [49,20], [48,41]])))
print("Maior: ",maior)
'''

from matplotlib.pyplot import show
from networkx import draw, Graph


svg_raio = 20
svg_dist = 5*svg_raio
svg_escala = 3*svg_raio
svg_margens = 15

svg_coord = lambda x, y: (svg_margens + (svg_dist * x), (y * svg_escala) + svg_margens)

svg_circle = lambda x,y:	'<circle cx="%f" cy="%f" r="%f" \tfill="%s" />' %(svg_coord(x, y) + (svg_raio,"blue"))
svg_line = lambda p,q:	'<line\t x1="%f" y1="%f" x2="%f" y2="%f" \tstroke="black" stroke-width="4"/>' %(svg_coord(*p) + svg_coord(*q))
svg_label = lambda p,t:	'<text\t x="%f" y="%f" \tfill="black">' %svg_coord(*p) + t + '</text>' 

label = lambda n,i, l: 'x_%d = %d [%s]' %(i,n,chr(ord('A')+l))

def grafo (arv, raiz='.', svg=None):
	

	linhas = []
	legenda = []
	bolas = []

	galho = [(0,(1+len(arv))/2)]*(1+len(arv[0]))
	
	g = Graph()
	g.add_node(raiz)
	h = (None,)*len(arv[0])
	s = list(h)#[label(arv[0][c],c+1) for c in range(len(arv[0]))]
	t = -1
	for r in arv:
		a = raiz
		c = 0
		while r[c] == h[c]:
			a = s[c]
			c += 1
		t += 1
		while c < len(r):
			b = label(r[c],c+1,t)
			'''if s[c] != b:
				b += ' [%x]' %t
				if s[c] != b:
					i = c
					t += 1
					b = label(r[c],c + 1) + ' [%x]' %t
					while i < len(s):
						s[i] = b
						i += 1'''
			galho[c+1] = (c+1,t+1)
			legenda.append((galho[c+1],b[:b.find('[')]))	# ((x,y),label)
			bolas.append(galho[c+1])	# (x, y)
			linhas.append((galho[c],galho[c+1]))	# ((z, w), (x,y))
			g.add_edge(a, b)
			s[c] = a = b
			c += 1
		h = r
	
	if svg != None:
		if type(svg) == str:
			svg = open(svg,'w')
		print('<svg\t xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" \tid="body">',file=svg)

		global svg_dist
		svg_dist = svg_escala*len(arv)/len(arv[0])

		for l in linhas:
			print('\t',svg_line(*l),file=svg)
		for c in bolas:
			print('\t',svg_circle(*c),file=svg)
		for l in legenda:
			print('\t',svg_label(*l),file=svg)

		print('</svg>',file=svg)

	return g
#draw(grafo(a,svg="tree.svg"),with_labels=True)
#show()


