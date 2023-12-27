# GemCHAT - Gemini LLM Demo
GemCHAT is a Streamlit-based application that utilizes the Gemini Pro Vision model from Google's GenerativeAI to generate content based on user input and images.

## Overview
GemCHAT provides a user-friendly interface for interacting with the Gemini Pro Vision model. Users can upload an image and provide a text query to prompt the model for content generation. The application leverages Streamlit for the frontend and relies on the GenerativeAI library from Google for backend processing.

## Usage
To use GemCHAT, follow these steps:
1. Clone the Repository:
   ```
   git clone https://github.com/your-username/gemchat.git
   cd gemchat
2. Install Dependencies:
   
    ```
    pip install -r requirements.txt
3. Set Up Google API Key:

  Create a .env file in the project directory.
  Add your Google API key:
  
    ```
    GOOGLE_API_KEY=your_api_key_here
  Replace your_api_key_here with your actual Google API key 
  
4. Run the Application:

     ```
     streamlit run gemchat.py
  Open your web browser and navigate to http://localhost:8501 to interact with GemCHAT.

5. Generate Content:

  Upload an image.
  Provide a text query.
  Click the "Ask GemCHAT" button to generate content.
  
## Dependencies
1. Python 3.7+
2. Streamlit
3. Pillow (PIL)
4. Google GenerativeAI
Install the dependencies using the provided requirements.txt file:
      ```
      pip install -r requirements.txt
## Contributing
Contributions to GemCHAT are welcome! If you'd like to contribute, please follow the standard GitHub flow:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes.
4. Create a pull request with a clear description of your changes.

   
## License
This project is licensed under the MIT License.
