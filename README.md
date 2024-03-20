# Melanoma Detection using CNN
To build a CNN based model which can accurately detect melanoma. 

Melanoma is a type of cancer that can be deadly if not detected early. 

It accounts for 75% of skin cancer deaths. A solution that can evaluate images and alert dermatologists about the presence of melanoma has the potential to reduce a lot of manual effort needed in diagnosis.



## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Conclusions](#conclusions)
* [Acknowledgements](#acknowledgements)

<!-- You can include any other section that is pertinent to your problem -->

## General Information
To detect Melanoma, we use ISIC data set and build a CNN with multiple layers, dropouts.  We also augment the data with some techniques.

The dataset consists of 2357 images of malignant and benign oncological diseases, which were formed from the International Skin Imaging Collaboration (ISIC). 

All images were sorted according to the classification taken with ISIC, and all subsets were divided into the same number of images, with the exception of melanomas and moles, whose images are slightly dominant.

The data set contains the following diseases:

- Actinic keratosis
- Basal cell carcinoma
- Dermatofibroma
- Melanoma
- Nevus
- Pigmented benign keratosis
- Seborrheic keratosis
- Squamous cell carcinoma
- Vascular lesion

### Project Pipeline

- **Data Reading** → Defined the path for train and test images
- **Dataset Creation** → Created train & validation dataset from the train directory with a batch size of 32. Made sure images are resized to 180*180
- **Dataset visualisation** → Created a code to visualize one instance of all the nine classes present in the dataset
- **Model Building & training** → 
   - Created a CNN model, which can accurately detect 9 classes present in the dataset. While building the model, rescale images to normalize pixel values between (0,1).
   - Chose an appropriate optimiser and loss function for model training
   - Trained the model for ~30 epochs
   - Wrote the findings after the model fit. Checked for overfitting and underfitting
- **Data Augmentation** → Chose an appropriate data augmentation strategy to resolve underfitting/overfitting
- **Model Building & training on the augmented data** →
  - Created a CNN model, which can accurately detect 9 classes present in the dataset. While building the model rescaled images to normalize pixel values between (0,1).
  - Chose an appropriate optimiser and loss function for model training
  - Trained the model for ~30 epochs
  - Wrote the findings after the model fit, and commented whether the overfitting and underfitting is fixed or not
- **Class distribution** → Examined the current class distribution in the training dataset 
   - Which class has the least number of samples? **Seaborrheic keratosis least number of samples**
   - Which classes dominate the data in terms of the proportionate number of samples? **Melanoma, pigmented benign keratosis and basal cell carcinoma dominate the samples**
- **Handling class imbalances** → Rectified class imbalances present in the training dataset with Augmentor library.
- **Model Building & training on the rectified class imbalance data** →
  - Created a CNN model, which can accurately detect 9 classes present in the dataset. While building the model, rescale images to normalize pixel values between (0,1).
  - Chose an appropriate optimiser and loss function for model training
  - Trained the model for ~50 epochs
  - Wrote the findings after the model fit, the overfitting was fixed and the accuracy improved

## Conclusions
- Conclusion 1 from the analysis
- Conclusion 2 from the analysis
- Conclusion 3 from the analysis
- Conclusion 4 from the analysis

<!-- You don't have to answer all the questions - just the ones relevant to your project. -->


## Technologies Used
- library - version 1.0
- library - version 2.0
- library - version 3.0

<!-- As the libraries versions keep on changing, it is recommended to mention the version of library used in this project -->

## Acknowledgements
Give credit here.
- This project was inspired by...
- References if any...
- This project was based on [this tutorial](https://www.example.com).


## Contact
Created by [@githubusername] - feel free to contact me!


<!-- Optional -->
<!-- ## License -->
<!-- This project is open source and available under the [... License](). -->

<!-- You don't have to include all sections - just the one's relevant to your project -->