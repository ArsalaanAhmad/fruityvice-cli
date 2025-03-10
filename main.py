import argparse
import json
import sys

from fruityvice_client import FruityViceClient


def format_human_readable(fruit_data: dict) -> str:
    """
    Formats the fruit data in a human-readable string.

    :param fruit_data: Dictionary containing fruit information.
    :return: A string with name, ID, family, sugar, and carbohydrates.
    """
    name = fruit_data.get("name", "Unknown")
    fruit_id = fruit_data.get("id", "Unknown")
    family = fruit_data.get("family", "Unknown")
    nutritions = fruit_data.get("nutritions", {})
    sugar = nutritions.get("sugar", "Unknown")
    carbs = nutritions.get("carbohydrates", "Unknown")

    lines = [
        f"Fruit Name: {name}",
        f"Fruit ID: {fruit_id}",
        f"Family: {family}",
        f"Sugar (g): {sugar}",
        f"Carbohydrates (g): {carbs}"
    ]
    return "\n".join(lines)


def main():
    """
    Main entry point for the CLI. Parses arguments, retrieves fruit data, and prints output.
    """
    parser = argparse.ArgumentParser(
        description="Fetch fruit data from FruityVice and display it."
    )
    parser.add_argument(
        "--fruit",
        required=True,
        help="The name of the fruit to look up (e.g., 'Banana', 'Strawberry')."
    )
    parser.add_argument(
        "--format",
        choices=["human", "json"],
        default="human",
        help="Output format: 'human' (default) or 'json'."
    )

    args = parser.parse_args()
    fruit_name = args.fruit

    # Initialize the FruityVice client
    client = FruityViceClient()

    try:
        fruit_data = client.get_fruit_info(fruit_name)
    except RuntimeError as e:
        print(f"[ERROR] Could not retrieve data: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"[ERROR] Parsing error: {e}")
        sys.exit(1)

    # If None, fruit is likely not recognized or data structure changed
    if fruit_data is None:
        print("[ERROR] The requested fruit was not found or the API response is invalid.")
        sys.exit(1)

    # Output
    if args.format == "human":
        print(format_human_readable(fruit_data))
    else:
        print(json.dumps(fruit_data, indent=2))


if __name__ == "__main__":
    main()