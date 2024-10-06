# Facial Emotion Recognition
![Started](https://img.shields.io/badge/Started-Dec%202020-blue%20green.svg)
![Last Updated](https://img.shields.io/badge/Last%20Updated-Jan%202021-blue.svg?color=informational)

This Artificial Neural Network (ANN) can understand emotions from a face! :D

## Model
The model makes use of convolutional layers to extract image information, this convolutional layers are then followed by an artificial neural network (ANN) that performs a classification task to assign one of the seven emotions to the face.

The model was trained in Google Colab's free tier which limited the amount of time and compute power used.

## Dataset
The dataset used to train the model was the data from the [Facial Expression Recognition Challenge from 2013](https://www.kaggle.com/competitions/challenges-in-representation-learning-facial-expression-recognition-challenge).

## Model Workflow
  1. ## Image Pre-Processing
     The image is cropped to where the face is (if needed) and then resized to 48x48 pixels.
    
   3. ## Inference
      The now pre-processed image is then passed through the model which analyses the image and identifies the current emotion being showed :O

## How to use

  1. Clone this repository:
     ```bash
     git clone https://github.com/juanmartin8a/Facial-Emotion-Recognition.git
     cd Facial-Emotion-Recognition

  2. Make sure to add the weights to the "weights" directory. To add the weights:
     
      1. Download the [model.h5](https://drive.google.com/file/d/1eFbDKUJtvoqzMNfCexs-uQ0ZOXMIKpgn/view?usp=sharing) file and [model.json](https://drive.google.com/file/d/1ZoWRkg13eXcjx6jrro2vEIwsLeMhsMDN/view?usp=sharing) file since this files contain the model with the weights.
     
      2. Add the files to the "weights" directory :)

  3. Run the program: `python test.py`.

## Example Screenshot
<img width="1440" alt="Screen Shot 2020-12-21 at 21 27 45 copy" src="https://github.com/user-attachments/assets/0d130ea1-d32c-4c77-a7b6-ce7f17bbf4a0">


## Disclaimer
If I remember correctly, the code used to train the model was inspired by someone who competed in the challenge I just don't remember who was it and I also was not able find the code.
