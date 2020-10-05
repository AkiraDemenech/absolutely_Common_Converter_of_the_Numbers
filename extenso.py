from convert import *

sinal = 'menos','negativo','negative','minus','less'
div = 'vírgula','virgula','ponto','point','dot'
milhar = 'mil','milhar','thousand'
centena = 'hundred','centos','centenas','centena'
numerais = {1:{1: ('um','one'), 2: ('dois','two'), 3: ('três','tres','three'), 4:('quatro','four'), 5: ('cinco','five'), 
6: ('seis','six'), 7:('sete','seven'), 8: ('oito','eight'), 9: ('nove','nine'), 10: ('dez','ten'), 
11:('onze','eleven','endleofan'), 12:('doze','twelve','twelf'), 13:('treze','thirteen'), 14:('catorze','quatorze','qüatorze','fourteen'),
15:('quinze','fifteen'), 16:('dezesseis','sixteen'), 17:('dezessete','seventeen'), 18:('dezoito','eighteen'),
19:('dezenove','nineteen'), 20:('vinte','twenty'),30:('trinta','thirty'),40:('quarenta','forty'),50:('cinquenta','cinqüenta','cincoenta','fifty'),
60:('sessenta','sixty'),70:('setenta','seventy'),80:('oitenta','eighty'),90:('noventa','ninety'),100:('cem',),},
100:{1:'cento',2:'duzentos',3:'trezentos',4:'quatrocentos',5:'quinhentos',6:'seiscentos',7:'setecentos',8:'oitocentos',9:'novecentos'}}
valores = {'zero':0}
for d in numerais:
	for n in numerais[d]:
		if type(numerais[d][n]) == str:
			valores[numerais[d][n]] = d*n
		else:
			for s in numerais[d][n]:
				valores[s] = d*n
				
#numerais = {int:numerais,str:valores}
#numerais[1].update(valores)

def extenso (n=0,sep=' ',adic='e',frac=div,neg=sinal,mil=milhar,ummil=False,notteens=False,escolha=lambda pos:pos[0]):
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
					if n in mil:
						if t == 0:
							t = 1
						r += 1000*t
						t = 0
					elif n in centena:
						t *= 100
					elif n in neg:
						inv = not inv
					elif n in div:
						r += t
						f = r
						r = t = d #caso d != 0, haverá bug
						d = 1
			#		else: 
			#			print(n)
					continue
			if n == 0:
				d *= 10
			else:
				t += n
		r += t
		try:
			dec = d/d
			while r/dec >= 1:
				dec *= 10
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
	
	if n >= 1000:
		if ummil or n >= 2000:
			r += extenso(n//1000,sep,adic,frac,neg,mil,ummil,notteens,escolha) + sep
		r += escolha(mil) + sep	
		n = n%1000
		if n%100 < 1 or n < 100:
			r += adic + sep
	
	if n > 100:
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
	n -= n//1
	while n%1 > 0:
		n *= 10
		
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