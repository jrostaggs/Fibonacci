#hashtag
#created by Hunter Seglem, Jon Staggs, with Counselling from Caleb Barnwell

import math 

def fibPrint(n):
	a=0
	b=1
	for i in range(n-1):
		c=a
		a=b
		b=b+c
		print(a)
	

kCzech=input("Desired Fibonacci term  ")
number=int(kCzech)


fibPrint(number)
