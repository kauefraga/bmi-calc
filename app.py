from lib import calcIMC, showInfo


print('>> Calculadora de Indice de Massa Corporal <<\n')
  
weight = input('Qual seu peso? (kg) > ')
height = input('Qual sua altura? (cm) > ')

imc = calcIMC(int(weight), int(height))

roundedIMC = round(imc, 2)

showInfo('\n-> ' + str(roundedIMC))
