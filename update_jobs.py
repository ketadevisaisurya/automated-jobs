import requests
import json

print("Fetching jobs from public API...")
# We use a free API for this test. You can change this later!
url = "https://www.arbeitnow.com/api/job-board-api"
response = requests.get(url)
data = response.json()

# Extract the top 15 jobs
jobs_list = []
for job in data['data'][:15]:
    jobs_list.append({
        "title": job['title'],
        "company": job['company_name'],
        "location": job['location'],
        "remote": job['remote'],
        "link": job['url']
    })

# Save the jobs to a file so the website can read them
with open('jobs.json', 'w') as f:
    json.dump(jobs_list, f)

print("Success! Saved jobs to jobs.json")
