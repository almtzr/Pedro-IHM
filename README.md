# Pedro-IHM

Créer les versions compilées de l’application
Voici comment tu peux créer les différentes versions de l’application IHM pour Windows, macOS, et Linux.

## Windows (via PyInstaller) :

1. Installe PyInstaller :
```
pip install pyinstaller
```
2. Crée un fichier .exe :
```
pyinstaller --onefile --add-data "avrdude;avrdude" --add-data "src/*;src" src/main.py
```
Cela génère un fichier Pedro-IHM.exe dans le dossier dist/.

## MacOS (via py2app) :

1. Installe py2app :
```
pip install py2app
```
2. Configure un fichier setup.py pour py2app.

3. Compile l’application :
```
python setup.py py2app
```
Cela générera un fichier Pedro-IHM.app dans le dossier dist/.

## Linux (via PyInstaller ou AppImage) :

1. Pour PyInstaller :
```
pyinstaller --onefile --add-data "avrdude;avrdude" --add-data "src/*;src" src/main.py
```
Cela génère un fichier Pedro-IHM.AppImage dans le dossier dist/.

2. Pour créer un fichier .deb, tu peux utiliser fpm :
```
fpm -s python -t deb src/main.py
```
