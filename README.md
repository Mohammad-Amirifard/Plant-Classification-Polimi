
# Rpository Structure:
```
- 📦 Plant Classification problem
  |- 📄 README.md        #Guide file
  |- 📂 data             #Here you can see dataset link.
  |- 📂 notebooks        #Here you can see jupyter files which should be run on Google Colab.
  |- 📂 submission       #Here you can see a zip file link which is appropraite to upload in Coda Lab
  |- 📂 report           #Here you can see a complete report of what we have done.
```


# Project Detail

**Problem**: Categorizing Healthy Plants Vs Unhealthy ones 

**Goal**: The task is to develop a model that is able to classify plants that are divided into two categories according to their state of health. It is a binary classification problem, so the goal is to predict the correct class label in {0, 1}.

# Dataset Detail:
**Image size:** 96x96
**Color space:** RGB
**File Format:** npz
**Number of classes:** 2
**Classes:**
0: "healthy"
1: "unhealthy"

# Dataset Structure:
containing the 'public_data.npz' file. The file contains the following items:
'data': numpy array of shape 5100x96x96x3, containing the RGB images.
'data': 3-dimensional numpy array of shape 5200x96x96x3, containing the RGB images.
'labels': 1-dimensional numpy array of shape 5200 with values in {'healthy', 'unhealthy'}

# Data Download:
You can access and download dataset from this [link](https://drive.google.com/file/d/1fA3GMxgyhNHlPKDiwlkYhoJZFpAqVAMb/view?usp=sharing).

# Data Loading:
The provided dataset is in zip format. 


**You should run notebooks, using google colab platforms. Since they have been written in this platforms.**


