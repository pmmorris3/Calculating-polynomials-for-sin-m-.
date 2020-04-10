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


class Sine:
	def __init__(self, power,arg,coeff):
		self.power = power
		self.arg = arg
		self.coeff = coeff



print("We claim sin(m°) is an algebraic number, whenever m  is an integer. Choose an m, and we will exhibit a polynomial over the rationals which sin(m°) satisfies.")
m_in=int(input("Enter an integer for m: "))
if m_in >= 0:
	m = m_in % 360
if m_in < 0:
	m = m_in % -360
listOfSines = []
condensedSines = []
for n in range(0,(90)//2+1):
		for j in range(0,n+1):
			z = complex(0,1) ** (90 - 2*n)
			summand = Sine(Decimal(90+2*j-2*n),(m*Pi/180), Decimal(int(z.real)*binomial(90,2*n)* binomial(n,j) * (-1)**j))
			listOfSines.append(summand)
listOfSines.sort(key=operator.attrgetter('power'))

for n in range(0,90 + 1):
	if n % 2 == 0:
		newSine = Sine(Decimal(n),m*Pi/180,(0))
		for x in listOfSines:
			if x.power == n:
				newSine.coeff += x.coeff

		condensedSines.append(newSine)

sum = Decimal(0.0)

if m== 0:
	print("sin(%d°) = 0 is clearly algebraic." % m_in)
	sys.exit(0)

if m %4 ==2 :
	for x in condensedSines:
		if x.power == 0:
			print("2", " ")
		elif x.coeff == 1:
			print("+ %dsin(%d°)^%d" % (x.coeff,m, x.power), " ")

		elif x.coeff < 0:
			print("- %d*sin(%d°)^%d" %(-x.coeff,m, x.power),  " ")
		else:
			print("+ %d*sin(%d°)^%d" %(x.coeff,m, x.power),  " ")
		sum += x.coeff*(Decimal(math.sin(x.arg)) ** Decimal(x.power))
if m %4 ==0:
	for x in condensedSines:
		if x.power == 0:
			continue
		elif x.coeff == 1:
			print("+ %dsin(%d°)^%d" % (x.coeff,m, x.power), " ")

		elif x.coeff < 0:
			print("- %d*sin(%d°)^%d" %(-x.coeff,m, x.power),  " ")
		else:
			print("+ %d*sin(%d°)^%d" %(x.coeff,m, x.power),  " ")
		sum += x.coeff*(Decimal(math.sin(x.arg)) ** Decimal(x.power))
if m %4 ==3 or (m % 4 == 1 and m != 1):
	for x in condensedSines:
		if x.power == 0:
			print("1", " ")
		elif x.coeff == 1:
			print("+ %dsin(%d°)^%d" % (x.coeff,m, x.power), " ")

		elif x.coeff < 0:
			print("- %d*sin(%d°)^%d" %(-x.coeff,m, x.power),  " ")
		else:
			print("+ %d*sin(%d°)^%d" %(x.coeff,m, x.power),  " ")
		sum += x.coeff*(Decimal(math.sin(x.arg)) ** Decimal(x.power))

if m == 1:
	for x in condensedSines:
		if x.power == 0:
			print("1", " ")
		elif x.coeff == 1:
			print("+ %dsin(1°)^%d" % (x.coeff, x.power), " ")

		elif x.coeff < 0:
			print("- %d*sin(1°)^%d" %(-x.coeff, x.power),  " ")
		else:
			print("+ %d*sin(1°)^%d" %(x.coeff, x.power),  " ")
		sum += x.coeff*(Decimal(math.sin(x.arg)) ** Decimal(x.power))



if m % 4 == 2:
	sum += Decimal(1)


print("= 0")
print("\n"*10,"Using a precision of 60 digits, your computer approximates this as: \n",sum)
print("\n")
print("It turns out one needs only three distinct polynomials, depending on the remainder upon division of m by 4.")
print("Curiously, in the case m % 4 == 1,3, the corresponding polynomial only has roots of the form sin(m°), each of multiplicity 1.")
print("In other cases, there are an additional 24 (possibly degenerate) roots which need not be of this form.")
