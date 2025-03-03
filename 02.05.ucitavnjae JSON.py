# Load library
import pandas as pd
# Create URL
url = 'https://api.github.com/users?since=0'
# Load data
dataframe = pd.read_json(url)
# View the first two rows
print(dataframe.head(200))