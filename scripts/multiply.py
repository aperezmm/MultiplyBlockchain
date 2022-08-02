from brownie import Stackies, Contract

def multiply():
    stackies = Contract("0x2c5194D242c8DE8F97e5760e53E3cc4A452d922A")
    #stackies = Stackies[-1]

    result = stackies.multiplyValues(5, 8)
    print(f"El valor a verificar si es modular es {result}")

def main():
    multiply()