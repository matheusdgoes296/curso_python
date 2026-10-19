a = 'A'
b = 'B'
c = 1.1
string = 'a={0}, b={nome2}, c={nome3:.2f}'
formato = string.format(nome1=a, nome2=b, nome3=c) #parametro nomeado (nome1, nome2, nome3) e o valor que será atribuido a cada parametro (a, b, c)
print(formato)

