from sys import exit
from argparse import ArgumentParser

def calcBMI(weight: int, height: int):
  return weight / (height ** 2) * 10000

def argsParser():
  parser = ArgumentParser(description='Optional app description')

  # Optional positional argument
  parser.add_argument(
    '--lang',
    type=str,
    default='en',
    help='Set language to use (available: en & pt_br)'
  )

  return parser.parse_args()

def signal_handler(signal, frame):
  exit(0)
