from locust import HttpUser, task, between
import random

class OllamaUser(HttpUser):
    """
    A Locust user class that simulates user behavior for testing the /generate endpoint.
    """
    # Wait time between tasks: between 1 to 3 seconds
    wait_time = between(1, 3)

    @task
    def generate_text(self):
        """
        Task to send a POST request to the /generate endpoint with a random prompt.
        """
        # List of sample prompts to choose from
        prompts = [
            "Tell me a joke about programming",
            "Explain quantum computing",
            "Write a haiku about artificial intelligence",
            "What are the benefits of exercise?",
            "Describe the taste of your favorite food"
        ]
        
        # Select a random prompt from the list
        prompt = random.choice(prompts)
        
        # Send a POST request to the /generate endpoint with the selected prompt
        self.client.post("/generate", json={"text": prompt})

if __name__ == "__main__":
    import os
    # Execute the Locust command to start the load test
    os.system("locust -f locustfile.py")