import signal
from lib import calcBMI, argsParser, signal_handler

def main():
  args = argsParser()

  if args.lang == 'en':
    print('>> Calculator of Body Mass Index <<\n')

    weight = input('Whats your weight? (kg) > ')
    height = input('Whats your height? (cm) > ')

    bmi = calcBMI(int(weight), int(height))

    roundedBMI = round(bmi, 2)

    print('\n-> ' + str(roundedBMI))

  if args.lang == 'pt_br':
    print('>> Calculadora de Indice de Massa Corporal <<\n')

    weight = input('Qual seu peso? (kg) > ')
    height = input('Qual sua altura? (cm) > ')

    bmi = calcBMI(int(weight), int(height))

    roundedBMI = round(bmi, 2)

    print('\n-> ' + str(roundedBMI))

if __name__ == '__main__':
  signal.signal(signal.SIGINT, signal_handler)
  main()
