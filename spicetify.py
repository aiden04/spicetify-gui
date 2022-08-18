import PySimpleGUI as sg
import subprocess as sp
import os

#local Variables
user = sp.getoutput('echo %username%')
theme_dir = sp.getoutput('dir C:\Users\{}\AppData\local\spicetify\themes'.format(user)')
print(theme_dir)

#Themes Window
def Themes():
    layout = [
        [sg.T('Themes: ')],
        [sg.T(theme_dir)],
        [sg.T('Theme Name:'), sg.In(key='theme_name')],
        [sg.T('Color Scheme:'), sg.In(key='color_scheme')],
        [sg.B('Set'), sg.B('View Color Scheme'), sg.B('Back')]
    ]
    window = sg.Window('Themes', layout, modal=False)
    while True:
        event, values = window.read()
        if event == 'Set':
            current_theme = (values['theme_name'])
            os.system('spicetify config current_theme {}'.format(current_theme))
            sg.popup('Theme/Color Scheme Applied')
        if event == 'View Color Scheme':
            color_scheme = (values['color_scheme'])
            current_theme = (values['theme_name'])
            f = open('C:/Users/{}/AppData/Local/spicetify/Themes/{}'.format(user, current_theme))
            color = f.read()
            sg.popup_scrolled(color)
        if event == 'Back':
            window.hide()
            main()
        if event == sg.WIN_CLOSED:
            return
    window.close()

def main():
    f = open(r'C:/Users/{}/AppData/Roaming/spicetify/config-xpui.ini'.format(user))
    config = f.read()
    layout = [
        [sg.T('Welcome to Spicetify!')],
        [sg.B('Config'), sg.B('Themes'), sg.B('Exit')]
    ]
    window = sg.Window('Spicetify', layout, modal=False)
    while True:
        event, values = window.read()
        if event == 'Config':
            sg.popup_scrolled(config)
        if event == 'Themes':
            window.hide()
            Themes()
        if event == 'Exit':
            return
        if event == sg.WIN_CLOSED:
            return
    window.close()

main()