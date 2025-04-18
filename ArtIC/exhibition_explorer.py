import requests
import json
import sys

BASE_URL = "https://api.artic.edu/api/v1"


def search_exhibitions(term: str) -> list[int]:
    """Make a request to exhibitions/search for the search term,
    using Elasticsearch `exists` option to only return results where the `artwork_titles` field is not empty
    Process the result and return a list of exhibitions IDs.
    """
    url = f"{BASE_URL}/exhibitions/search"
    params = {
        "q": term,
        "query": {"bool": {"must": [{"exists": {"field": "artwork_titles"}}]}},
    }

    try:
        response = requests.post(url, json=params)
        response.raise_for_status()
        data = response.json()

        # Extract exhibition IDs
        exhibition_ids = [item["id"] for item in data.get("data", [])]
        return exhibition_ids
    except requests.exceptions.RequestException as e:
        print(f"Error searching exhibitions: {e}")
        return []


def get_exhibition_details(exhibition_id: int) -> dict:
    """Get detailed information about a specific exhibition by ID."""
    url = f"{BASE_URL}/exhibitions/{exhibition_id}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json().get("data", {})
    except requests.exceptions.RequestException as e:
        print(f"Error getting exhibition details: {e}")
        return {}


def display_exhibition_info(exhibition: dict):
    """Display formatted information about an exhibition."""
    print("\n" + "=" * 50)
    print(f"Title: {exhibition.get('title', 'N/A')}")
    print(f"Status: {exhibition.get('status', 'N/A')}")
    print(f"Short Description: {exhibition.get('short_description', 'N/A')}")

    # Display artwork titles
    artwork_titles = exhibition.get("artwork_titles", [])
    if artwork_titles:
        print("\nArtwork Titles:")
        for i, title in enumerate(artwork_titles, 1):
            print(f"  {i}. {title}")
    else:
        print("\nNo artwork titles available for this exhibition.")

    print("=" * 50 + "\n")


def main():
    print("Welcome to the Art Institute of Chicago Exhibition Explorer!")

    while True:
        # Get search term from user
        search_term = input(
            "\nEnter a search term for exhibitions (or 'quit' to exit): "
        )
        if search_term.lower() == "quit":
            print("Thank you for using the Exhibition Explorer. Goodbye!")
            sys.exit(0)

        # Search for exhibitions
        print(f"Searching for exhibitions related to '{search_term}'...")
        exhibition_ids = search_exhibitions(search_term)

        if not exhibition_ids:
            print("No exhibitions found matching your search term. Please try again.")
            continue

        print(f"Found {len(exhibition_ids)} exhibitions with artwork titles.")

        # Ask how many exhibitions to view
        while True:
            try:
                num_to_view = input(
                    f"How many exhibitions would you like to view (1-{len(exhibition_ids)}, or 'all'): "
                )
                if num_to_view.lower() == "all":
                    num_to_view = len(exhibition_ids)
                else:
                    num_to_view = int(num_to_view)

                if 1 <= num_to_view <= len(exhibition_ids):
                    break
                else:
                    print(f"Please enter a number between 1 and {len(exhibition_ids)}.")
            except ValueError:
                print("Please enter a valid number or 'all'.")

        # Display the selected number of exhibitions
        for i in range(min(num_to_view, len(exhibition_ids))):
            exhibition_id = exhibition_ids[i]
            exhibition_details = get_exhibition_details(exhibition_id)
            display_exhibition_info(exhibition_details)


if __name__ == "__main__":
    main()
