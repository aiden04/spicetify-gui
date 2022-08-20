@echo off
title Spicetify-GUI Installer

setlocal
call :setESC

echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94m [+] Setting up Spicetify-GUI.%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
timeout /t 1 > null
goto 1

:1
cls
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94m [+] Setting up Spicetify-GUI. .%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
timeout /t 1 >  null
goto 2

:2
cls
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94m [+] Setting up Spicetify-GUI. . .%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
timeout /t 1 > null
goto UpdatePIP

:UpdatePIP
cls
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94m [+] Updating PIP%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94m [-] Starting Update%ESC%[0m
echo.
color 0b
pip install --upgrade pip
echo.
echo %ESC%[32m#####################################%ESC%[0m
echo.
echo %ESC%[32m [+] Pip Updated!%ESC%[0m
echo.
echo %ESC%[32m#####################################%ESC%[0m
timeout /t 2 > null
goto requirements

:requirements
cls
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94m [+] Installing Pip Requirements%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94m [-] Installing requirements.txt%ESC%[0m
echo.
color 0b
pip install -r requirements.txt
echo.
echo %ESC%[32m#####################################%ESC%[0m
echo.
echo %ESC%[32m [+] Requirements Installed!%ESC%[0m
echo.
echo %ESC%[32m#####################################%ESC%[0m
timeout /t 2 > null
goto PyInstaller

:PyInstaller
cls
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94m [+] Creating Executable with PySintaller%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94m [-] Creating Executable%ESC%[0m
echo.
color 0b
pyinstaller --onefile --windowed --name Spicetify-GUI --noupx -i "src/spicetify-logo.ico" --distpath "spicetify-gui" "spicetify.pyw" --clean
echo.
echo %ESC%[32m#####################################%ESC%[0m
echo.
echo %ESC%[32m [+] Executable Created!%ESC%[0m
echo.
echo %ESC%[32m#####################################%ESC%[0m
timeout /t 3 > null
goto clean_up

:clean_up
cls
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94m [+] Cleaning Up%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94m [-] move spicetify-gui\spicetify-gui.exe .\spicetify-gui.exe[0m
move spicetify-gui\spicetify-gui.exe .\spicetify-gui.exe
echo %ESC%[94m [-] RMDIR /Q/S build
RMDIR /Q/S build
timeout /t 1 >null
echo %ESC%[94m [-] RMDIR /Q/S spicetify-gui
RMDIR /Q/S spicetify-gui
timeout /t 1 >null
echo %ESC%[94m [-] del /f Spicetify-GUI.spec
timeout /t 3 >null
echo.
del /f Spicetify-GUI.spec
echo %ESC%[32m#####################################%ESC%
echo.
echo %ESC%[32m [+] Directory cleaned up!%ESC%
echo.
echo %ESC%[32m#####################################%ESC%
timeout /t 3 > null

:completed
cls
echo %ESC%[32m#####################################%ESC%[0m
echo.
echo %ESC%[32m [+]Installation Completed!%ESC%[0m
echo.
echo %ESC%[32m#####################################%ESC%[0m
echo.
echo %ESC%[32m [-]Press any key to exit. . .%ESC%[0m
pause > null


:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)
exit /B 0
