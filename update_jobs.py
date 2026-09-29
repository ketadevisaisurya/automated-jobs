import requests
import json

print("Fetching India tech jobs from Remotive API...")

# We use the Remotive API and add "?search=India" to the end of the URL
url = "https://remotive.com/api/remote-jobs?search=India"
response = requests.get(url)
data = response.json()

# Extract the top 15 jobs from the results
jobs_list = []

# Remotive stores their jobs inside 'jobs' instead of 'data'
for job in data['jobs'][:15]:
    jobs_list.append({
        "title": job['title'],
        "company": job['company_name'],
        "location": job['candidate_required_location'],
        "remote": True, # All Remotive jobs are remote
        "link": job['url']
    })

# Save the jobs to a file so your website can read them
with open('jobs.json', 'w') as f:
    json.dump(jobs_list, f)

print("Success! Saved India jobs to jobs.json")
