from flask import Flask, render_template, request
from pyfladesk import init_gui
import os, sys
import glob
from helper import resource_path
import base64
from PIL import Image
from io import BytesIO




icon = resource_path(os.path.join('static', 'appicon.png'))
if getattr(sys, 'frozen', False):
    template_folder = resource_path('templates')
    static_folder = resource_path('static')
    temp_folder = resource_path('temp')
    app = Flask(__name__, template_folder=template_folder,
                static_folder=static_folder,temp_folder=temp_folder)
else:
    app = Flask(__name__)

@app.route('/')
def upload_file():
    objects = [os.path.basename(objects) for objects in glob.glob('static/*.glb')]
    return render_template('index.html',objects=objects)



@app.route('/save', methods=['GET', 'POST'])
def load_file():
    objects = [os.path.basename(objects) for objects in glob.glob('static/*.glb')]
    content = request.data
    print(content.decode("utf-8"))
    file = open('temp/scene.babylon', 'w')
    file.write(content.decode("utf-8"))
    file.close()
    return render_template("index.html",objects=objects)

@app.route('/import', methods=['GET', 'POST'])
def import_files():
    objects = [os.path.basename(objects) for objects in glob.glob('static/*.glb')]
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join('static', file.filename))
        return render_template('index.html',objects=objects)


@app.route('/export', methods=['GET', 'POST'])
def export_files():
    objects = [os.path.basename(objects) for objects in glob.glob('static/*.glb')]
    content = request.data
    im = Image.open(BytesIO(base64.b64decode(content)))
    im.save("temp/imag1e.png")
    im.close()
    return render_template('index.html',objects=objects)

@app.route('/glb', methods=['GET', 'POST'])
def glb_go():
    objects = [os.path.basename(objects) for objects in glob.glob('static/*.glb')]
    content = request.data
    print(content)
    file = open('temp/scene.glb', 'w')
    file.write(content.decode("utf-8"))
    file.close()

    return render_template('index.html',objects=objects)
init_gui(app,port=5000, width=1366, height=768,
             window_title="AssetEditor", icon="appicon.png", argv=None)

if __name__ == '__main__':
    init_gui(app)


