from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
# from app_helper import *

IMAGE_FOLDER = '/var/www/projects/api/static'

app = Flask(__name__)
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

@app.route("/predict", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        image = request.files["image"]
        if image.filename == '':
            return redirect(request.url)
        else:
            imageName = secure_filename(image.filename)
            imagePath = os.path.join(app.config['IMAGE_FOLDER'], imageName)
            image.save(imagePath)
            return redirect(url_for("upload_file", imageName = imageName))
    else:
        return render_template("index.html")

@app.route("/upload/<imageName>")
def upload_file(imageName):
    return render_template("image.html", image=imageName)
#     predictions=""
#         predictions=get_classes(file_path)
#         pred_strings = []
#         for _,pred_class,pred_prob in predictions:
#             pred_strings.append(str(pred_class).strip()+ " : "+ str(round(pred_prob,5)).strip())
#         preds = ", ".join(pred_strings)
#         print("preds:::",preds)
#     return render_template("upload.html" , predictions=preds, display_image=f.filename)   

if __name__ == "__main__"   :
    #app.run(debug=True)
    app.run(host="127.0.0.1",debug=True,port="5000")