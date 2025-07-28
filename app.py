import streamlit as st
import requests
from PIL import Image
import io
import time
import json

API_URL = "YOUR API"
headers = {
    "YOUR HEADERS"
}

def query_huggingface(image_bytes):
    try:
        response = requests.post(API_URL, headers=headers, data=image_bytes)

        if response.status_code == 503:
            return {"status": "loading", "message": "Model is loading, please wait."}
        elif response.status_code != 200:
            try:
                error_data = response.json()
                error_message = error_data.get('error', error_data.get('detail', 'Unknown API error')) or "No specific error message provided by API."
                return {"error": f"API Error ({response.status_code}): {error_message}"}
            except json.JSONDecodeError:
                return {"error": f"API Error ({response.status_code}): {response.text}"}

        try:
            json_response = response.json()
            if json_response is None:
                return {"error": "API returned an empty or null JSON response."}
            return json_response
        except json.JSONDecodeError as e:
            return {"error": f"Failed to decode JSON: {e}. Response: {response.text[:200]}..."}

    except requests.exceptions.RequestException as e:
        return {"error": f"Network or request error: {e}"}
    except Exception as e:
        return {"error": f"Unexpected error: {e}"}

st.set_page_config(page_title="Flawed Photo Tagger", layout="wide")
st.title(" Flawed Photo Tagger – Bias Exploration with Vision AI")
st.write("Upload an image and explore how a computer vision model labels it. This tool helps investigate potential bias.")

uploaded_file = st.file_uploader(" Upload an image (JPG or PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner(" Analyzing image with Hugging Face model..."):
        buf = io.BytesIO()
        image.save(buf, format="JPEG")
        image_bytes = buf.getvalue()

        retry_count = 0
        max_retries = 5
        output = query_huggingface(image_bytes)

        # Retry logic for model loading
        while isinstance(output, dict) and output.get("status") == "loading" and retry_count < max_retries:
            st.info(f"⏳ {output.get('message', 'Model is still loading')}. Retrying in 5 seconds...")
            time.sleep(5)
            output = query_huggingface(image_bytes)
            retry_count += 1

        if isinstance(output, dict) and output.get("status") == "loading":
            st.error(" Model did not load in time. Please try again later.")
        elif isinstance(output, list):
            st.success(" Model Predictions:")
            for item in output:
                label = item.get('label', 'N/A')
                score = item.get('score', 0.0)
                st.markdown(f"- **{label}** — Confidence: `{score:.2%}`")
        elif isinstance(output, dict) and "error" in output:
            st.error(f"Error from API: {output['error']}")
        else:
            st.warning(" Unexpected API response format. Try again or upload a different image.")
            st.json(output)
