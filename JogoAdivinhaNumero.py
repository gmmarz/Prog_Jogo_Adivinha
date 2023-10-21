#Aluno: Guilherme Melo Marzano
#Objetivo: Jogo de adivinhação, onde pede um número e em seguida pede para usuário tente adivinhar
#Dando dicas se o número digitado é maior ou menor que o número do segredo.

print('Jogo para adivinhar o número')


flg_prog = True #flag para manter o programa rodando.
cnt = 1 # variável acumuladora para contabilizar número de tentativas.
num_pass = 100
num = 0

while flg_prog:
    num_str = input(f'{cnt}º Tentativa  digite um número ou digite x para sair e pressione enter: ')
    
    if num_str.isdigit():
        num = int(num_str)
        if num == num_pass: #Usuário acertou
            break
        elif num > num_pass * 10:
            print('\nO número digitado foi muito acima do segredo')
        elif num > num_pass:
            print('\nO número digitado foi acima do segredo')
        elif num < num_pass/10:
            print('\nO numero dgitado foi muito abaixo que o número segredo')
        elif num < num_pass:
            print('\nO numero dgitado foi abaixo que o número segredo')
        cnt +=1
    elif num_str == 'x':
        flg_prog = False
    else:
        print('Digite apenas números inteiros')        

if flg_prog:
    print(f'Parabéns você adivinhou o número {num_pass} em {cnt} tentativas')
else:
    print('Programa abortado pelo usuário')
    print(f'Programa abortado com {cnt} tentativas. O número segredo era: {num_pass}')

print('\n-------------------Fim do programa-----------------------------------------')