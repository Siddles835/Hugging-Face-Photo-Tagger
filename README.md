# Hugging-Face-Photo-Tagger
Welcome to the Photo Tagger Demo! Here, we have a program that allows you to select an image and test it for AI bias in Algorithms. This project uses an API from Hugging Face to explore potential **biases in image labeling in certain algorithms.

# Features

- Upload any image (JPG or PNG)
- Automatically retrieves and displays labels from Hugging Face API
- Displays confidence scores for each label
- Built with Streamlit for a lightweight, interactive interface
- One of **Many** examples of bias shown in AI
- **Zero** training needed

# Project Structure
app.py - Where you deploy your streamlit and make your code for the photo tagger
requirements.txt - The necessary libraries that we need to import related to AI, ML, and Images

# Step by step guide
1. **Clone the Repository**
git clone https://github.com/yourusername/flawed-photo-tagger.git
cd hugging-face-photo-tagger

2. **Install Dependencies**

pip install -r requirements.txt

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt

3. **Create a Hugging Face Account and API Token**
   Go to huggingface.co.
   Create an account or log in.
   Navigate to Settings > Access Tokens.
   Click New Token, select “read” permissions, and copy the token.

This token will allow your app to access Hugging Face models securely.

# IMPORTANT NOTE: DO NOT SHARE YOUR API TOKEN, THIS SHOULD BE KEPT PRIVATE

4. **Understand the Model**
This app uses the microsoft/beit-base-patch16-224 model — a powerful Vision Transformer trained on ImageNet. It can recognize hundreds of common objects and concepts. You won’t need to train anything — just send the image and receive predictions.

5. **Run the App**
Once setup is complete, you can launch the app using a single command. The app will open in your browser, where you can interactively upload images and get AI-generated tags instantly.
**Here is the command:** streamlit run app.py

6. **Explore the Bias**
   Once you run the app and everything works, you will start to see AI label some images with different names than you probably expect. Some of those names can at times be offensive, especially toward a certain group of people. Keep adding different types of images and try to recognize patterns.

This is created by: Siddles835 (Sidhaanth Kapoor)
