@echo off

setlocal
call :setESC

echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94mSetting up Spicetify-GUI.%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
timeout /t 1 > null
goto 1

:1
cls
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94mSetting up Spicetify-GUI. .%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
timeout /t 1 >  null
goto 2

:2
cls
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94mSetting up Spicetify-GUI. . .%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
timeout /t 1 > null
goto UpdatePIP

:UpdatePIP
cls
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94mUpdating PIP%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo %ESC%[94mStarting Update%ESC%[0m
pip install --upgrade pip
echo %ESC%[32m#####################################%ESC%[0m
echo.
echo %ESC%[32mPip Updated!%ESC%[0m
echo.
echo %ESC%[32m#####################################%ESC%[0m
timeout /t 2 > null
goto requirements

:requirements
cls
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94mInstalling Pip Requirements%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94mInstalling requirements.txt%ESC%[0m
pip install -r requirements.txt
echo %ESC%[32m#####################################%ESC%[0m
echo.
echo %ESC%[32mRequirements Installed!%ESC%[0m
echo.
echo %ESC%[32m#####################################%ESC%[0m
timeout /t 2 > null
goto PyInstaller

:PyInstaller
cls
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94mCreating Executable with PySintaller%ESC%[0m
echo.
echo %ESC%[94m#####################################%ESC%[0m
echo.
echo %ESC%[94mCreating Executable%ESC%[0m
pyinstaller --onefile --windowed --name Spicetify-GUI --noupx -i "src/spicetify-logo.ico" --distpath "spicetify-gui" "spicetify.pyw" --clean
echo %ESC%[32m#####################################%ESC%[0m
echo.
echo %ESC%[32mExecutable Created!%ESC%[0m
echo.
echo %ESC%[32m#####################################%ESC%[0m
timeout /t 3 > null
goto completed

:completed
cls
echo %ESC%[32m#####################################%ESC%[0m
echo.
echo %ESC%[32mInstallation Completed!%ESC%[0m
echo.
echo %ESC%[32m#####################################%ESC%[0m
echo.
echo %ESC%[32mPress any key to exit. . .%ESC%[0m
pause > null


:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)
exit /B 0