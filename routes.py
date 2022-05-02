from flask import Flask, render_template, jsonify, url_for, redirect, Blueprint, request
from sklearn.metrics import zero_one_loss
from alg import canvasObject
import os, io
import base64
from io import BytesIO
import numpy as np
from PIL import Image, ImageDraw
from matplotlib import pyplot as plt
import json, requests
color = Blueprint('color', __name__,
                  template_folder="templates", static_folder="static")

@color.route("/")
def index():
    return render_template("index.html")

@color.route("/gallery")
def gallery():
    print(str(len(os.listdir("static/assets/coloringPages"))))
    args = {
        "files": os.listdir("static/assets/coloringPages")
    }
    print(args['files'])
    return render_template("gallery.html", **args)

@color.route("/draw")
def draw():
    return render_template("draw.html")

@color.route('/bgprocess', methods=['GET', 'POST'])
def bgprocess():
    # when we make edit on canvas, we send to python
    if request.method == 'POST':
        print("Image recieved")

        # decode image
        data_url = request.values['imgUrl']
        img_bytes = base64.b64decode(data_url.split(",")[1])
        img = Image.open(BytesIO(img_bytes))
        img = img.convert("RGBA")

        # get x,y coordinates clicked
        x = int(request.values['x'])
        y = int(request.values['y'])

        # get color we want to use
        color = json.loads(json.loads(json.dumps(request.values['color'])))

        # fill algorithm
        ImageDraw.floodfill(img, (x, y), (color["r"], color["g"], color["b"], 255), thresh=200)
        img.save("geeks.png")
        # canvasObj = canvasObject(img)
        # canvasObj.updateImage(x,y,[color["r"], color["g"], color["b"], 255])
        # canvas = canvasObj.canvas 

        # take edited array and save in correct format to send back to JS
        # imaa = Image.fromarray(canvas.astype('uint8'), mode='RGBA')

        im_file = BytesIO()
        img.save(im_file, format="PNG")
        im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
        imgByteArr = base64.encodebytes(im_bytes).decode('ascii')
        print("done")

        return jsonify(result=imgByteArr)
    return jsonify(result="Error")
 
