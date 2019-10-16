# asseteditor
A 3d asset / level editor


requires pyfladesk and pyinstaller.

 pip install pyfladesk

 pip install pyinstaller

 to build out to an exe on Windows 10: pyinstaller -w  --add-data "templates;templates" --add-data "static;static" app.py
 
 to build out on a linux distro: pyinstaller -w --add-data "templates:templates" --add-data "static:static" app.py
