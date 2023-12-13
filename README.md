# ChatBot for PDF Interaction

#### Video Demo: <https://youtu.be/NJjIPksbp0c>

#### Description:

This project is a simple chatbot implemented using Streamlit for the user interface and Google Palm as the backend. The primary functionality of the chatbot is to facilitate conversations with PDF documents that users upload.

## Features:

1. **PDF Interaction:** Upload any PDF document, and the chatbot will provide information, answer questions, or engage in discussions based on the content of the document.

2. **User-Friendly Interface:** The frontend is built with Streamlit, providing an intuitive and easy-to-use interface for interacting with the chatbot.

3. **Google Palm Integration:** Leveraging the power of google Palm, the chatbot utilizes advanced natural language processing capabilities to understand and respond to user queries related to the uploaded PDF.

4. **Conversational Experience:** Engage in dynamic conversations with the chatbot, making it a versatile tool for extracting information and insights from PDF documents.

## Usage:

1. **Configuration:**
    - Create a `config.py` file in the project directory.
    - Insert your google Palm API key in the following format:
        ```python
        # config.py
        API_KEY = "your_api_key"
        ```

2. **Upload PDF:** Click the upload button to select and upload a PDF document.

3. **Start Chat:** Initiate a conversation with the chatbot by typing your queries or providing instructions related to the uploaded PDF.

4. **Receive Responses:** The chatbot will analyze the PDF content and provide relevant responses, allowing for a seamless and informative interaction.

## Installation:

To run the project locally, follow these steps:

```bash
# Clone the repository
git clone https://github.com/yourusername/your-project.git

# Navigate to the project directory
cd your-project

# Install dependencies
pip install -r requirements.txt

# Create config.py and insert your google Palm API key
echo "API_KEY = 'your_api_key'" > config.py

# Run the Streamlit app
streamlit run project.py
