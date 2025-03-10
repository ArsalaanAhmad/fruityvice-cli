# FruityVice CLI

FruityVice CLI is a command-line tool that interacts with the [FruityVice API](https://www.fruityvice.com/api/fruit) to fetch and display fruit data. It supports both human-readable and machine-readable (JSON) output formats.

## Features

- **Fetch Fruit Data:** Retrieve details such as the fruit's name, ID, family, and nutritional information (sugar and carbohydrates).
- **Output Options:** Display output in a human-friendly format or as JSON for machine processing.
- **Error Handling:** Gracefully handles unrecognized fruit names and API connection issues.
- **Modular Design:** Separate client module (`fruityvice_client.py`) for easy library usage and future extensions.
- **Command-Line Interface:** Simple CLI interface for quick lookups.

## Files

  - fruityvice_client.py: Contains the FruityViceClient class, which handles interactions with the FruityVice API.
- main.py: Implements the command-line interface that uses the client to fetch and display fruit data.
  - README.md: This documentation file.
 
## Usage

### Command-Line Interface

To fetch fruit data using the CLI, run:

```bash
python main.py --fruit Banana
```

This displays the fruit data in a human-readable format. To output machine-readable JSON, use:
``` bash
python main.py --fruit Banana --format json
```
## Library Usage
You can also use the FruityViceClient as a library in your own Python projects. For example:
```bash
from fruityvice_client import FruityViceClient

# Initialize the client
client = FruityViceClient()

# Retrieve fruit data
fruit_data = client.get_fruit_info("Banana")

# Check and use the data
if fruit_data:
    print("Fruit Data:", fruit_data)
else:
    print("Fruit not found or an API error occurred.")
```
## Prerequisites

- Python 3.7 or higher.
- The `requests` library. Install it with:
  ```bash
  pip install requests

  
