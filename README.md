# Naive Bayes ChatBot

Create an interactive web chatbot using the Naive Bayes Model and a custom dataset.

## Overview

The Naive Bayes ChatBot project demonstrates the implementation of a web-based chatbot powered by the Naive Bayes Model. By utilizing this probabilistic classifier, the chatbot is designed to understand user messages and respond with contextually relevant answers. The project also incorporates the Flask framework to provide a seamless web interface.

## Features

- Leveraging Naive Bayes: The chatbot's underlying engine employs the Naive Bayes Model to categorize and predict responses based on input messages. This model is trained on a custom dataset tailored to the desired chatbot behavior.

- Web Interface with Flask: The project integrates the Flask web framework, enabling the creation of an interactive web interface. Users can easily input messages and receive responses directly within the web browser.

- Custom Dataset: The chatbot's responses are derived from a custom dataset provided by the user. The dataset includes labeled messages and corresponding categories, enabling the Naive Bayes Model to learn and generalize patterns for accurate predictions.

## Installation

Before running the code, ensure you have the required packages installed. You can install them using the `requirements.txt` file.

## Usage

1. Prepare Your Dataset:
- Create an "Excel file" containing user messages and corresponding labels (categories).
- Prepare a "JSON file" with intents, including tags and potential responses for the chatbot.

2. Configure Dataset Paths:
- Update the `excel_data_path` and `json_tag_path` variables in the `model_NB.py` file to point to your dataset files.

3. Train the Model:
- Run the `model_NB.py` script to preprocess the dataset, train the Naive Bayes Model, and evaluate its performance.

4. Run the Flask App:
- Execute the `app_1.py` script to launch the Flask web application.
- Access the chatbot interface by visiting http://localhost:5000/ in your web browser.

## Frameworks and Tools Used

- Flask: A lightweight web framework used to create the chatbot's interactive web interface.
- Scikit-learn: A machine learning library employed for training the Naive Bayes Model and performing text classification tasks.

This project combines machine learning techniques and web development to offer an interactive and educational chatbot experience. Explore the potential of the Naive Bayes Model and witness the chatbot's ability to generate contextually relevant responses.

## License

This project is licensed under the MIT License. You can find more details in the LICENSE file.

---

**Note:** This project is intended for educational purposes and can be further extended to enhance chatbot capabilities and improve model accuracy.


