import requests
def search_show(title):
    url = f"https://api.tvmaze.com/singlesearch/shows?q={title}"
    # Send the request to the API
    response = requests.get(url)

    # Check if the request succeeded
    if response.status_code == 200:
        data = response.json()  # Convert the response to a Python dictionary
        print(f"\nTitle: {data['name']}")
        print(f"Genres: {', '.join(data['genres'])}")
        print(f"Official Rating: {data['rating']['average']}")
        print(f"Summary: {data['summary']}\n")

        show = {
            'title': data['name'],
            'genres': data.get('genres', []),
            'rating': data['rating'].get('average') if data.get('rating') else None,
            'watched': False,
            'personal_rating': None
        }
        return show
    else:
        print("Show not found or API request failed.\n")
