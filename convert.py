#-*-coding:utf-8;-*-
#dig = '0123456789abcdefghijklmnopqrstuvwxyz'
from string import digits, ascii_uppercase
dig = digits + ascii_uppercase
def convert (n, b=None, d=dig.lower(), p='.', neg='-'):
	
	b0 = 10
	if type(n) in (tuple,list):
		if len(n) > 2 and b == None:
			b  = n[2]
		if len(n) > 1:
			b0 = n[1]
		#else:
		n = str(n[0]).lower()
		
	if type(n) == str:
	#    m = 1
		c = e = 0
		"""if neg in n:
			m = -1"""
		for a in n.replace(neg,""):
			if a == p:
				e = 1
				continue
			e *= b0
			c *= b0
			c += d.find(a)#*m
		if neg in n:
			c *= -1#= -c
		n = c
		if e != 0:
			n /= e
	
	if b == 10:
		return n
	if b == None:
		b = 2
	elif b == 1:
		return d[1]*n#int(n)
	c = ''
	a = 1
	if n < 0:
		c = neg#'-'
		n = -n
	while a < n:
		a *= b
	while n > 0 or a >= 1:
		if a == 1/b:
			c += p#'.'        
		"""if n < a:
			c += '0'
		else:
			c += '1'
			n -= a"""
		#    print (' -',a)
		#c += d[int(n<a)]
		e = b
		while e > 0:
			e -= 1
			if e*a <= n:
				n -= e*a
				c += d[e]
				e = 0
		a /= b
		if a == 0:
			break
	return c

def bcd (n,d=10):
	if type(n) == str:
		c = b = 0
		n = dig[0]*((4-(len(n)%4))%4) + n
		while c < len(n):
			b = b*10 + convert((n[c:c+4],2,10))
			c += 4
		return b
	
	b = ''
	for c in str(n):
		b += '%04d' %int(convert((c,d)))
	return b

def rbc (n,to=False,at=2):
	if at != 2:
		n = convert((n,at))
	elif type(n) != str:
		n = str(n)
	r = n[0]
	b = n
	c = 1
	while c < len(n):
		if not to:
			b = r
		r += dig[int(n[c]!=b[c-1])]
		c += 1
	return r

def gray (l=0,d=dig):
	g = list(d[:2])
	while l > 0:
		c = len(g)
		while c > 0:
			c += -1
			g.append(d[1] + g[c])
			g[c] = d[0] + g[c]
		l -= 1
	return g

def parity (n, test=0, count=1, b=2, add=dig):
	n = str(n)
	return add[int(n.count(str(count))%b!=test)] + n

def check (n, test=0, count=1, b=2, get=dig):
	n = str(n)
	return n[0] == get[int(n[1:].count(str(count))%b!=test)]

romans = 'mdclxvi'
to_roman = {}
from_roman = {}
n,m = 2,5
b = 1000
for a in romans:
	to_roman[b] = a.upper()
	b //= n
	n,m=m,n
for a in to_roman:
	from_roman[to_roman[a]] = a
from_roman.update(
	{
		'Z':2000,'Q':500,'P':400,'B':300,'E':250,'H':200,'T':160,'Y':150,'R':80,'F':40,'O':11
	}	#A, Ϛ, S, N, K
)
romans = list(to_roman)
romans.sort()
#print(romans,to_roman,from_roman)

def roman (n,addonly=False):
	if type(n) == str:
		d = b = a = 0
		for c in n.upper():
			if from_roman[c] != a:
				if from_roman[c] < a:
					d += b
					b = 0
				elif from_roman[c] > a:
					b = -b
				a = from_roman[c]
			b += from_roman[c]
		return d + b

	r = ''
	p = len(romans) - 1
	while n > 0:
		while n >= romans[p]:
			r += to_roman[romans[p]]
			n -= romans[p]
		if n >= romans[p] - romans[p+(p%2)-2] and not addonly:
			r += to_roman[romans[p+(p%2)-2]] + to_roman[romans[p]]
			n += romans[p+(p%2)-2] - romans[p]
		p -= 1
	return r

try:
	while True:
		print(eval(input('>>>')))
	#	print(" =",bcd(x))
	#	print(" =",convert(x),"=",convert(x,4),"=",convert(x,8),"=",convert(x,16))
except Exception:
	print("<<<")