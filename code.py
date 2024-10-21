import pandas as pd
import numpy as np
import matplotlib.pyplot as mlt
import seaborn as sns

## Data
data ={
    't': [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'icd-teu': [0.991, 0.949, 1.089, 1.116, 1.260, 1.493, 1.653, 1.847, 1.802, 1.815, 1.950, 2.277, 2.316, 2.168],
    'ctg-teu': [1.343, 1.392, 1.406, 1.542, 1.731, 2.024, 2.422, 2.667, 2.904, 3.088, 2.840, 3.215, 3.143, 3.006]
    }

df = pd.DataFrame(data)

df.head()

## Create variables
df["icd-share"] = df["icd-teu"]/df["ctg-teu"]*100

