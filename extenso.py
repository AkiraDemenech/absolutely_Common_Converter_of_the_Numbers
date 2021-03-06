from convert import *

zero = 'zero'
sinal = 'menos','negativo','negative','minus','less'
div = 'vírgula','virgula','ponto','point','dot'
curta = 'milhão','milhões','milioes','milhao','million','millions'
milhar = 'mil','milhar','thousand'
centena = 'hundred','centos','centenas','centena'
numerais = {1:{1: ('um','one'), 2: ('dois','two'), 3: ('três','tres','three'), 4:('quatro','four'), 5: ('cinco','five'), 
6: ('seis','six'), 7:('sete','seven'), 8: ('oito','eight'), 9: ('nove','nine'), 10: ('dez','ten'), 
11:('onze','eleven','endleofan'), 12:('doze','twelve','twelf'), 13:('treze','thirteen'), 14:('catorze','quatorze','qüatorze','fourteen'),
15:('quinze','fifteen'), 16:('dezesseis','sixteen'), 17:('dezessete','seventeen'), 18:('dezoito','eighteen'),
19:('dezenove','nineteen'), 20:('vinte','twenty'),30:('trinta','thirty'),40:('quarenta','forty'),50:('cinquenta','cinqüenta','cincoenta','fifty'),
60:('sessenta','sixty'),70:('setenta','seventy'),80:('oitenta','eighty'),90:('noventa','ninety'),100:('cem',),},
100:{1:'cento',2:'duzentos',3:'trezentos',4:'quatrocentos',5:'quinhentos',6:'seiscentos',7:'setecentos',8:'oitocentos',9:'novecentos'}}
valores = {zero:0}
for d in numerais:
	for n in numerais[d]:
		if type(numerais[d][n]) == str:
			valores[numerais[d][n]] = d*n
		else:
			for s in numerais[d][n]:
				valores[s] = d*n
				
#numerais = {int:numerais,str:valores}
#numerais[1].update(valores)

def escala (n,d = 1,b = 10):
	if d == 0:
		return 1
	while n >= d:
		d *= b
	return d

def extenso (n=0,sep=' ',adic='e',frac=div,neg=sinal,mil=(milhar,curta),ummil=False,notteens=False,escolha=lambda pos:pos[0]):
	if type(n) == str:
		f = t = r = 0
		d = 0
		inv = False
		for n in n.lower().split():
			try:
				n = valores[n]
			except KeyError:
				try:
					n = eval(n,valores)
				except Exception:				
					if n in centena:
						if t == 0:
							t = 1
						t *= 100
					elif n in neg:
						inv = not inv
					elif n in div:
						r += t
						f += r
						r = t = 0 # caso já houvesse um ponto anterior, ele seria considerado mero caractere de formatação
						d = 1
					else: 
						m = len(mil)
						while m > 0:
							m -= 1
							if n in mil[m]:
								if m == 0:
									if t == 0:
										t = 1	# mil = um mil
								else:
									r *= 1000**(m+1)
								r += (1000**(m+1))*t	# mil mil = mil + mil, não se multiplica multiplicadores
								t = m = 0
					continue
			if n == r == t == 0:
				d *= 10
			t += n
		r += t
		try:
			dec = escala(r,d/d)
		except ZeroDivisionError:
			d = dec = 1
		r = f + r/(d*dec)
		if inv:
			return -r
		return r
		
	if n < 0:
		n = -n
		r = escolha(neg) + sep
	else:
		r = ''
	m = len(mil)
	while m > 0:
		if n >= 1000**m:
			if ummil or n >= 2000:
				r += extenso(n//(1000**m),sep,adic,frac,neg,mil,ummil,notteens,escolha) + sep
			r += escolha(mil[m-1][(m>1)*(n//(1000**m) != 1):])  	
			n = n%(1000**m)
			if n >= 1:
				r += sep
				if n%(10**(2*m-(m%2))) < 1 or n < 10**(2*m - (m%2)):
					r += adic + sep
		m -= 1
	
	if int(n) > 100:
		r += numerais[100][n//100]
		n = n%100
		if n >= 1:
			r += sep + adic + sep
		
	try:
		if notteens:
			raise KeyError()
		r += escolha(numerais[1][n//1])
	except KeyError:
		if n >= 1:
			r += escolha(numerais[1][(n//10)*10]) + sep + adic + sep + escolha(numerais[1][int(n%10)])
	d = 0
	n -= n//1
	while n%1 > 0:
		n *= 10
		d += 1
	d = 10**(d - 1)
	if n > 0:
		if len(r) == 0:
			r = zero
		r += sep + escolha(div)
		while d > n:
			d /= 10
			r += sep + zero
		r += sep + extenso(n)
	return r
	

while __name__ == "__main__":
	ln = input('>>')
	try:	
		print(eval(ln))
	except KeyboardInterrupt:
		print('<<')
		break
#	except SyntaxError:
#		print(exec(ln))
	except Exception as ex:
		print(extenso(ln),"\n",ex)