import PySimpleGUI as sg
import subprocess as sp
import os

#GUI Theme
sg.theme('SystemDefaultForReal')
ttk_style = 'clam'

#Local Variables
user = sp.getoutput('echo %username%')
theme_dir = sp.getoutput(r'dir C:\Users\{}\AppData\local\spicetify\Themes'.format(user))
ext_dir = sp.getoutput(r'dir C:\Users\{}\AppData\Local\spicetify\Extensions'.format(user))
apps_dir = sp.getoutput(r'dir C:\Users\{}\AppData\Local\spicetify\CustomApps'.format(user))

actv_ext = sp.getoutput('spicetify config extensions')
actv_apps = sp.getoutput('spicetify config custom_apps')
actv_theme = sp.getoutput('spicetify config current_theme')
actv_color = sp.getoutput('spicetify config color_scheme')

#Themes Window
def Themes():
    layout = [
        [sg.T('Themes: ')],
        [sg.T(theme_dir)],
        [sg.T('Current theme:'), sg.T(actv_theme)],
        [sg.T('Current Color:'), sg.T(actv_color)],
        [sg.T('Theme Name:'), sg.In(key='theme_name')],
        [sg.T('Color Scheme:'), sg.In(key='color_scheme')],
        [sg.B('Set'), sg.B('View Color Scheme'), sg.B('Back')]
    ]
    window = sg.Window('Themes',
                       layout, 
                       modal=False,
                       icon=r'src\spicetify-logo.ico',
                       use_ttk_buttons=True,
                       ttk_theme=ttk_style)
    while True:
        event, values = window.read()
        if event == 'Set':
            current_theme = (values['theme_name'])
            color_scheme = (values['color_scheme'])
            os.system('spicetify config current_theme {}'.format(current_theme))
            os.system('spicetify config color_scheme {}'.format(color_scheme))
            sg.popup('Theme/Color Scheme Applied',
                     icon=r'src\spicetify-logo.ico',
                     ttk_theme=ttk_style)
        if event == 'View Color Scheme':
            color_scheme = (values['color_scheme'])
            current_theme = (values['theme_name'])
            f = open('C:/Users/{}/AppData/Local/spicetify/Themes/{}'.format(user, current_theme))
            color = f.read()
            sg.popup_scrolled(color,
                              icon=r'src\spicetify-logo.ico',
                              ttk_theme=ttk_style)
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
        [sg.T('Active Extensions:'), sg.T(actv_ext)],
        [sg.T('Extension Name:'), sg.In(key='ext')],
        [sg.B('Add'), sg.B('Remove'), sg.B('Back')]
    ]
    window = sg.Window('Extensions',
                        layout, 
                        modal=False,
                        icon=r'src\spicetify-logo.ico',
                        use_ttk_buttons=True,
                        ttk_theme=ttk_style)
    while True:
        event, values = window.read()
        if event == 'Add':
            ext_name = (values['ext'])
            os.system('spicetify config extensions {}'.format(ext_name))
            sg.popup('Extension Added',
                     icon=r'src\spicetify-logo.ico')
        if event == 'Remove':
            ext_name = (values['ext'])
            os.system('spicetify config extensions {}-'.format(ext_name))
            sg.popup('Extension Removed',
                     icon=r'src\spicetify-logo.ico')
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
        [sg.T('Active Apps'), sg.T(actv_apps)],
        [sg.T('App Name'), sg.In(key='app_name')],
        [sg.B('Add'), sg.B('Remove'), sg.B('Back')]
    ]
    window = sg.Window('Apps', 
                        layout, 
                        modal=False,
                        icon=r'src\spicetify-logo.ico',
                        use_ttk_buttons=True,
                        ttk_theme=ttk_style)
    while True:
        event, values = window.read()
        if event == 'Add':
            app = (values['app_name'])
            os.system('spicetify config custom_apps {}'.format(app))
            sg.popup('App Added',
                     icon=r'src\spicetify-logo.ico',
                     ttk_theme=ttk_style)
        if event == 'Remove':
            app = (values['app_name'])
            os.system('spicetify config custom_apps {}-'.format(app))
            sg.popup('App Removed',
                     icon=r'src\spicetify-logo.ico',
                     ttk_theme=ttk_style)
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
        [sg.Multiline(config, size=(82, 10))],
        [sg.B('Apps'), sg.B('Themes'), sg.B('Extensions'), sg.B('Apply'), sg.B('Backup'), sg.B('Restore'), sg.Button('Install CLI'), sg.B('Exit')],
        [sg.T('Console Input: '), sg.In(key='command', size=(52)),sg.B('Send Command')]
    ]
    window = sg.Window('Spicetify', 
                        layout, 
                        modal=False,
                        icon=r'src\spicetify-logo.ico',
                        use_ttk_buttons=True,
                        ttk_theme=ttk_style).Finalize()
    while True:
        event, values = window.read()
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
            sg.popup('Spicetify Config Applied!',
                     icon=r'src\spicetify-logo.ico',)
        if event == 'Backup':
            os.system('spicetify backup')
            sg.popup('Spicetify Backed Up!',
                     icon=r'src\spicetify-logo.ico')
        if event == 'Restore':
            os.system('spicetify restore')
            sg.popup('Spotify Restored!',
                     icon=r'src\spicetify-logo.ico')
        if event == 'Install CLI':
            sp.run("iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-cli/master/install.ps1 | iex", shell=True ,capture_output=True,text=True)
            sp.run("iwr -useb https://raw.githubusercontent.com/spicetify/spicetify-marketplace/main/resources/install.ps1 | iex", shell=True ,capture_output=True,text=True)
        if event == 'Exit':
            return
        if event == 'Send Command':
            command = (values['command'])
            os.system(command)
        if event == sg.WIN_CLOSED:
            return
    window.close()

main()
