# Ollama Text Generation API

A FastAPI-based API for generating text using the `llama2` model via the `Ollama` integration. This project includes load testing capabilities using Locust to ensure the API can handle high traffic efficiently.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the API](#running-the-api)
  - [API Endpoint](#api-endpoint)
- [Load Testing](#load-testing)
  - [Running Locust](#running-locust)
- [Contributing](#contributing)
- [License](#license)

## Features

- **FastAPI**: High-performance web framework for building APIs.
- **Ollama Integration**: Utilize the `llama2` model for text generation.
- **Pydantic**: Data validation and settings management using Python type annotations.
- **Asynchronous Endpoints**: Efficient handling of multiple requests concurrently.
- **Automatic API Documentation**: Interactive Swagger and Redoc documentation.
- **Locust Load Testing**: Simulate multiple users to test API performance.

## Tech Stack

- **Programming Language**: Python 3.8+
- **Framework**: FastAPI
- **Language Model**: Ollama (`llama2`)
- **Data Validation**: Pydantic
- **Load Testing**: Locust

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/ollama-text-generation-api.git
   cd ollama-text-generation-api

*Create a Virtual Environment*

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

*Install Dependencies*

bash
Copy code
pip install -r requirements.txt
If requirements.txt is not present, you can install the necessary packages manually:

bash
Copy code
pip install fastapi uvicorn pydantic langchain-community locust

*Set Up Ollama*

Ensure that the Ollama CLI is installed and the llama2 model is pulled:

bash
Copy code
ollama pull gemma2
Usage
Running the API
Start the FastAPI Server

bash
Copy code
uvicorn main:app --host 0.0.0.0 --port 8000
The API will be accessible at http://0.0.0.0:8000.

Access API Documentation

Swagger UI: http://0.0.0.0:8000/docs
Redoc: http://0.0.0.0:8000/redoc
API Endpoint
POST /generate

*Generates text based on the provided prompt.*

Request Body

json
Copy code
{
  "text": "Your prompt here"
}
Response

json
Copy code
{
  "generated_text": "Generated response from the model."
}
Example

bash
Copy code
curl -X POST "http://0.0.0.0:8000/generate" -H "Content-Type: application/json" -d '{"text": "Tell me a joke about programming"}'

**Load Testing**
Running Locust

*Start the API Server*

Ensure the FastAPI server is running before starting the load tests.

Run Locust

bash
Copy code
python locustfile.py
This command will automatically launch Locust's web UI.

*Access Locust Web UI*

Open your browser and navigate to http://localhost:8089.

Configure the Test

Number of Users: Set the number of concurrent users to simulate.
Spawn Rate: Set how quickly users are spawned.
Host: Ensure it points to your API server (e.g., http://0.0.0.0:8000).
Start the Test

Click the "Start swarming" button to begin the load test. Monitor the performance metrics in real-time.