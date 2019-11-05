import random


def main():

    print('\n')
    opcao = str(input('Escolha "x" para digitar os valores ou "o" para valores aleatórios: '))
    limite = int(input('Escolha o limite de limiarização: '))

    if opcao == 'x':
        matriz = []
        for i in range(10):
            matriz.append([])
            for j in range(10):
                matriz[i].append(int(input(f'Posição {i+1}x{j+1}: ')))
    elif opcao == 'o':
        matriz = []
        for i in range(10):
            matriz.append([])
            for j in range(10):
                matriz[i].append(random.randint(1, 255))
    else:
        print('Opção incorreta, digite apenas "x" ou "o"')


    print('\n')
    print('Antes da binarização:')
    for item in matriz:
        print(item)

    for i in range(10):
        for j in range(10):
            if matriz[i][j] >= limite:
                matriz[i][j] = 1
            else:
                matriz[i][j] = 0

    print('\n')
    print('Depois da binarização:')
    for item in matriz:
        print(item)

if __name__ == '__main__':
    main()
