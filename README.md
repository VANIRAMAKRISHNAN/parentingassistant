# parentingassistant
ChatGPT based AI application to enable parents to make use of AI for getting questions regarding their kids clarified in multilingual languages

# Overview

Parenting Assistant is an AI-powered application developed to provide real-time assistance to parents. The application is capable of answering questions about parenting in different regional languages using OpenAI's GPT LLM and Microsoft's Translator API. This project is inspired by mothers of newborn kids who may need assistance during off-hours when the baby is crying, and it can also track a child's progress.

# Features

Ask questions about parenting in your preferred language.
Get instant AI-powered responses.
Easy-to-use UI.

# Pre-reqisites

Generate API key for OpenAI GPT
Generate API keys, note down region and endpoint for Translator API in Azure

# Setup

1. Create a Azure VM (Ubuntu)
2. Clone the code
      git clone https://github.com/yourusername/parenting-assistant.git
      cd parenting-assistant
4. Update the app.py program with OpenAPI api key and Translator API key and region
5. Install the below packakges/dependencies using: pip install -r requirements.txt command
6. Install Docker
7. Build Docker image and run as container using below 2 commands:
      docker build -t parenting-assistant .
      docker run -p 80:80 parenting-assistant
      
 # Usage

    Open your browser and visit http://localhost.
    Type your question in the provided field and press "Ask" in your preferred language.
    The AI will respond to your question in the chatbox in your preferred language
