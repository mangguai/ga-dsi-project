<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Project 4 - Skin Cancer Detection

> Authors: Cher Wee Zheng, Ng Wei, Ryan Yong

---

## Overview

This project aims to develop a skin cancer detection system to classify skin lesions as either benign or malignant. By leveraging deep learning algorithms on a dataset of skin lesion images, this system seeks to assist individuals like Joseph Tan, a construction foreman, in quickly and accurately determining whether a skin lesion requires medical attention, thereby reducing costs and the need for invasive procedures.

## Persona

Joseph migrated from Guangzhou, China back in 2015 to start a family with his Singaporean wife. Today, Joseph is a Permanent Resident and father of 2, living in Chinese Garden in a 4-room hdb on a 30-year loan. Due to the nature of his job, Joseph is constantly under the sun and recently, noticed a large black spot on his forearm which was not there previously. Joseph is suspicious of the patch, but has no intentions to taking time off and spending more money to run a battery of tests in a hospital. Joseph is willing to seek treatment, only if he is confident in the necessity. In this situation, what should Joseph do?

## Problem Statement

Can we develop a model to be able to effectively and accurately distinguish between a benign or malignant skin cancer spot visually, improving visual tests and reducing the necessity for more invasive biopsies?

## Python Version and Libraries

- Python 3.8 or above
- TensorFlow
- Keras
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn
- OpenCV

## Data Aquisition

The data used in this project is from [Kaggle](https://www.kaggle.com/datasets/bhaveshmittal/melanoma-cancer-dataset/data)

## EDA and Preprocessing
This project utilizes a dataset comprising malignant and benign skin lesion images for model training and evaluation. The dataset is divided into training and testing subsets.

### Exploratory Data Analysis (EDA)
The dataset contains malignant and benign skin lesion images.
Histogram analysis reveals differences in pixel intensity distributions between malignant and benign images.

### Image Preprocessing
- Resizing: Images are resized to a standard resolution.
- Data Augmentation: Techniques like rotation and flipping are applied on images to generate more imagesto increase dataset diversity.
- Normalization: Pixel values are scaled to [0, 1].
These steps prepare the dataset for model training by ensuring uniformity and enhancing model generalization.

## Modelling

During the modelling phase, several deep learning architectures including Inception-ResNetV2, Sequential, Hybrid Model, and a Support Vector Machine (SVM) classifier are trained and evaluated using the prepared dataset. 

### Model Training and Results

| Model                 | Accuracy | Recall | Process Time (min) |
|-----------------------|----------|--------|---------------------|
| Inception-ResNetV2    |   0.89   |  0.82  |       155           |
| Sequential            |   0.88   |  0.90  |       50            |
| Hybrid Model           |   0.91   |  0.91  |       160           |
| SVM                   |   0.90   |  0.87  |       60            |

The Sequential model stands out with a relatively short processing time while maintaining competitive accuracy and recall. This combination of efficiency and performance makes it an attractive choice for the skin cancer detection system, addressing the concerns outlined in the problem statement.

## Model Selection

Based on the evaluation results, the Sequential model is selected for its high accuracy and recall. Its robustness and performance make it suitable for accurately classifying skin lesions, addressing the concerns outlined in the problem statement.

## Model Tuning
For the Sequential model, we tuned the parameters of Learning Rate (0.0001, 0.001, 0.01), Number of Epochs (5, 10, 20) and we decided to proceed with an untuned Sequential model as there was no notable increase in performance. 

## Conclusion

In response to the problem statement concerning the need for efficient and accurate skin cancer detection, this project has developed a Sequential model capable of classifying skin lesions with high accuracy. Through rigorous data preprocessing, model training, and evaluation, we have achieved a reliable solution that can assist individuals like Joseph Tan in making informed decisions about seeking medical attention for suspicious skin lesions.

## Recommendations

Moving forward, the following recommendations can further enhance the effectiveness of the skin cancer detection system:

1. **Continuous Improvement**: Regular updates and enhancements to the model can improve its performance and adaptability to evolving skin lesion patterns and characteristics (e.g., hair removal), as well as other skin cancer types.

2. **Community Outreach**: Educational initiatives aimed at raising awareness about skin cancer detection and prevention can empower individuals to proactively monitor their skin health and seek timely medical advice when necessary.

3. **Development of Consumer Application**: Creation of a consumer application that allows the general public to self-assess any anomalies on their skin without having to consult a doctor can improve accessibility to early detection methods and reduce unnecessary visits to medical facilities.

