import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
my_key = os.getenv("RAPIDAPI_KEY")


def fetch_rapid_jobs(query="Software Developer", location="India"):
    url = "https://jsearch.p.rapidapi.com/search" # using JSearch API

    querystring = {
        "query": f"{query} in {location}",
        "num_pages": "3",
        "date_posted": "week"
    }

    headers = {
        "X-RapidAPI-Key": my_key,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status() # Check for errors
        data = response.json()
        
        # Extracting the useful bits
        jobs = data.get('data', [])
        job_list = []
        for j in jobs:
            job_list.append({
                "Role": j.get("job_title"),
                "Company": j.get("employer_name"),
                "Location": j.get("job_city"),
                "Link": j.get("job_apply_link")
            })
        return pd.DataFrame(job_list)
    
    except Exception as e:
        print(f"Failed to fetch: {e}")
        return None

# Quick test
if __name__ == "__main__":
    df = fetch_rapid_jobs(query="Python Developer")
    print(df.head())