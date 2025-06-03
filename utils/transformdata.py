#Import dependencies
import pandas as pd
import pickle
from pathlib import Path
from sklearn.feature_extraction.text import CountVectorizer , TfidfVectorizer
from sklearn.model_selection import train_test_split
datapath = Path("../datasets/allsymptomsdisease.csv")
data = pd.read_csv(datapath)

# Binning function

def binner(scores):
    output = []
    for score in scores:
        if score > 900:
            output.append(1)
        elif score > 675:
            output.append(2)
        elif score > 375:
            output.append(3)
        elif score > 100:
            output.append(4)
        else:
            output.append(5)
    return output


# Binning the dataframes and renaming them
data = data.rename(columns = {"text": "Text", "label" : "Label"})

data["Label"] = binner(data['Label'])


#Vectorize data
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(data["Text"])
y = data["Label"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)


with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)