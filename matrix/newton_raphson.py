

from matplotlib import pyplot
import numpy
import poli

steps_min = 5
steps_max = 10

step_white = steps_max - 1

def converge (p, d1p, d2p, x, min = steps_min, max = steps_max, met = poli.newton):

	d = 0
	for i in range(min):
		d_ = met(x,p,d1p,d2p)
		x -= d_	
		d_ = abs(d_)
		dif = abs(d - d_)
		d = d_
		
		
	x_ = x
	for i in range(min,max):
		x_ -= met(x,p,d1p,d2p)
		d_ = abs(x_ - x)		
		dif_ = abs(d_ - d) 		
		if dif_ > dif:
			return x_, False, i

		x = x_		
		d = d_
		dif = dif_			
	return x, True	


'''
a = numpy.array([[[0, 100, 200], [0, 50, 100], [0, 25, 50]], [[255, 144, 33], [121, 125, 127], [0, 1, 2]], [[1, 2, 3], [10, 20, 30], [100, 200, 300%255]]])

pyplot.imshow(a)
pyplot.show()
'''

polinomio = [-1,2,-4,8]
derivada_1 = poli.df(polinomio)
derivada_2 = poli.df(derivada_1)

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
		
		res = converge(polinomio, derivada_1, derivada_2, a + b)

		
		
		
		linha.append(preto if res[1] else ([numpy.uint8(255 * res[2] // step_white)]) * 3)

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
