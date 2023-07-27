# Operator SDK

## Getting Started 
You will need an Operator API key to use the SDK. You can request one at https://operator.io. 

## Python

### Installation

Install the package with:

```pip install operatorio```

### Usage

```python
import os
import operatorio
import dotenv

# Use dotenv to load the API key from a .env file 
dotenv.load_dotenv()

# Retrieve the API key from environment variables
api_key = os.environ['OPERATOR_API_KEY']

# Initialize the OperatorSearchAPI with the retrieved API key
api = operatorio.OperatorSearchAPI(api_key)

# Define a Query
query = operatorio.Query(
    query="Bored Ape Yacht Club", # Query for "Bored Ape Yacht Club"
    blockchain="Ethereum", # Query for Ethereum entities
    entity_type=operatorio.EntityType.nft, # Query for NFTs
    query_by=[] # Query by all fields (default)
)

# Use the OperatorSearchAPI to perform the search
entities = api.search(query)

# Print the top result's address
print(entities.matches[0].address)
```

