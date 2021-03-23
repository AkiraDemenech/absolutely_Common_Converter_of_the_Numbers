print(end='distribuindo')
import matplotlib.pyplot as plot
print('....')

def combin (n=2,p=6,r=None):
	try:
		if r == None:
			r = [[]]
		if p.__iter__ != None:
			pass
	except AttributeError:
		p = range(1,p+1)
	
	while n > 0:
		n += -1
		c = len(r)
		while c > 0:
			c += -1
			v = r.pop(c)
			for i in p:
				try:
					l = list(v)
					l.append(i)
				except TypeError:
					l = v+i
				r.append(l)
#				print(l)
	
	return r

def dist (n=2,p=6,s=None):
	if s == None:
		try:
			s = (n*p)+1
		except TypeError:
			s = (n*(p.stop-1))+1
		s = [0]*s
	#	s = {}
	c = combin(n,p,[0])
	for v in c:
		try:
			s[v] += 1
		except KeyError:
			s[v] = 1
	return s,len(c)

def prob (n=2,p=6):
	try:
		if n.__iter__ != None:
			pass
	except AttributeError:
		n,p = dist(n,p)
	c = len(n)
	while c > 0:
		c -= 1
		n[c] /= p
	return n 
	
def somas (n):
	s = {(n,)}
	if n <= 1:
		return s
	s.add((n-1,1))
	a = n - 1
	while a > 1:
		a -= 1
		for c in somas(n - a):
			b = list(c)
			b.append(a)
			b.sort()
			b.reverse()
			s.add(tuple(b))
		#	print(b)
	return s
	
def quantidades_somas (n):
	qtd_s = {}
	for s in somas(n):
		if not len(s) in qtd_s:
			qtd_s[len(s)] = []
		qtd_s[len(s)].append(s)
	return qtd_s




total = 0
k = 5
q = quantidades_somas(12)
for b in range(k):
	q[b + 1].sort()
	print(b+1, len(q[b+1]))
	for c in q[b+1][::-1]:
		print(c)
		b = len(c)
		l = k
		local = 1
		repet = 1
		anterior = 0
		while b > 0:
			b -= 1
			if anterior == c[b]:
				r += 1
				repet *= r
				print('\t\tRepete',anterior,r,'vezes')
			else:
				r = 1
			local *= l
			l -= 1
			anterior = c[b]
		print('Soma',local,'dividida por',repet,'=',local/repet)
		total += local/repet
	print('\to total até aqui é de',total,'caixas diferentes')
try:
	while True:
		k += 1
		print('Ignorados',len(q[k]),'outros grupos de somas de',k,'números!')
except KeyError:
	print("FIm")

while True:
	try:
		print(eval(input('–—')))
	except KeyboardInterrupt:
		break
	except:
		continue
		
		

try:
	for c in range(1,10):
		p = prob(c)
		plot.plot(range(0,len(p)),p)
		print(c)
except KeyboardInterrupt:
	pass
plot.show()

#print(dist(2,r=[0]))
while True:
	p = eval(input('_'))
	print(p)
	if type(p) == tuple:
		p = p[0]
	x = range(int(p[0]==0),len(p))
	plot.plot(x,p[p[0]==0:])
	plot.show()
	print(x)
