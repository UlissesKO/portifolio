import PySimpleGUI as sg
import random

num = random.randint(1,100)
contagem = 0

sg.theme('Topanga')
lay = [
    [sg.Text('Número foi sorteado')],
    [sg.Text('insira um número: ')],
    [sg.Input(key='numero')],
    [sg.Text('', key='dica')],
    [sg.Button('Número certo?')],[sg.Text('', key='contagem')],
    [sg.Text('', key='mensagem')]
]

jan = sg.Window('número', layout=lay)

while True:
    event, valor = jan.read()
    num12 = valor['numero']
    num1 = int(num12)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Número certo?':
        if num1 > num:
            num2 = num1 - num
            if num2 > 40:
                jan['dica'].update('Muito grande, fale um muito menor')
            elif num2 < 40 and num2 > 15:
                jan['dica'].update('Grande, diminua um pouco')
            elif num2 < 15 and num2 > 5:
                jan['dica'].update('Esta bem proxima, diminua mais')
            elif num2 < 5 and num2 > 0:
                jan['dica'].update('Esta extremamente perto, diminua um pouco')

        if num1 < num:
            num2 = num - num1
            if num2 > 40:
                jan['dica'].update('Muito pequeno, fale um muito maior')
            elif num2 < 40 and num2 > 15:
                jan['dica'].update('Pequeno, aumente um pouco')
            elif num2 < 15 and num2 > 5:
                jan['dica'].update('Esta bem proxima, aumente mais')
            elif num2 < 5 and num2 > 0:
                jan['dica'].update('Esta extremamente perto, aumente um pouco')
    contagem = contagem + 1
    jan['contagem'].update(f'Esta é a {contagem} tentativa')

    if num1 == num:
        jan['mensagem'].update('Certo')
        sg.popup('Certissimo!!')
        break