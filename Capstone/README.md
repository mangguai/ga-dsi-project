<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Capstone Project - TheiaVision: Object Detection Technology for PMD Safety Alerts

> Authors: Ng Wei

---

## Overview

This project aims to develop a object detection system to identifies obstacles such as pedestrians, vehicles, and traffic signs. By leveraging CNN algorithms YOLO model, this system would help Darren, a project manager, to lead the development of an alert system with object detection technology

## Persona

Darren (Product Manager of MaximalSG) is addressing the critical challenge of enhancing PMD safety due to increasing urban accidents. He is leading the development of an alert system with object detection technology that identifies obstacles such as pedestrians, vehicles, and traffic signs.


## Problem Statement

How can we enhance the safety of Personal Mobility Devices (PMDs) in urban environments by using object detection to improve PMD users' ability to perceive and respond to their surroundings?

## Python Version and Libraries

- Python 3.8 or above
- Pytorch
- Ultralytics
- IPython
- Pillow
- os
- subprocess
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn
- OpenCV
- Numpy
- Random

## Dataset

1. Udacity Self Driving Car Data: [Roboflow](https://public.roboflow.com/object-detection/self-driving-car)
2. Singapore Traffic Sign Data: [Github](https://github.com/eugeneyan84/Classification-and-Detection-of-Singapore-Road-Traffic-Signs/tree/main/Dataset)

### Exploratory Data Analysis (EDA)
- There are total 7 type of signs shortlisted in the Singapore Traffic Data

### Image Augmentation
- Singapore Traffic Sign data have been 3 augmentation method, which are saturation, rotation and blur.

## Modelling
- Pytorch Simple CNN and YOLOv8 CNN models are ultilized in this project
1.  Simple CNN with Pytorch framework, a basic multi-class single-prediction model with Singapore Traffic Sign Data only
2.  YOLOv8 Pytorch based CNN pre-trained model. Multi-class multi-prediction model with Singapore Traffic Sign Data only
3.  YOLOv8 Pytorch based CNN pre-trained model. Multi-class multi-prediction model with Singapore Traffic Sign + Udacity data

## Hypertuning
- Hyperparameters tuned are learning rate and Batch size.
- Learning Rate: 0.001, 0.01 and 0.1
- Batch Size: 8 and 16
- Based model perform better compare to hpyertuning. Have 80.5% sensitivity

## Conclusion
- TheiaVision helps to detect object with 80.5% sensitivity

## Recommendations
- Handle imbalance datasets (SMOTE)
- Include Diverse Image of Traffic Sign (Currently Data from DashCam Only, low resolution)
- Stereo Video for depth estimation
- Including hazard detection (pavement condition, construction, etc.)
- Install Speaker for Voice Feedback to PMD Users