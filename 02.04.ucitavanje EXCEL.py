# Load library
import pandas as pd
# Create URL
url = 'https://github.com/datagy/mediumdata/raw/master/Sales.xlsx'
# Load data
dataframe = pd.read_excel(url)
# View the first two rows
print(dataframe.head(20))