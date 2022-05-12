from flask import Flask, render_template
from flask import request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

#path_new = os.chdir(os.getcwd() + "\\Hacking\\host")

app.config["UPLOAD_FOLDER"] = "./Upload"

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])

def upload():
    if request.method == "POST":
        f = request.files["archivo"]
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        return "<h1>Archivo subido exitosamente</h1>"

if __name__=="__main__":
    app.run(debug=True)