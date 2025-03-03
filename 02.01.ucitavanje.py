# Load scikit-learn's datasets
from sklearn import datasets
import matplotlib.pyplot as plt
# Load digits dataset 2
digits = datasets.load_digits()
# Create features matrix
features = digits.data
# Create target vector
target = digits.target
# View first observation
print(features[0])
plt.gray()
plt.matshow(digits.images[0])
plt.show()
