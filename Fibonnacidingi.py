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
	

kCzech=input("Just put a damn number here and see what happens ")
number=int(kCzech)


fibPrint(number)
