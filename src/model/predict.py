import pickle
import joblib
import numpy as np


with open("artifacts/model.pkl",'rb') as f:
    model = pickle.load(f)

def predict(data: list) -> list:
    """
    This will take input data and predict according to the learned parameters(those are saved in model.pkl).
    def predict(data: list):, you are leaving a "hint" for other developers (and your code editor) that says:
    data: list -->  "Hey,this function expects the data argument to be a list. Please don't pass a string or a dictionary here."
    can also hint at what the function returns using an arrow ->. A fully hinted function looks like this:
    """
    arr = np.array(data).reshape(1,-1)
    prediction = model.predict(arr)

    return prediction.tolist()






