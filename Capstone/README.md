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

## Data Aquisition

#The data used in this project is from [Kaggle](https://www.kaggle.com/datasets/bhaveshmittal/melanoma-cancer-dataset/data)

## EDA and Preprocessing


### Exploratory Data Analysis (EDA)


### Image Preprocessing


## Modelling



### Model Training and Results

| Model                  | Recall | Process Time (min) |
|-----------------------------------------|---------------------|
| Inception-ResNetV2          |  0.82  |       155           |
| Sequential              |  0.90  |       50            |
| Hybrid Model             |  0.91  |       160           |
| SVM                    |  0.87  |       60            |

The Sequential model stands out with a relatively short processing time while maintaining competitive accuracy and recall. This combination of efficiency and performance makes it an attractive choice for the skin cancer detection system, addressing the concerns outlined in the problem statement.

## Model Selection



## Model Tuning


## Conclusion



## Recommendations



