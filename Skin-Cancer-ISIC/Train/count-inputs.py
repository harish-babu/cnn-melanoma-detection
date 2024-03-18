import os
import pandas as pd
import glob
from pathlib import Path

base_path = "./"
# Specify the root directory
root_dir = os.path.join(base_path, "")

class_names=['actinic keratosis',
 'basal cell carcinoma',
 'dermatofibroma',
 'melanoma',
 'nevus',
 'pigmented benign keratosis',
 'seborrheic keratosis',
 'squamous cell carcinoma',
 'vascular lesion']

data = [(str(j), i) for i in class_names for j in Path(root_dir).glob(i + '/**/*.jpg')]
original_df = pd.DataFrame(data, columns=['Path', 'Label'])
original_df['Label'].value_counts()

# Print the DataFrame
print(original_df['Label'].value_counts())
