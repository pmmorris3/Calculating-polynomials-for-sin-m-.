import math
import operator
import sys
from math import log
from math import exp
from decimal import *
getcontext().prec = 60

Pi = Decimal(3.14159265359)
def binomial(n, k):
    def eratosthenes_simple_numbers(N):
        yield 2
        nonsimp = set()
        for i in range(3, N + 1, 2):
            if i not in nonsimp:
                nonsimp |= {j for j in range(i * i, N + 1, 2 * i)}
                yield i
    def calc_pow_in_factorial(a, p):
        res = 0
        while a:
            a //= p
            res += a
        return res
    ans = 1
    for p in eratosthenes_simple_numbers(n):
        ans *= p ** (calc_pow_in_factorial(n, p) - calc_pow_in_factorial(k, p) - calc_pow_in_factorial(n - k, p))
    return ans
def polyval(x, coef):
    sum = Decimal(0)
    count = 0
    while 1:
        sum = sum + coef[0]     
        coef = coef[1:]         
        if not coef: break      
        sum = sum * x           

    return sum

class Sine:
	def __init__(self, power,arg,coeff):
		self.power = power
		self.arg = arg
		self.coeff = coeff
class Poly:
	def __init__(self,m):
		self.m = m

	def generatePolynomial(self):
		listOfSines = []
		condensedSines = []
		for n in range(0,(90)//2+1):
			for j in range(0,n+1):
				z = complex(0,1) ** (90 - 2*n)
				summand = Sine(Decimal(90+2*j-2*n),(self.m*Pi/180), Decimal(int(z.real)*binomial(90,2*n)* binomial(n,j) * (-1)**j))
				listOfSines.append(summand)
		listOfSines.sort(key=operator.attrgetter('power'))

		for n in range(0,90 + 1):
			if n % 2 == 0:
				newSine = Sine(Decimal(n),self.m*Pi/180,(0))
				for x in listOfSines:
					if x.power == n:
						newSine.coeff += x.coeff

				condensedSines.append(newSine)
		return condensedSines
	def printPolynomial(self):
		summands = self.generatePolynomial()
		if self.m % 180== 0:
			print("sin(%d°) = 0 is clearly algebraic." % self.m)

		if self.m %4 ==2 :
			for x in summands:
				if x.power == 0:
					print("2", " ")
				elif x.coeff == 1:
					print("+ %dsin(%d°)^%d" % (x.coeff,self.m, x.power), " ")

				elif x.coeff < 0:
					print("- %d*sin(%d°)^%d" %(-x.coeff,self.m, x.power),  " ")
				else:
					print("+ %d*sin(%d°)^%d" %(x.coeff,self.m, x.power),  " ")
		if self.m %4 ==0 and self.m % 180 != 0:
			for x in summands:
				if x.power == 0:
					continue
				elif x.coeff == 1:
					print("+ %dsin(%d°)^%d" % (x.coeff,self.m, x.power), " ")

				elif x.coeff < 0:
					print("- %d*sin(%d°)^%d" %(-x.coeff,self.m, x.power),  " ")
				else:
					print("+ %d*sin(%d°)^%d" %(x.coeff,self.m, x.power),  " ")
		if self.m %4 ==3 or (self.m % 4 == 1 and self.m != 1):
			for x in summands:
				if x.power == 0:
					print("1", " ")
				elif x.coeff == 1:
					print("+ %dsin(%d°)^%d" % (x.coeff,self.m, x.power), " ")

				elif x.coeff < 0:
					print("- %d*sin(%d°)^%d" %(-x.coeff,self.m, x.power),  " ")
				else:
					print("+ %d*sin(%d°)^%d" %(x.coeff,self.m, x.power),  " ")

		if self.m == 1:
			for x in summands:
				if x.power == 0:
					print("1", " ")
				elif x.coeff == 1:
					print("+ %dsin(1°)^%d" % (x.coeff, x.power), " ")

				elif x.coeff < 0:
					print("- %d*sin(1°)^%d" %(-x.coeff, x.power),  " ")
				else:
					print("+ %d*sin(1°)^%d" %(x.coeff, x.power),  " ")

	def evaluatePolynomial(self):
		summands = self.generatePolynomial()
		summands.sort(key=operator.attrgetter('power'))
		coeff = []
		n = 90
		while n >= 0:
			if n % 2 == 0:
				coeff.append(Decimal(summands[n//2].coeff))
			else:
				coeff.append(0)
			n -= 1
		if self.m % 4 == 2:
			return polyval(Decimal(math.sin(self.m * Pi/180)), coeff) + 1
		if self.m % 4 == 0:
			return polyval(Decimal(math.sin(self.m * Pi/180)), coeff) - 1
		else:
			return polyval(Decimal(math.sin(self.m * Pi/180)), coeff)





stop = " "
while (stop.lower() != "no" ):
	stop = " "
	print("We claim sin(m°) is an algebraic number, whenever m  is an integer. Choose an m, and we will exhibit a polynomial over the rationals which sin(m°) satisfies.")
	degrees_in=input("Enter an integer for m: ")
	while (degrees_in.isnumeric() == 0):
		if (degrees_in[0] in {'+','-'} and degrees_in[1::].isnumeric() == 1):
			break
		else:
			degrees_in=input("Enter an integer for m: ")
	print("\n"*100)

	degrees_in = int(degrees_in)
	if degrees_in >= 0:
		degrees = degrees_in % 360
	if degrees_in < 0:
		degrees = degrees_in % -360
	p_m = Poly(degrees)
	p_m.printPolynomial()
	sum = p_m.evaluatePolynomial()
	if degrees %180 != 0:
		print("\n","Your computer approximates this as: \n",sum)

	stop = input("Would you like to try another? Enter yes or no: ")
	if stop != "no":
		while (stop.lower() != "yes"):
			stop = input("Would you like to try another? Enter yes or no: ")
			if stop == "no":
				break
	print("\n"*100)

print("It turns out one needs only three distinct polynomials, depending on the remainder upon division of m by 4.")
print("Curiously, in the case m % 4 == 1,3, the corresponding polynomial only has roots of the form sin(m°), each of multiplicity 1.")
print("In other cases, there are an additional 24 (possibly degenerate) roots which need not be of this form.")
