#An introduction to f-strings in Python

name = 'Matheus Goes'
height = 1.75
weight = 98
imc = weight / (height**2)

line_1 = f'{name} have {height:.2f} height' #:.2f} is used to format the height to 2 decimal places 
line_2 = f'weight {weight} as his IMC is'
line_3 = f'{imc:.2f}'
print(line_1)
print(line_2)
print(line_3)

##print(name, 'have', height, 'height and', weight,'weight, so his IMC is', imc)

