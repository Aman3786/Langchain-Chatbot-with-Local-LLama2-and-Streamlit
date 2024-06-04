# Langchain ChatBot with Local LLAMA-2 & Streamlit
This repository contains a Streamlit application that uses the Langchain library to create a chatbot interface with the LLAMA-2 model locally. The chatbot, named `Mario`, is designed to be a helpful assistant that responds to user questions.
## Tech Stack
- **Python**: Python is an interpreted, object-oriented, high-level programming language.
- **Streamlit**: An open-source app framework for Machine Learning and Data Science projects.
- **Langchain Core**: Provides tools and components to build complex prompt chains.
- **Langchain Community**: Community-driven extensions and integrations for Langchain.
- **LLAMA-2**: LLama 2 is a pre-trained and fine-tuned large language models (LLMs) released by Meta AI in 2023. Released free of charge for research and commercial use, Llama 2 AI models are capable of a variety of natural language processing (NLP) tasks, from text generation to programming code. It comes with `Ollama` tool to run it locally

## Code Explanation
The main code in this repository sets up a Streamlit application with the following key components:
1. **Environment Setup**:
    - Uses `dotenv` to load environment variables from a `.env` file during development.
    - Sets up necessary environment variables for Langchain API and tracing.
2. **Prompt Template**:
    - Creates a `ChatPromptTemplate` to structure the input and define the model's behavior.
3. **Model and Parser**:
    - Initializes the LLAMA-2 model using the `Ollama` class.
    - Uses `StrOutputParser` to handle the output from the model.
4. **Chains**:
    - Uses Chain from langchain for sequencing of Prompts, llm model, o/p parser
6. **Streamlit UI**:
    - Sets up the Streamlit user interface with a title and text input field.
    - Displays the model's response to the user's query.

## Requirements
Ensure the following packages are listed in your `requirements.txt` file:
```plaintext
streamlit
python-dotenv
langchain-core
langchain-community
```

## Running the Code
To run this code locally, follow these steps:
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Aman3786/Langchain-Chatbot-with-Local-LLama2-and-Streamlit.git
    cd Langchain-Chatbot-with-Local-LLama2-and-Streamlit
    ```
2. **Set Up Environment Variables**:
    - Create a `.env` file in the root of your project and add your Langchain API key:
    ```env
    LANGCHAIN_API_KEY="your_api_key_here"
    ```
3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run the Streamlit Application**:
    ```bash
    streamlit run app.py
    ```

## Deployment Instructions
For deployment, make sure to:
- Comment out or remove the `load_dotenv()` line and the lines setting `LANGCHAIN_TRACING_V2` and `LANGCHAIN_API_KEY` directly in the code.
- Set environment variables securely through your deployment platform (e.g., HuggingFace, AWS, GCP & more).

## Local Run Images

![image (21)](https://github.com/Aman3786/Langchain-Chatbot-with-Local-LLama2-and-Streamlit/assets/53119534/aecacb69-e2ab-4831-bc16-c4b6419882b3)

![image (22)](https://github.com/Aman3786/Langchain-Chatbot-with-Local-LLama2-and-Streamlit/assets/53119534/5fdb9e60-aab7-4a91-806b-f557c716611c)
