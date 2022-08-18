import PySimpleGUI as sg
import subprocess as sp
import os

#GUI Theme
sg.theme('Default')

#Local Variables
user = sp.getoutput('echo %username%')
theme_dir = sp.getoutput(r'dir C:\Users\{}\AppData\local\spicetify\Themes'.format(user))
ext_dir = sp.getoutput(r'dir C:\Users\{}\AppData\Local\spicetify\Extensions'.format(user))
apps_dir = sp.getoutput(r'dir C:\Users\{}\AppData\Local\spicetify\CustomApps'.format(user))

#Themes Window
def Themes():
    layout = [
        [sg.T('Themes: ')],
        [sg.T(theme_dir)],
        [sg.T('Theme Name:'), sg.In(key='theme_name')],
        [sg.T('Color Scheme:'), sg.In(key='color_scheme')],
        [sg.B('Set'), sg.B('View Color Scheme'), sg.B('Back')]
    ]
    window = sg.Window('Themes',
                       layout, 
                       modal=False,
                       icon=r'src\spicetify-logo.ico')
    while True:
        event, values = window.read()
        if event == 'Set':
            current_theme = (values['theme_name'])
            color_scheme = (values['color_scheme'])
            os.system('spicetify config current_theme {}'.format(current_theme))
            os.system('spicetify config color_scheme {}'.format(color_scheme))
            sg.popup('Theme/Color Scheme Applied', icon=r'src\spicetify-logo.ico')
        if event == 'View Color Scheme':
            color_scheme = (values['color_scheme'])
            current_theme = (values['theme_name'])
            f = open('C:/Users/{}/AppData/Local/spicetify/Themes/{}'.format(user, current_theme))
            color = f.read()
            sg.popup_scrolled(color, icon=r'src\spicetify-logo.ico')
        if event == 'Back':
            window.hide()
            main()
        if event == sg.WIN_CLOSED:
            return
    window.close()

def Extensions():
    layout = [
        [sg.T('Extensions:')],
        [sg.T(ext_dir)],
        [sg.T('Extension Name:'), sg.In(key='ext')],
        [sg.B('Add'), sg.B('Remove'), sg.B('Back')]
    ]
    window = sg.Window('Extensions',
                        layout, 
                        modal=False,
                        icon=r'src\spicetify-logo.ico')
    while True:
        event, values = window.read()
        if event == 'Add':
            ext_name = (values['ext'])
            os.system('spicetify config extensions {}'.format(ext_name))
            sg.popup('Extension Added', icon=r'src\spicetify-logo.ico')
        if event == 'Remove':
            ext_name = (values['ext'])
            os.system('spicetify config extensions {}-'.format(ext_name))
            sg.popup('Extension Removed', icon=r'src\spicetify-logo.ico')
        if event == 'Back':
            window.hide()
            main()
        if event == sg.WIN_CLOSED:
            return 
    window.close()

def Apps():
    layout = [
        [sg.T('Apps:')],
        [sg.T(apps_dir)],
        [sg.T('App Name'), sg.In(key='app_name')],
        [sg.B('Add'), sg.B('Remove'), sg.B('Back')]
    ]
    window = sg.Window('Apps', 
                        layout, 
                        modal=False,
                        icon=r'src\spicetify-logo.ico')
    while True:
        event, values = window.read()
        if event == 'Add':
            app = (values['app_name'])
            os.system('spicetify config custom_apps {}'.format(app))
            sg.popup('App Added', icon=r'src\spicetify-logo.ico')
        if event == 'Remove':
            app = (values['app_name'])
            os.system('spicetify config custom_apps {}-'.format(app))
            sg.popup('App Removed', icon=r'src\spicetify-logo.ico')
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
        [sg.Im('src/spicetify-full.png')],
        [sg.B('Config'), sg.B('Apps'), sg.B('Themes'), sg.B('Extensions'), sg.B('Apply'), sg.B('Backup'), sg.B('Restore'), sg.B('Exit')]
    ]
    window = sg.Window('Spicetify', 
                        layout, 
                        modal=False,
                        icon=r'src\spicetify-logo.ico')
    while True:
        event, values = window.read()
        if event == 'Config':
            sg.popup_scrolled(config, icon=r'src\spicetify-logo.ico')
        if event == 'Apps':
            window.hide()
            Apps()
        if event == 'Themes':
            window.hide()
            Themes()
        if event == 'Extensions':
            window.hide()
            Extensions()
        if event == 'Apply':
            os.system('spicetify apply')
            sg.popup('Spicetify Config Applied!', icon=r'src\spicetify-logo.ico')
        if event == 'Backup':
            os.system('spicetify backup')
            sg.popup('Spicetify Backed Up!', icon=r'src\spicetify-logo.ico')
        if event == 'Restore':
            os.system('spicetify restore')
            sg.popup('Spotify Restored!', icon=r'src\spicetify-logo.ico')
        if event == 'Exit':
            return
        if event == sg.WIN_CLOSED:
            return
    window.close()

main()
