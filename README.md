# SDK's to interact with the Operator API

## Python

### Installation

Install the package with:

```pip install operator-search```

### Usage

```python
from operator_search import OperatorSearchAPI, Query, EntityType

# Create a client instance
client = OperatorSearchAPI('your-api-key')

# Define your query
query = Query(
    query='Bored Ape Yacht Club',
    blockchain='Ethereum',
    entity_type=EntityType.NFT
)

# Perform the search
response = client.search(query)

# Print the address of the top match
print(f"Top Match Address: {response.matches[0].address}")
```

