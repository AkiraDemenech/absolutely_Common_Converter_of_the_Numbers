import matplotlib.pyplot as plot

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
