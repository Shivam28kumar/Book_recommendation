from mira_sdk import MiraClient, Flow
from mira_sdk.exceptions import FlowError
from dotenv import load_dotenv
import os

# Load environment variables from .env file if necessary
load_dotenv()

# Initialize the client with your API key
client = MiraClient(config={"API_KEY": "sb-f915fc31d83eed93780402d2eec45787"})

# Load the book recommendation flow from flow.yaml
flow = Flow(source="flow.yaml")

try:
    # Deploy the flow
    client.flow.deploy(flow)
    print("Book Recommendation Flow deployed successfully!")

except FlowError as e:
    # Handle deployment errors
    print(f"Error occurred: {str(e)}")

except Exception as e:
    # General error handling for issues like 404
    print(f"Deployment failed with error: {str(e)}")
