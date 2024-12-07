from flask import Flask,request,jsonify
import json
import base64
import magic

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask API on Azure!"

@app.route('/process', methods=['POST'])
def process_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the uploaded file temporarily
    file_path = f"./{file.filename}"
    file.save(file_path)

    # Using the magic module to identify the file type
    file_format = identify_file_format(file_path)
    
    # Creating a sample response with file type and base64 encoding
    content = {
        "file_name": file.filename,
        "file_format": file_format,
        "base64_content": encode_file_to_base64(file_path)
    }
    
    return jsonify(content)

# Function to identify file type using magic module
def identify_file_format(file_path):
    mime = magic.Magic(mime=True)
    file_format = mime.from_file(file_path)
    return file_format

# Function to convert file to base64 encoding
def encode_file_to_base64(file_path):
    with open(file_path, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode("utf-8")
    return encoded_string

if __name__ == "__main__":
    app.run(debug=True)

