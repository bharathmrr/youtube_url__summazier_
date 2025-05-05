import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.schema.output_parser import StrOutputParser

# Function to extract transcript
def video_context(video_id):
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
        full_text = " ".join(chunk['text'] for chunk in transcript_list)
        return full_text
    except TranscriptsDisabled:
        return "Transcript is disabled for this video."

# Setup Gemini API
GEMINI_API_KEY = "AIzaSyDjPW2kOBlzvgYIRy9D98I44vI-hXCh_2o"
chatai = GoogleGenerativeAI(api_key=GEMINI_API_KEY, model='gemini-2.0-flash')

# Streamlit UI
st.title("📺 YouTube Video Summarizer & Q&A")

# Input
url = st.text_input("Enter YouTube Video URL:")
if url:
    try:
        video_id = url.split("v=")[1].split("&")[0]  
    except IndexError:
        st.error("Invalid YouTube URL.")
        st.stop()

    context = video_context(video_id)

    # Sidebar options
    option = st.sidebar.selectbox(
        "Select an option",
        ['Just context of YouTube (no modification)', 'Summarizer', 'Questions']
    )

    if option == 'Just context of YouTube (no modification)':
        st.subheader("📄 Raw Transcript")
        st.write(context)

    elif option == 'Summarizer':
        summary_type = st.sidebar.radio("Select Summary Type", ['Long', 'Medium', 'Short'])

        prompt_text = f"Generate a {summary_type.lower()} summary of the following YouTube transcript:\n{{context}}"
        prompt = PromptTemplate(template=prompt_text, input_variables=["context"])
        chain = prompt | chatai | StrOutputParser()

        with st.spinner("Generating summary..."):
            result = chain.invoke({"context": context})
        st.subheader(f"📝 {summary_type} Summary")
        st.write(result)

    elif option == 'Questions':
        num_questions = st.sidebar.slider("Select number of questions", min_value=1, max_value=50, value=5)

        prompt = PromptTemplate(
            template="Generate {number} questions and relavent answers based on the following YouTube transcript:\n{context}",
            input_variables=["number", "context"]
        )
        chain = prompt | chatai | StrOutputParser()

        with st.spinner("Generating questions..."):
            result = chain.invoke({"number": num_questions, "context": context})
        st.subheader("❓ Generated Questions")
        st.write(result)
