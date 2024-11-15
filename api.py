from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.llms import Ollama

# Initialize FastAPI app
app = FastAPI(
    title="Ollama Text Generation API",
    description="API for generating text using the gemma2 model via Ollama.",
    version="1.0.0"
)

# Define the data model for incoming requests using Pydantic
class Prompt(BaseModel):
    text: str  # The prompt text to generate a response for

@app.post("/generate", summary="Generate Text", response_description="The generated text based on the prompt.")
async def generate_text(prompt: Prompt):
    """
    Generate text based on the provided prompt using the llama2 model.

    - **prompt.text**: The input text prompt.
    """
    # Initialize the Ollama model
    llm = Ollama(model="gemma2:2b")
    
    # Invoke the model with the prompt text
    response = llm.invoke(prompt.text)
    
    # Return the generated text as JSON
    return {"generated_text": response}

if __name__ == "__main__":
    import uvicorn
    # Run the FastAPI app with Uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)