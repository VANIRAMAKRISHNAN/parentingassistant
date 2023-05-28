import os
import openai
import requests
import uuid
import json
from flask import Flask, render_template, request, jsonify, send_file

app = Flask(__name__)
openai.api_key = "provide openai api key"

# Set up Azure translator
subscription_key = 'provide translator key'
endpoint = 'https://api.cognitive.microsofttranslator.com/'
location = 'provide region'

def translate(input_text, target_language):
    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'en',
        'to': [target_language]
    }

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{'text': input_text}]

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    return response[0]['translations'][0]['text']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()  # Use get_json() since we're sending JSON
    question = data['question']
    language = data['language']

    # Translate question to English
    question_in_english = translate(question, 'en')

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"Parenting question: {question_in_english}\nAnswer:",
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    answer = response.choices[0].text.strip()

    # Translate answer to the chosen language
    answer_in_chosen_language = translate(answer, language)

    return jsonify({'answer': answer_in_chosen_language})

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
