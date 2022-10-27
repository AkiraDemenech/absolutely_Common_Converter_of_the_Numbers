def alpha_freq_count (text):
	alpha = {}

	for s in text:
		if not s in alpha:
			alpha[s] = 0
		alpha[s] += 1	

	return alpha

def huffman (alpha_freq, base = 2):

	forest = {alpha_freq[a]: [] for a in alpha_freq}
	for a in alpha_freq: 
		forest[alpha_freq[a]].append(a)
	print('Frequências: [símbolos]\n\t',forest)	

	while len(forest) > 1:

		f = 0	
		alpha = subtree = []		

		while len(subtree) < base and len(forest) > 0:
			while not len(alpha):
				freq = min(forest)
				alpha = forest.pop(freq)

			subtree.append(alpha.pop())	
			f += freq

		if len(alpha):	
			forest[freq] = alpha

		if not f in forest:	
			forest[f] = []
		forest[f].append(subtree)	
		print('\n\t',forest)

	tree = forest[f].pop()	
	print('Árvore:\t', tree)
	return tree

def show_tree (tree, prefix = (), map = {}):	

	for i in range(len(tree)):

		code = prefix + (i,)

		if type(tree[i]) == list:
			show_tree(tree[i], code, map)
		else:	
			print(*code,'\t',repr(tree[i]))
			map[code] = tree[i]
			map[tree[i]] = code

	return map		

#contagem = {'b': 1, 'c': 6, 'a': 5, 'd': 3}
contagem = {'e': 4, 'a': 4, ' ': 7, 'n': 2, 't': 2, 'm': 2, 'i': 2, 'h': 2, 's': 2, 'f': 3, 'o': 1, 'u': 1, 'x': 1, 'p': 1, 'r': 1, 'l': 1}
arvores = {}
mapas = {}
melhoria = 0
for n in range(2, len(contagem) + 1):
	print('\n\tBase/ordem',n)
	arvores[n] = huffman(contagem, n)
	mapas[n] = {}
	show_tree(arvores[n], map = mapas[n])

tabela = {}
for n in arvores:	
	fixo = 1
	while n**fixo < len(contagem):
		fixo += 1
	print('\n\nBase/ordem',n)	

	fdt = sum(fixo * contagem[a] for a in contagem)
	vdt = sum(len(mapas[n][a]) * contagem[a] for a in contagem)
	vds = {len(mapas[n][a]) for a in mapas[n]}
	m = 100 * (1 - (vdt / fdt))
	melhoria = max(melhoria, m)
	tabela[n] = fixo, fdt, vds, vdt, m
	
	print('Fixo:\n\t',fixo,'dígitos por símbolo')
	print('\t', fdt, 'dígitos totais')

	print('\nVariável:\n\t', vds, 'dígitos por símbolo')
	print('\t', vdt, 'dígitos totais')
	print(m,'% melhor')
	
	if m == melhoria:
		print('Melhor até agora')
	
print(contagem, len(contagem))

for n in tabela:
	print(n, *tabela[n], 'Melhor' if tabela[n][-1] == melhoria else '', sep='  \t')