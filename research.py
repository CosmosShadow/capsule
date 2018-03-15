# coding: utf-8
import math

def squash(s):
	# assert 0 < s <= 1
	power = math.pow(s, 2)
	left = power / (1 + power) 
	right = s / (abs(s) + 0.00001)
	return left * right

if __name__ == '__main__':
	print squash(100)
	print squash(-100)
	print squash(0.1)