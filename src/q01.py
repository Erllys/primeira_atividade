'''
Created on 9 de mar de 2017

@author: erllys (erllysf@gmail.com)
'''
from math import log 

number = int(input("tamanho da mensagem?"))

bits = int(log(number,2)+1)

print("Quantidae de bits = {0}" .format(bits))