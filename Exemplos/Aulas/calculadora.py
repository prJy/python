# -*- coding: utf-8 -*-
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def calculadora():
    try:
        primeiroNumero = float(input("Informe o primeiro numero da conta "))
        segundoNumero = float(input("Informe o segundo numero da conta "))
    except:
        print("No primeiro e no segundo numero devem ser infomados apenas numeros válidos, não utilize letras.")
        return False
    operacao = input("Informe o tipo de operação que será realizada (+, -, *, /): ")

    resultado = 0
    tipoOperacao = ""

    if(operacao == "-"):
        resultado = subtracao(primeiroNumero, segundoNumero);
        tipoOperacao = "subtração"
    elif(operacao == "+"):
        resultado = soma(primeiroNumero, segundoNumero);
        tipoOperacao = "soma"
    elif(operacao == "/"):
        resultado = divisao(primeiroNumero, segundoNumero);
        tipoOperacao = "divisão"
    elif(operacao == "*"):
        resultado = multiplicacao(primeiroNumero, segundoNumero);
        tipoOperacao = "multiplicação"
    else:
        print('Informe um operador válido ( + , - , * , / ) ');
        return;  #podemos usar return False, ou apenas return os dois fazem a mesma coisa, interrompem a execução do programa

    print("O valor da " + tipoOperacao + " " + str(primeiroNumero) + " " + operacao + " " + str(segundoNumero) + " é: " + str(resultado));
    return;

print("Bem vindo usuário, vamos testar a nossa calculadora?")
calculadora();

input("Pressione qualquer tecla para continuar")
