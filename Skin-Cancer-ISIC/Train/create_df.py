import os
import pandas as pd

# Initialize an empty list to store the data
data = []

# Specify the root directory
root_dir = '.'

# Walk through the directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    # Check if there are files in the directory
    if filenames:
        # Get the label from the directory name
        label = os.path.basename(os.path.dirname(dirpath)) if os.path.basename(dirpath) == 'output' else os.path.basename(dirpath)
        # Iterate over each file
        for filename in filenames:
            # Check if the file is a jpg file
            if filename.endswith('.jpg'):
                # Get the full path of the file
                filepath = os.path.join(dirpath, filename)
                # Append the data to the list
                data.append([filepath, label])

# Create a DataFrame from the data
df = pd.DataFrame(data, columns=['Filepath', 'Label'])

# Print the DataFrame
print(df['Label'].value_counts())
