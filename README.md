

### RelativityAI: Einstein's Relativity AI Chat Bot

DocuAssist is an AI-powered chatbot designed to assist users with document-based queries, focusing initially on Albert Einstein's "Relativity: The Special and General Theory." Here’s how different components work together and how you can use this project:

#### Components Used:

1. **PDF Reader (`read_pdf` function):**
   - Reads the "Relativity: The Special and General Theory.pdf" file and extracts text from it using PyPDF2. This text serves as the corpus for the chatbot.

2. **Retrieval-Augmented Generation (RAG) (`RAG` class):**
   - The `RAG` class is initialized with the extracted text from the Einstein PDF. It provides a method `retrieve_passages` which, given a query, retrieves relevant passages from the Einstein text. For demo purposes, it returns the first 1000 characters of the text as a passage.

3. **Natural Language Processing (NLP) (`NLP` class):**
   - Handles the generation of responses based on user queries using OpenAI's GPT-3.5 model (`gpt-3.5-turbo`). It generates responses based on the context provided by the retrieved passages and the user's query.

4. **Translation (`translate_text` function):**
   - Utilizes the Opus-MT model hosted on Hugging Face for translating responses from English to Hindi. This allows the chatbot to respond in both English and Hindi.

5. **Text-to-Speech (TTS) (`query_tts` function):**
   - Uses the MMS-TTS model from Hugging Face to convert the chatbot's responses into audio format. This enables the chatbot to audibly communicate its responses to users.

#### Functionality:

- **User Interaction:**
  - Users interact with the chatbot by asking questions related to Einstein's theories via a Streamlit interface.
  - The chat history is maintained and displayed on each interaction, showing both user queries and the chatbot's responses.

- **Response Generation Flow:**
  - When a user inputs a query, the chatbot first retrieves relevant passages from the Einstein text using the RAG component.
  - It then generates a response using NLP, incorporating the retrieved passages and the user's query.
  - The response is translated into Hindi using the translation component, enhancing accessibility for Hindi-speaking users.
  - Finally, the translated response is converted to speech using the TTS component, providing an audio response to the user.

#### How to Use:

1. **Clone the Repository:**
   - Clone the repository to your local machine:
     ```
     git clone https://github.com/harvinderr15/RelativityAI
     ```

2. **Configuration:**
   - Navigate to the project directory and ensure you have a `secrets.toml` file with the following structure:
     ```toml
     [openai]
     api_key = "YOUR_OPENAI_API_KEY"
     
     [huggingface]
     translate_api_key = "YOUR_HUGGINGFACE_TRANSLATION_API_KEY"
     tts_api_key = "YOUR_HUGGINGFACE_TTS_API_KEY"
     ```
     Replace `"YOUR_OPENAI_API_KEY"`, `"YOUR_HUGGINGFACE_TRANSLATION_API_KEY"`, and `"YOUR_HUGGINGFACE_TTS_API_KEY"` with your actual API keys from OpenAI and Hugging Face.

3. **Dependencies:**
   - Install the required Python dependencies by running:
     ```
     pip install -r requirements.txt
     ```

4. **Running the Application:**
   - Execute the `main.py` script:
     ```
     streamlit run main.py
     ```
   - This will start a Streamlit server and open the application in your default web browser.

5. **Interacting with the Chat Bot:**
   - Once the application is running, interact with the chatbot by typing questions related to Einstein's theories into the input box provided.

6. **Feedback and Contributions:**
   - Feel free to explore the codebase, make improvements, or provide feedback. Contributions are welcome via pull requests.

#### Project Focus:

DocuAssist leverages AI technologies to provide an interactive and educational experience focused on document-based queries, starting with Einstein's "Relativity: The Special and General Theory" in this implementation. By integrating RAG for context retrieval, NLP for response generation, and translation and TTS for multilingual and auditory outputs, the chatbot aims to assist users in understanding and exploring Einstein's theories.

#### Future Improvements:

- Implement advanced methods for passage retrieval within RAG to enhance relevance and accuracy.
- Expand language translation capabilities to support additional languages beyond English and Hindi.
- Enhance TTS functionality for clearer and more natural audio responses.

