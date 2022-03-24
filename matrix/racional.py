
import muldiv

to_int = lambda x: x if type(x) == float and not x.is_integer() else int(x)

class frac:

	def is_integer (self):
		return False

	def as_integer_ratio (self):
		return self.num, self.den

	def __init__ (self, n, d = True):	
		if type(n) == frac:
			d *= n.den
			n = n.num

		

		if type(n) != float or n.is_integer():	
			if n == None:
				n = False
			n = int(n)
		else:	
			a, b = n.as_integer_ratio()
			n = a
			d *= b

		if type(d) != float or d.is_integer():	
			if d == None:
				d = True
			d = int(d)
		else:	
			a, b = d.as_integer_ratio()
			d = a
			n *= b	

		if d < 0:
			n = -n
			d = -d	

		s = muldiv.mdc(n, d, v = False) 
		if s > 1:
			n //= s
			d //= s

		self.numerator = self.num = n
		self.denominator = self.den = d
		if d != 0:
			self.real = n
			if d > 1:
				self.real /= d
			self.imag = self.real.imag # se não for 0, complex teria causado erro em comparações e conversões anteriores já

	def __abs__ (self):
		return self.real.__abs__()
	
	def __add__ (self, parcela):	
		parcela = frac(parcela)
		d = muldiv.mmc(parcela.den, self.den, v = False)
		return frac((d * self.num // self.den) + (parcela.num * d // parcela.den), d)
		

	def __mul__ (self, fator):	
		fator = frac(fator)
		return frac(self.num * fator.num, fator.den * self.den)

	def __truediv__ (self, divisor):	
		return self * (~frac(divisor))

	def __rtruediv__ (self, dividendo):	 	
		return self.__invert__() * dividendo 

	def __sub__ (self, subtraendo):	
		return self + (-subtraendo)

	def __rsub__ (self, minuendo):	
		return minuendo + self.__neg__()

	def __radd__ (self, parcela):	
		return self.__add__(parcela)

	def __rmul__ (self, fator):
		return self.__mul__(fator)	

	def __rpow__ (self, base):	
		return base ** self.real

	def __pow__ (self, expoente):		
		s = self
		if expoente < 0:
			expoente = -expoente
			s = self.__invert__()
		return frac(s.num ** expoente, s.den ** expoente)

	def __pos__ (self):	
		return self

	def __invert__ (self):	
		return frac(self.den, self.num)

	def __neg__ (self):	
		return frac(-self.num, self.den)	

	def __ne__ (self, x):	
		return not self.__eq__(x)

	def __eq__ (self, x):	
		if type(x) == frac:
			x = x.real
		return self.real == x		

	def __gt__ (self, x):	
		if type(x) == frac:
			x = x.real
		return self.real > x

	def __lt__ (self, x):			
		return self.__le__(x) and self.__ne__(x)	

	def __le__ (self, x):	
		return not self.__gt__(x)

	def __ge__ (self, x):	
		return not self.__lt__(x)	

	def __str__ (self):	
		return f'{self.num}' + (f'/{self.den}' * (self.den != 1))

	def __repr__ (self):	
		return f'frac({self.num}' + (f', {self.den}' * (self.den != 1)) + ')'

	def __bool__ (self):
		return self.num != 0

	def __hash__ (self):	
		return self.real.__hash__()