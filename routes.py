from flask import Flask, render_template, jsonify, url_for, redirect, Blueprint, request
from alg import updateImage
import os
import base64
from io import BytesIO
import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
import json 
color = Blueprint('color', __name__,
                  template_folder="templates", static_folder="static")

@color.route("/")
def index():
    return render_template("index.html")

@color.route("/gallery")
def gallery():
    print(str(len(os.listdir("static/assets/coloringPages"))))
    args = {
        "numFiles": len(os.listdir("static/assets/coloringPages"))
    }
    return render_template("gallery.html", **args)

@color.route("/draw")
def draw():
    return render_template("draw.html")


color.route("/bg_process/", methods=['GET', 'POST'])
def bg_process():
    print("Image recieved")
    print(request)
    # data_url = request.values['imageBase64']
    # Decoding base64 string to bytes object
    # img_bytes = base64.b64decode(data_url)
    # blob = request.files['image']
    # image_object = Image.open(blob)
    # img = np.array(img)
    # print(img)
    # im = Image.fromarray(A)
    # im.save("your_file.jpeg")

    # canvas = array returned by json process
    #updateImage(canvas,x,y,color)
    # return the modified array
    return jsonify(result="Error")
 
