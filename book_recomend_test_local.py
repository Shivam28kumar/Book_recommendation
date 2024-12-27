from mira_sdk import MiraClient, Flow
from dotenv import load_dotenv
import os

# Load environment variables from .env file if needed
# load_dotenv(r"path_to_your_env_file")

# Initialize the Mira client with your API key
client = MiraClient(config={"API_KEY": "sb-f915fc31d83eed93780402d2eec45787"})

# Load the book recommendation flow from flow.yaml
flow = Flow(source="flow.yaml")

# Define the user inputs for book recommendations
input_dict = {
    "genre": "Mystery",
    "author": "Agatha Christie",
    "style": "Fast-paced",
    "length": "300-400 pages",
    "previous_book": "The Da Vinci Code"
}

# Test the flow with the provided inputs
response = client.flow.test(flow, input_dict)

# Print the response with the book recommendations
print(response)
