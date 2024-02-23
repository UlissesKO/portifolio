from random import choice
from time import time, sleep

WORDS_LENGHT = 261798
points = 0
rounds = 0
Times = []
media = 0
correct = False

#Abre o arquivo txt com todas as palavras
with open(r'C:\Users\uliss\Documents\VsCode\Projetos\Velocidade_digitação\palavras.txt', 'r', encoding='utf-8') as database:
    text = database.readlines()

print("Este é um desafio para ver quão rápido se pode digitar!\nDigite a palavra que aparecer escrita e aperte enter o mais rápido possivel")  
input()

while correct == False: #Para garantir nenhum erro na hora de escrever o numero de rounds
    try:
        rounds = input("Quantas palavras vai escrever? ")
        Round = int(rounds.strip()) 

        correct = True

    except ValueError:
        print("Digite um número ordinal")
        

input("Pressione enter para começar o jogo")   
sleep(1)

for i in range(Round):
    Choice = choice(range(WORDS_LENGHT))
    choosenWord = text[Choice]#Escolhe a palavra da lista

    initial_time = time()#Seta o tempo inicial
    word = input(choosenWord)
    end_time = time()#Seta tempo final

    Time = end_time - initial_time #Calcula o tempo gasto para escrever a palavra

    if word.lower().strip() == choosenWord.lower().strip(): #Confere se a palavra está certa ou não
        print(round(Time, 3))
        points += 1
        Times.append(Time)
    else:
        Round -= 1
    
    sleep(0.5)


for time in Times: #Calcula a media do tempo
    media += time
media /= Round

print(f"Parabéns, você fez {points} pontos e teve uma média de {media} segundos por palavra!")