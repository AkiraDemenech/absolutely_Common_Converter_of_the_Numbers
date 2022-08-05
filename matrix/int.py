import math#, numpy as np 

ajuda = lambda: print('''\tAJUDA:\nrn1,pn1\nrn2,pn2\nrn3,pn3\nrn4,pn4\nrn5,pn5
\n	edo(função(x, y), x0, y0, h, n) #dobra h e usa metade de n para runge-kutta 4

	é equivalente a:
	modif_euler (função(x, y), x0, y0, h, n) 
	runge_kutta_2 (função(x, y), x0, y0, h, n) 
	runge_kutta_4 (função(x, y), x0, y0, 2*h, n/2) 

	quadratura(função(x, y), xa,xb, ya,yb, rx,px, ry,py) # pesos e raízes opcionais (por padrão n = 4), e iguais em y se não for explícito\n''')

rn1 = [0]
pn1 = [2]

rn2 = [-0.57735, 0.57735]
pn2 = [1, 1]

rn3 = [-0.774597, 0, 0.774597]
pn3 = [0.555556, 0.888889, 0.555556]

rn4s = ['-0.86113631', '-0.33998104', '0.33998104', '0.86113631']
rn4 = [float(r) for r in rn4s]

pn4s = ['0.34785485', '0.65214515', '0.65214515', '0.34785485']
pn4 = [float(r) for r in pn4s]

rn5 = [-0.90618, -0.538469, 0 ,0.538469 ,0.90618]
pn5 = [-0.236927, -0.478629, 0.56888 , 0.478629, 0.236927]



def modif_euler (f, x, y, h, n = 5):

	while n > 0:

		n -= 1

		k1 = round(f(x, y), 6)
		k2 = round(f(x + (h / 2), y + round(k1 * h / 2, 6)), 6)
		
		print('\nx = %0.6f\ny = %0.6f\nk1 = %0.6f\nk2 = %0.6f\n' %(x.real, y.real, k1.real, k2.real))

		x += h
		y += round(h * k2, 6) 

	return y 

def runge_kutta_2 (f, x, y, h, n = 5):

	while n > 0:

		n -= 1

		k1 = round(f(x, y), 6)
		k2 = round(f(x + h, y + round(h * k1, 6)), 6)
		
		print('\nx = %0.6f\ny = %0.6f\nk1 = %0.6f\nk2 = %0.6f\n' %(x.real, y.real, k1.real, k2.real))

		x += h
		y += round(h * (k1 + k2) / 2, 6) 

	return y

def runge_kutta_4 (f, x, y, h, n = 5):

	while n > 0:

		n -= 1

		k1 = round(f(x, y), 6)
		k2 = round(f(x + (h / 2), y + round(k1 * h / 2, 6)), 6)
		k3 = round(f(x + (h / 2), y + round(k2 * h / 2, 6)), 6)
		k4 = round(f(x + h, y + round(k3 * h, 6)), 6)
		
		print('\nx = %.6f\ny = %.6f\nk1 = %.6f\nk2 = %.6f\nk3 = %.6f\nk4 = %.6f\n' %(x.real, y.real, k1.real, k2.real, k3.real, k4.real))

		x += h
		y += round(h * ((k1/2) + k2 + k3 + (k4/2)) / 3, 6) 

	return y

def edo (f, x, y, h, n):

	if type(f) == str:
		f = eval('lambda x,y:(' + f.lower().replace('^', '**') + ')') 

	print('Euler modificado: ',modif_euler(f,x,y,h,n).real,'\n')
	print('Runge-Kutta de 2a ordem: ',runge_kutta_2(f,x,y,h,n).real,'\n')
	print('Runge-Kutta de 4a ordem: ',runge_kutta_4(f,x,y,h*2,n/2).real,'\n')


nodos = lambda u, a, b: (((b-a)*u) + a + b) / 2 	
def quadratura (f, xa, xb, ya, yb, rx = rn4, wx = pn4, ry = None, wy = None):

	if type(f) == str:
		f = eval('lambda x,y:(' + f.lower().replace('^', '**') + ')') 


	ux = []
	uy = []
	print('\nRaízes transformadas:')
	if ry == None:
		ry = rx
	for r in rx:
		rx = round(nodos(r, xa, xb).real,6)
		ux.append(rx)

	for r in ry:	
		ry = round(nodos(r, ya, yb).real,6)				
		uy.append(ry)
				
	ux.sort()
	uy.sort()	

	for r in range(max(len(ux), len(uy))):
		
		if r < len(ux):
			print(end='%0.6f' %ux[r].real)
		else:
			print(end=' '*8)	
		print(end='\t')
		if r < len(uy):
			print(end='%0.6f' %uy[r].real)
		print()	

	print('\nf(x,y):')
	valores = []
	for x in ux:
		v = []
		valores.append(v)
		for y in uy:
			z = round(f(x,y).real,6)
			v.append(z)
		#	print(z, end=' ')
			print(end=' %0.6f ' %z)
		print(end='\n')		

	print('\nPesos multiplicados:')
	w = []
	if wy == None:
		wy = wx
	for px in wx:
		v = []
		w.append(v)
		for py in wy:
			p = round((px * py).real,6)
			v.append(p)
		#	print(p, end=' ')
			print(end=' %0.6f ' %p)
		print(end='\n')

	print('\nwwf(x,y):')	
	s = 0
	for i in range(len(wx)):
		for j in range(len(wy)):
			r = round((valores[i][j] * w[i][j]).real,6)
			s += r
		#	print(r, end=' ')
			print(end=' %0.6f ' %r)		
		print(end='\n')	
	
	return (s * (xb - xa) * (yb - ya)).real / 4 	




while __name__ == '__main__':
	try:
		linha = input('\\$')
		try:
			res = eval(linha)			
		except SyntaxError:
			r = exec(linha)
			if r == None:
				continue
			print('RES =', r)
			res = r
				
		else:
			print('RES='+(repr(res) if type(res) == str else str(res)))		
	except KeyboardInterrupt:
		break
	except Exception as e:
		print('ERRO:',e)
		err = e