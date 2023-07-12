import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import f1_score
from sklearn.feature_extraction.text import TfidfVectorizer
import json
import re

excel_data_path = 'data/chitchat(formal).xlsx'
json_tag_path = 'data/intentsDataset(formal).json'

# Load the intents from the JSON file
with open(json_tag_path) as file:
    data = json.load(file)
    intents = data['intents']

# Convert the intents into a hashtable
tag_responses = {intent['tag']: intent['responses'] for intent in intents}

# Load the dataset from Excel
df = pd.read_excel(excel_data_path)

# Define a regular expression pattern to match non-English characters
non_english_pattern = re.compile(r'[^a-zA-Z ]')

# Apply lowercase and remove non-English words for the 'text' column
df['text'] = df['text'].apply(lambda x: re.sub(non_english_pattern, '', x.lower()))

# Separate the features (text) and labels (categories)
X = df['text'].values
y = df['label'].values

# Delete the df object to free up memory
del df

# Convert text data to a sparse matrix representation. stop_words='english'
vectorizer = CountVectorizer()
#vectorizer = TfidfVectorizer()
X_sparse = vectorizer.fit_transform(X)

# Split the data into training and testing sets
# You can adjust the test_size and random_state values as per your needs
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_sparse, y, test_size=0.2, random_state=42)

# Train the Multinomial Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Predict on the test set
y_pred = classifier.predict(X_test)

# Calculate the F1 score
f1 = f1_score(y_test, y_pred, average='weighted')

# Print the F1 score
print("F1 Score:", f1)

print('y_pred[0] type: ', type(y_pred[0]))

# def nb_response(msg):
#     msg_sparse = vectorizer.transform([msg])
#     res_pred = classifier.predict(msg_sparse)
#     return res_pred[0]

def nb_response(msg):
    msg = re.sub(non_english_pattern, '', msg.lower())
    msg_sparse = vectorizer.transform([msg])
    res_pred = classifier.predict(msg_sparse)
    tag = res_pred[0]
    if tag in tag_responses:
        return tag_responses[tag], tag
    else:
        return "Tag not found in the hashtable.", "No Tag"

print("nb: ", 'type ', type(nb_response("hospice care for end-stage kidney disease?")), 
      "\n", nb_response("hospice care for end-stage kidney disease?"))


## ------------------------ ##

# # console input
# while True:
#     user_input = input("Enter a message (or 'stop' to exit): ")
#     if user_input.lower() == "stop":
#         break
#     else:
#         print("nb: ", nb_response(user_input))

# # Save the trained model to a file
# with open(savemodel_path, 'wb') as file:
#     pickle.dump(classifier, file)

# # Load the saved model
# with open(savemodel_path, 'rb') as file:
#     clsfier = pickle.load(file)