

from matplotlib import pyplot
import numpy
import poli

def converge (p, x, min = 5, max = 10, met = poli.newton_raphson):

	x = met(p,x,min)
	d = 0
	dif = None

	for i in range(min,max):
		x_ = met(p,x,1)
		d_ = abs(x_ - x)		
		dif_ = abs(d_ - d) 		
		if dif != None and dif_ > dif:
			return x_, False, i

		x = x_		
		dif = dif_	
	return x, True	


'''

'''

polinomio = [10,20,30]

a_max = 2 * poli.fujiwara(polinomio)
b_max = a_max * 1j
b_min = -b_max
a_min = -a_max

px_d = 4096 # largura (diâmetro) da imagem, em pixels 
a_step = poli.racional.frac(2 * a_max, px_d).real
b_step = a_step * 1j
# unidades por pixel

print('Diâmetro de Fujiwara:\t',a_max)
print('Resolução (px):\t',px_d)
print(a_step, '/ 1px')

preto = [numpy.uint8(0)] * 3

c = []

b = b_min
while len(c) < px_d:
	linha = []
	c.append(linha)
#	print(len(c), b)

	a = a_min
	while a <= a_max:
		

	#	z = 
		
		res = converge(polinomio, a + b)

		
		
		
		linha.append(preto if res[1] else ([numpy.uint8(255 * res[2] // 9)]) * 3)

		a += a_step
	b += b_step



c = numpy.array(c)

pyplot.imshow(c)
pyplot.show()

from PIL import Image
nome = sinal = ''
for a in polinomio:
	if a > 0:
		nome += sinal
	nome += str(a)
	sinal = '+'
nome += '_' + str(px_d) + '.png'	
print(nome)
Image.fromarray(c).save(nome)
