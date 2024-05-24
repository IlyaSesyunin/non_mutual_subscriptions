import json

# Load data from the JSON files
with open('data/following.json', 'r') as f:
    following_data = json.load(f)['relationships_following']

with open('data/followers_1.json', 'r') as f:
    followers_data = json.load(f)


# Function to extract hrefs from the provided data structure
def extract_hrefs(data):
    hrefs = set()
    for item in data:
        for string_list_item in item['string_list_data']:
            hrefs.add(string_list_item['href'])
    return hrefs


# Extract the href values
following_links = extract_hrefs(following_data)
followers_links = extract_hrefs(followers_data)

# Find links that are in following but not in followers
unique_following_links = following_links - followers_links

# Print the results
print(f'Your followers: {len(followers_links)}')
print(f'Your subscriptions: {len(following_links)}')
print(f'You are not mutually subscribed: {len(unique_following_links)}')
for link in unique_following_links:
    print(link)
