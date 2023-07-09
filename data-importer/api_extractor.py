import csv
import pandas as pd
import requests

def extract_data_from_api(api_endpoint):
    # Make API request and retrieve data
    response = requests.get(api_endpoint)
    # Process the response and convert to DataFrame
    data = response.json()  # Example: assuming the API returns JSON
    df = pd.DataFrame(data)
    return df

def extract_data_from_apis(api_endpoints):
    dfs = []
    for api_endpoint in api_endpoints:
        df = extract_data_from_api(api_endpoint)
        dfs.append(df)
    return dfs
