import time


class FiladoBanco:
    def __init__(self):
        self.items = []

    def vazio(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] >= 60:
                maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi+1] = []
        return item


preferencial = FiladoBanco()
normal = FiladoBanco()

numpreferencial = 0
numnormal = 0
numidosos = 0
numjovens = 0
print('-=' * 20)
print(f'{"FILA DE BANCO":>25}')
print('-=' * 20)
print('Clinte com menos de 16 anos é proibido pegar fila. ')
print('Fila prefencial só apartir dos 60 anos.')
print()
while True:

    Cliente = int(input('Digite sua idade ou zero pra sair: '))
    print('Computando a dados...')
    time.sleep(1)
    if Cliente >= 16:
        print('Dados computados!')
    if Cliente < 16 and Cliente != 0:
        print('INVÁLIDO')
        continue

    elif Cliente >= 60:
        numidosos += 1
        numpreferencial += 1
        preferencial.insert((numpreferencial))

    elif Cliente != 0:
        numjovens += 1
        numnormal += 1
        normal.insert(numnormal)
    else:
        break

print()
print('-=' * 20)
print(f'{"ORDEM DAS FILAS":>25}')
print('-=' * 20)

while len(preferencial.items) != 0 or len(normal.items) != 0:  #Contando de dois em dois
    cont = 0
    for n in range(2):
        if len(preferencial.items) != 0:
            print('\033[31mATENDIMENTO PREFERENCIAL ')
            print((f'P \033[m'), preferencial.remove())

    if len(normal.items) != 0:
        print('\033[34mATENDIMENTO NORMAL')
        print('N \033[m', normal.remove())

print(f'\033[31mTOTAL DE IDOSOS É {numidosos} \033[m', end=' ')
print(f'\033[34mTOTAL DE JOVENS É {numjovens} \033[m')
print('-=' * 20)