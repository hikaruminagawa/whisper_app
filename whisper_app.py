import streamlit as st
import whisper
import tempfile
import os

# Title
st.title("🎙 Whisper Speech-to-Text App")

# Model selection
model_size = st.selectbox("Select model size (balance between speed and accuracy)", ["tiny", "base", "small", "medium", "large"])
st.caption("※ Larger models are more accurate but may take longer to process")

# Audio file upload
uploaded_file = st.file_uploader("Upload an audio file (mp3, wav, m4a, webm)", type=["mp3", "wav", "m4a", "webm"])

if uploaded_file is not None:
    # Save to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.audio(uploaded_file, format='audio/wav')

    if st.button("Start Transcription"):
        with st.spinner("Transcribing..."):
            # Load and run the model
            model = whisper.load_model(model_size)
            result = model.transcribe(temp_path)
            st.success("Transcription completed!")
            st.text_area("📝 Transcription Result", value=result["text"], height=300)

        # Delete the temporary file
        os.remove(temp_path)
```# filepath: /Users/hminagawa/Desktop/whisper_app.py
import streamlit as st
import whisper
import tempfile
import os

# Title
st.title("🎙 Whisper Speech-to-Text App")

# Model selection
model_size = st.selectbox("Select model size (balance between speed and accuracy)", ["tiny", "base", "small", "medium", "large"])
st.caption("※ Larger models are more accurate but may take longer to process")

# Audio file upload
uploaded_file = st.file_uploader("Upload an audio file (mp3, wav, m4a, webm)", type=["mp3", "wav", "m4a", "webm"])

if uploaded_file is not None:
    # Save to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=uploaded_file.name) as tmp_file:
        tmp_file.write(uploaded_file.read())
        temp_path = tmp_file.name

    st.audio(uploaded_file, format='audio/wav')

    if st.button("Start Transcription"):
        with st.spinner("Transcribing..."):
            # Load and run the model
            model = whisper.load_model(model_size)
            result = model.transcribe(temp_path)
            st.success("Transcription completed!")
            st.text_area("📝 Transcription Result", value=result["text"], height=300)

        # Delete the temporary file
        os.remove(temp_path)
