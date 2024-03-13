# respostas teste target sistemas
# 1

# indice = 13
# k = 0
# soma = 0

# while k < indice:
#     k = k + 1
#     soma = soma + k

# print(soma)
# --------------------------------------------------------------


# 2


# Adição em uma lista toda a sequência de fibonacci onde é realizado os incrementos
def fibonacci(n):
    fib = [0, 1]
    while fib[-1] <= n:
        fib.append(fib[-1] + fib[-2])
    return fib


# checagem se o número existe ou não na sequência
def fib_check(num):
    fib_seq = fibonacci(num)
    if num in fib_seq:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."


# passagem de parametros
numero = int(input("Digite um número: "))
print(fib_check(numero))

# --------------------------------------------------------------------
