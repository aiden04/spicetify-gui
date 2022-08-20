import PySimpleGUI as sg
import subprocess
import os
import sys

#GUI Theme
sg.theme('SystemDefaultForReal')
ttk_style = 'clam'

#Local Variables
user = subprocess.getoutput('echo %username%')
theme_dir = subprocess.getoutput(r'dir C:\Users\{}\AppData\local\spicetify\Themes'.format(user))
ext_dir = subprocess.getoutput(r'dir C:\Users\{}\AppData\Local\spicetify\Extensions'.format(user))
apps_dir = subprocess.getoutput(r'dir C:\Users\{}\AppData\Local\spicetify\CustomApps'.format(user))

actv_ext = subprocess.getoutput('spicetify config extensions')
actv_apps = subprocess.getoutput('spicetify config custom_apps')
actv_theme = subprocess.getoutput('spicetify config current_theme')
actv_color = subprocess.getoutput('spicetify config color_scheme')

#Run console commands
def runCommand(cmd, timeout=None, window=None):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    output = ''
    for line in p.stdout:
        line = line.decode(errors='replace' if (sys.version_info) < (3, 5) else 'backslashreplace').rstrip()
        output += line
        print(line)
        window.Refresh() if window else None
        retval = p.wait(timeout)
    return (retval, output)                         

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
            exit()
            break
    window.close()

#Extensions Window
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
            exit()
            break 
    window.close()

#Apps Window
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
                     icon=r'src\spicetify-logo.ico')
        if event == 'Remove':
            app = (values['app_name'])
            os.system('spicetify config custom_apps {}-'.format(app))
            sg.popup('App Removed',
                     icon=r'src\spicetify-logo.ico')
        if event == 'Back':
            window.hide()
            main()
        if event == sg.WIN_CLOSED:
            exit()
            break
    window.close()

#Main Menu
def main():
    f = open(r'C:/Users/{}/AppData/Roaming/spicetify/config-xpui.ini'.format(user))
    config = f.read()
    layout = [
        [sg.Im('src/spicetify-full.png')],
        [sg.T('Spicetify Config File:')],
        [sg.Multiline(config, size=(90, 10))],
        [sg.B('Apps'), sg.B('Themes'), sg.B('Extensions'), sg.B('Apply'), sg.B('Backup'), sg.B('Restore'), sg.Button('Install CLI'), sg.B('Install Spotify'), sg.B('Exit')],
        [sg.T('Console Input:'), sg.In(key='_IN_', size=(61)),sg.B('Send Command')],
        [sg.Output(size=(90,5))],
    ]
    window = sg.Window('Spicetify', 
                        layout, 
                        modal=False,
                        icon=r'src\spicetify-logo.ico',
                        use_ttk_buttons=True,
                        ttk_theme=ttk_style
                        )
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
            apply = subprocess.getoutput('spicetify apply')
            print(apply)
            sg.popup('Spicetify Config Applied!',
                     icon=r'src\spicetify-logo.ico',)
        if event == 'Backup':
            backup = subprocess.getoutput('spicetify backup')
            print(backup)
            sg.popup('Spicetify Backed Up!',
                     icon=r'src\spicetify-logo.ico')
        if event == 'Restore':
            restore = subprocess.getoutput('spicetify restore')
            print(restore)
            sg.popup('Spotify Restored!',
                     icon=r'src\spicetify-logo.ico')
        if event == 'Install CLI':
            install = subprocess.getoutput('cmd /c start /min "" powershell -WindowStyle Hidden -ExecutionPolicy Bypass -File "src/install.ps1"')
            market = subprocess.getoutput('cmd /c start /min "" powershell -WindowStyle Hidden -ExecutionPolicy Bypass -File "src/market-install.ps1"')
            print(install)
            print(market)
            print('Spicetify Installed')
            sg.popup('Spicetify has been installed!',
                     icon=r'src\spicetify-logo.ico')
        if event == 'Install Spotify':
            spotify_install = subprocess.getoutput('powershell winget install Spotify.Spotify')
            print(spotify_install)
            print('Spotify Installed')
            sg.popup('Spotify Installed',
                     icon=r'src\spicetify-logo.ico')
        if event == 'Exit':
            exit()
            break
        if event == 'Send Command':
            runCommand(cmd=values['_IN_'], window=window)
        if event == sg.WIN_CLOSED:
            exit()
            break
    window.close()

main()
