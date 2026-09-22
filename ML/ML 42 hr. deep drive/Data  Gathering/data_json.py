import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    df = pd.DataFrame(data)

    print(df)
else:
    print("API request failed")