import pandas as pd

data = {
    "channel_name": ["Tech A", "Tech B", "Tech C"],
    "subscribers": [100000, 250000, 150000],
    "total_views": [5000000, 10000000, 7000000]
}

df = pd.DataFrame(data)

print(df)
