from flask import * 
import argparse
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel
import detect
app = Flask(__name__)
@app.route('/')
def helloWorld():
    return render_template('index.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        f = request.files['file']
        print(f)
        print("hi")
        # sys.argv = []
        f.save('static/'+f.filename)
        
        detect.detect('./static/'+f.filename)
        return redirect("/endpoint")
        
@app.route('/endpoint',methods= ['GET','POST'])
def endpoint():
    return render_template('success.html')

if __name__ == "__main__":
    app.run(debug=True)