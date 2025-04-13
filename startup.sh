#!/bin/bash

# ffmpegが入ってない環境でも使えるようにするならこのへんに追加もOK
streamlit run whisper_app.py --server.port=$PORT --server.enableCORS=false
