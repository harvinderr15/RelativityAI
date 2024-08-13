import streamlit as st
from nlp import NLP
from rag import RAG
from utils import read_pdf
from translation import translate_text
from tts import query_tts

def main():
    # Load the PDF and initialize components
    pdf_path = "relativity.pdf"
    ramayana_text = read_pdf(pdf_path)
    rag = RAG(ramayana_text)
    OPENAI_API_KEY = st.secrets["openai"]["api_key"]
    HF_TTS_API_KEY = st.secrets["huggingface"]["tts_api_key"]
    HF_TRANSLATE_API_KEY = st.secrets["huggingface"]["translate_api_key"]
    nlp = NLP(OPENAI_API_KEY, HF_TTS_API_KEY, HF_TRANSLATE_API_KEY)

    st.title("Relativity AI Chat Bot")



    # Set a default model
    if "openai_model" not in st.session_state:
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if prompt := st.chat_input("Ask me Relativity..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(prompt)

        # Initialize progress bar and spinner
        progress_bar = st.progress(0)
        status_text = st.empty()

        status_text.text("Retrieving passages...")
        with st.spinner("Retrieving passages..."):
            passages = rag.retrieve_passages(prompt)
        context = " ".join(passages)
        progress_bar.progress(33)

        status_text.text("Generating response...")
        with st.spinner("Generating response..."):
            response = nlp.generate_response(context, prompt)
        progress_bar.progress(66)

        status_text.text("Translating response to Hindi...")
        with st.spinner("Translating response to Hindi..."):
            translated_response = translate_text({"inputs": response}, HF_TRANSLATE_API_KEY)
        progress_bar.progress(99)

        translated_text = translated_response[0]['translation_text'] if isinstance(translated_response, list) and len(translated_response) > 0 and 'translation_text' in translated_response[0] else "Translation error"

        # Append assistant responses to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.session_state.messages.append({"role": "assistant", "content": f"Translated (Hindi): {translated_text}"})

        # Display assistant messages in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        with st.chat_message("assistant"):
            st.markdown(f"Translated (Hindi): {translated_text}")

        # Update the progress bar to 100% after displaying the results
        progress_bar.progress(100)
        status_text.text("Completed")

    if st.session_state.messages:
        # Generate TTS for the last assistant response
        last_response = st.session_state.messages[-2]["content"]  # The last message is the translated response, so we take the second last
        status_text.text("Generating TTS...")
        with st.spinner("Generating TTS..."):
            audio_bytes = query_tts({"inputs": last_response}, HF_TTS_API_KEY)
        st.audio(audio_bytes, format="audio/wav")

        # Remove the "Generating TTS..." message
        status_text.empty()

if __name__ == "__main__":
    main()
