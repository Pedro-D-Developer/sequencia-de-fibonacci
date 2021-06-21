def fibonacci(num):
    """
    Fizemos uma função que recebe como parâmetro a quantidade de resultados que o usuário deseja.
    E aplica a sequência de Fibonacci.
    """
    i, a, b = 0, 1, 1
    sequencia_fibonacci = []
    while i < num:
        sequencia_fibonacci.append(a)
        c = a + b
        a, b = b, c
        i += 1
    return sequencia_fibonacci


if __name__ == "__main__":
    # Fazendo o "input" para receber a quantidade de resultados da sequência.
    input_num = int(input("Insira a quantidade da sequência de Fibonacci: "))
    # Imprimimos o resultado para o usuário.
    print(f'O resultado da sequência foi: {", ".join(str(num) for num in fibonacci(input_num))}')
