from flask import Flask, render_template, jsonify, url_for, redirect, Blueprint, request
from sklearn.metrics import zero_one_loss
from alg import canvasObject
import os, io
import base64
from io import BytesIO
import numpy as np
from PIL import Image
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
        "numFiles": len(os.listdir("static/assets/coloringPages"))
    }
    return render_template("gallery.html", **args)

@color.route("/draw")
def draw():
    return render_template("draw.html")

@color.route('/bgprocess', methods=['GET', 'POST'])
def bgprocess():
    print("hall")
    if request.method == 'POST':
        print("Image recieved")
        data_url = request.values['imgUrl']
        color = json.loads(json.dumps(request.values['color']))
        print("color is", color)
        img_bytes = base64.b64decode(data_url.split(",")[1])
        img = Image.open(BytesIO(img_bytes))
        img  = np.array(img)

        with open('test.txt', 'w') as outfile:
            for slice_2d in img:
                np.savetxt(outfile, slice_2d.astype(int))

        # canvas = array returned by json process
        x = int(request.values['x'])
        y = int(request.values['y'])

        canvasObj = canvasObject(img)
        canvasObj.updateImage(x,y,[255,0,0,255])
        canvas = canvasObj.canvas 

        imaa = Image.fromarray(canvas.astype('uint8'), mode='RGBA')
        # print("image has been saved")
        # imaa.save("your_file.png")

        im_file = BytesIO()
        imaa.save(im_file, format="PNG")
        im_bytes = im_file.getvalue()  # im_bytes: image in binary format.
        imgByteArr = base64.encodebytes(im_bytes).decode('ascii')
        return jsonify(result=imgByteArr)
    # return the modified array
    return jsonify(result="Error")
 
