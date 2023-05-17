<H1 align="center">Development has ended, Spicetify-GUI will no longer recieve updates. Updates to spicetify-cli may leave this project broken and unable to install spicetify!</h1>

<h3 align="center"><a href="https://spicetify.app/"><img src="https://user-images.githubusercontent.com/9298623/185500058-09a6bbc4-1326-4d17-96e8-1eb4e6fe1337.png" width="600px"></a></h3>

<h1 align="center">Spicetify GUI</h1>

<p align="center">
  Welcome to Spicetify-GUI, a program that offers a graphical user interface for the <a href="https://spicetify.app">Spicetify-CLI</a> project. With spicetify, you can have full control over your spotify. When using the <a href="https://github.com/spicetify/spicetify-themes">Community Made Themes</a>, you can polish your spotify to however you like. With the <a href="https://github.com/3raxton/spicetify-custom-apps-and-extensions">Comunity Made Extensions</a>, you can control your spotify in many different ways. Finally with <a href="https://github.com/3raxton/spicetify-custom-apps-and-extensions">Custom Apps</a>, you can have reddit integration, raw lyrics, and more.
</p>

<p align="center">
  <a href="https://github.com/search?q=Spicetify"><img src="https://img.shields.io/badge/for-spicetify-E71A0E.svg" alt="For Spicetify"></a>
  <a href="https://github.com/git/git-scm.com/blob/main/MIT-LICENSE.txt"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License"></a>
</p>

<h1 align="center">Requirements</h1>

<p>
  This software requires three other software in order to run, these are:
</p>

<ul>
  <li><a href="https://python.org">Python 3.0</a></li>
  <li><a href="https://spicetify.app">Spicetify-CLI</a></li>
  <li><a href="https://spotify.com">Spotify</a></li>
</ul>

<h1 align="center">Installation</h1>

<p>
  The installation for Spicetify-GUI is very easy and straight foward. There are two methods, these methods are automatic or manual.
</p>

<h3>Automatic</h3>

The automatic way is as easy as downloading the releases and launching the `Installer.bat`. This will update pip, then install the requirements, and finally create an executable. You can choose to move the root folder to where you want, then create a shortcute on the desktop.

<h3>Manual</h3>

<p>
Open a command prompt and paste this code into the console:
</p>

```python
git clone https://github.com/aiden04/spicetify-gui.git
cd spicetify-gui
pip install -r requirements.txt
pyinstaller --onefile --windowed --name Spicetify-GUI --noupx -i "src/spicetify-logo.ico" --distpath "spicetify-gui" "spicetify.pyw" --clean
RMDIR /Q/S build
RMDIR /Q/S spicetify-gui
del /f Spicetify-GUI.spec
powershell -ExecutionPolicy Bypass -File "src/install.ps1"
powershell -ExecutionPolicy Bypass -File "src/market-install.ps1"
```

This will install the requirements, and create an executable. You can choose to move the root folder to where you want, then create a shortcute on the desktop.

<h1 align="center">Features</h1>
<p>
Spicetify offers many features like oneclick easyinstall for <a href="https://spicetify.app">Spicetify-CLI</a>, <a href="https://spotify.com">Spotify</a>, and many more!.
</p>

<ul>
  <li>Easy edit to <a href="https://spicetify.app">Spicetify-CLI</a> config file</li>
  <li>Simple way to change theme</li>
  <li>Simple way to add Extensions</i>
  <li>Simple way to add Apps</li>
  <li>Built in Command Line Interface for quick debugging and <a href="https://spicetify.app">Spicetify-CLI</a> settings</li>
  <li>Easy Install <a href="https://spicetify.app>Spicetify-CLI</a></li>
  <li>Easy Install <a href="https://spotify.com">Spotify</a></li>
</ul>

<h1 align="center">Media</h1>

<h3 align="center">Main Menu</h3>
<h3 align="center"><img src="https://user-images.githubusercontent.com/9298623/193435984-13fb9c5c-293a-451d-a137-dc7592ddca98.png"></h3>

<h3 align ="center">Apps</h3>
<h3 align="center"><img src="https://user-images.githubusercontent.com/9298623/186846373-7978dbdc-c2a0-4762-8030-2da2da0c8ecb.png"></h3>

<h3 align="center">Themes</h3>
<h3 align="center"><img src="https://user-images.githubusercontent.com/9298623/186846458-700e1c28-4307-4f25-8f2f-3ce96a656046.png"></h3>

<h3 align="center">Extensions</h3>
<h3 align="center"><img src="https://user-images.githubusercontent.com/9298623/186846547-c05f57b0-cf19-4078-888b-f863855459db.png"></h3>

<h1 align="center">More about Spicetify-CLI</h1>

<p>
  This project wouldn't be possible if it weren't for the great people behind the <a href="https://spicetify.app">Spicetify-CLI Project</a>. Everyone should definetly go check out their website.
</p>

<ul> 
  <li><a href="https://spicetify.app">Spicetify Website</a></li>
  <li><a href="https://github.com/spicetify/spicetify-cli">Github</a></li>
  <li><a href="https://spicetify.app/docs/getting-started">Docs</a></li>
  <li><a href="https://spicetify.app/blog">Blog</a></li>
</ul>

<h3>License</h3>
<p>
MIT License

Copyright (c) 2022 aiden04

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
</p>
