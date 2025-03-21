# Smart-Cooking-assistance-


prepared by: Atha Alghamdi- Aghadir Jammah

 - Smart Cooking Assistant

Is an interactive web application that helps users create food recipes based on the ingredients they have. The app utilizes AI to recognize ingredients from images and suggest suitable recipes, with the ability to generate images of the suggested dishes.

Contents

	•	Introduction
	•	Requirements
	•	Installation
	•	Usage
	•	Technologies Used
	•	Contribution
	•	License

Introduction

The application analyzes an image of ingredients using Roboflow, then utilizes Gemini AI to generate recipes based on the detected ingredients. Additionally, it can create images of the suggested dishes using the Hugging Face Inference API.

Requirements

The following tools and libraries must be installed before running the project:
	•	Python 3.8+
	•	Required Python libraries:

pip install streamlit opencv-python numpy roboflow google-generativeai huggingface_hub


	•	Roboflow API Key
	•	Gemini AI API Key
	•	Hugging Face Inference API Key

Installation

Follow these steps to install and run the project locally:

git clone https://github.com/username/smart-cooking-assistant.git
cd smart-cooking-assistant
pip install -r requirements.txt
streamlit run app.py

Usage

	1.	Open the app by running:

streamlit run app.py


	2.	Click the Start button and log in with your username.
	3.	Upload an image containing your food ingredients.
	4.	The app will recognize the ingredients and display a list.
	5.	Select the ingredients you want to use, then click Make Recipes.
	6.	Wait for the recipes to be generated and view the suggested dish images.

Technologies Used

	•	Streamlit – For creating an interactive user interface.
	•	OpenCV – For image processing.
	•	Roboflow API – To detect food ingredients from images.
	•	Google Gemini AI – To generate cooking recipes based on ingredients.
	•	Hugging Face Inference API – To generate images of dishes based on recipes.
