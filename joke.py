import requests

def get_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    res = requests.get(url)
    if res.status_code == 200:
        joke = res.json()
        print(f"\n{joke['setup']}")
        print(f"{joke['punchline']}")
    else:
        print("Couldn’t fetch joke.")

if __name__ == "__main__":
    print("Random Joke Generator")
    get_joke()
