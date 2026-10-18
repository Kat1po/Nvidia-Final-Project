#!/usr/bin/python3

import jetson_inference
import jetson_utils
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("filename", type=str, help="file path of an object in space to classify.")
opt=parser.parse_args()

img=jetson_utils.loadImage(opt.filename)
net=jetson_inference.imageNet(argv=["--labels=labels.txt", "--model=resnet18.onnx", "--input_blob=input_0", "--output_blob=output_0"])
class_idx, confidence=net.Classify(img)
class_desc=net.GetClassDesc(class_idx)

print("This is a "+str(class_desc)+" ("+f"{confidence*100:.2f}"+"% confidence)" )