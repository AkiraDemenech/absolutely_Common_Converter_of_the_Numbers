mul = '·'
ast = "*"

def matriz (x = 4, y = None, e = lambda s='': eval(input(s)), r = None, v = 0):
	if y == None:
		y = x
	if r == None:
		r = []
	while len(r) < y:
		r.append([])
	j = 0
	while j < y:
		i = 0
		while len(r[j]) < x:
			r[j].append(v)
		while i < x:
			r[j][i] = e()
			i += 1
		j += 1
	return r

def det (m, s = mul):
	d = c = ''
	n = len(m)
	r = a = 0
	while a < n:
		c += '+'
		d += ' + '
		
		t = 1
		b = 0
		while b < n:
			if m[b][(a+b)%n] < 0:
				v = '(%d)'%m[b][(a+b)%n]
				d += v
			else:
				v = str(m[b][(a+b)%n])
				if b > 0:
					d += s
				d += v
			t *= m[b][(a+b)%n]
			if b > 0:
				c += '*'
			c += v
			b += 1
		r += t
		a += 1
	
	while a > 0:
		a -= 1
		c += '-'
		d += ' %s ' %chr(8211)
		
		b = 0
		t = 1
		while b < n:
			t *= m[b][(a-b)%n]
			if m[b][(a-b)%n] < 0:
				v = '(%d)'%m[b][(a-b)%n]
				d += v
			else:
				v = str(m[b][(a-b)%n])
				if b > 0:
					d += s
				d += v
			if b > 0:
				c += '*'
			c += v
			b += 1
		r -= t
		
	return r, c, d