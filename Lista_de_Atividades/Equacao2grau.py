"""Faça um programa que leia 3 números reais de precisão dupla, representando os 3 coeficientes de 
uma equação de segundo grau.
E mostre as duas raízes reais dessa equação com precisão de 4 casas decimais separadas por um espaço 
em branco.
A primeira raiz a ser mostrada deve ser aquela a qual se adiciona a raiz de D."""

from math import sqrt 
coefs = input() 
a = float(coefs.split()[0]) 
b = float(coefs.split()[1]) 
c = float(coefs.split()[2]) 
delta = pow(b,2.) - 4. * a * c
 
if delta < 0:
    print("Esta equacao nao possui raizes reais.")
else:
    x1 = (-b + sqrt(delta)) / (2.0 * a) 
    x2 = (-b - sqrt(delta)) / (2.0 * a) 
    print("%.4f %.4f" % (x1, x2))