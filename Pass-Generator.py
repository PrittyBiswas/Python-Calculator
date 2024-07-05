import random
import string
import PySimpleGUI as sg

upper = random.sample(string.ascii_uppercase, 2)
lower = random.sample(string.ascii_lowercase, 2)
digits = random.sample(string.digits, 2)
symbols = random.sample(string.punctuation, 2)

total = upper + lower + digits + symbols
total = random.sample(total, len(total))
total = ''.join(total)
print(total)

sg.theme('DarkBlue6')
sg.set_options(font='Any 16')

layout = [
    [sg.Text('Uppercase: '), sg.Push(), sg.Input(size=15, key='UP')],
    [sg.Text('Lowercase: '), sg.Push(), sg.Input(size=15, key='Low')],
    [sg.Text('Digits: '), sg.Push(), sg.Input(size=15, key='DIG')],
    [sg.Text('Symbols: '), sg.Push(), sg.Input(size=15, key='SYM')],
    [sg.Button('OK'), sg.Button('Cancel')],
    [sg.Text('Password'), sg.Push(), sg.Input(size=15, key='PASS')]

]

window = sg.Window('Password Generator', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == 'OK':
        u_upper = int(values['UP'])
        u_lower = int(values['Low'])
        u_digits = int(values['DIG'])
        u_symbols = int(values['SYM'])
        upper = random.sample(string.ascii_uppercase, u_upper)
        lower = random.sample(string.ascii_lowercase, u_lower)
        digits = random.sample(string.digits, u_digits)
        symbols = random.sample(string.punctuation, u_symbols)

        total = upper + lower + digits + symbols
        total = random.sample(total, len(total))
        total = ''.join(total)
        window['PASS'].update(total)

window.close()
