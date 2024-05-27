# Import necessary libraries
from flask import Flask, request, jsonify
from googletrans import Translator, LANGUAGES
from googletrans.constants import LANGCODES

# Initialize Flask application
app = Flask(__name__)

# Initialize Translator
translator = Translator()

# Endpoint to handle translation requests
@app.route('/translate', methods=['POST'])
def translate_text():
    # Check if request contains JSON data
    if not request.json or 'text' not in request.json:
        return jsonify({'error': 'Invalid request format. JSON data with key "text" is required.'}), 400
    
    # Get the text to translate from the request
    text_to_translate = request.json['text']
    
    # Attempt to translate text to French
    try:
        translation = translator.translate(text_to_translate, dest='fr').text
        return jsonify({'translation': translation})
    except Exception as e:
        return jsonify({'error': f'Translation error: {str(e)}'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
