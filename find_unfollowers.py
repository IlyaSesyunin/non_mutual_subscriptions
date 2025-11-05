import json

# Load data from the JSON files
with open('data/following.json', 'r') as f:
    following_data = json.load(f)['relationships_following']

with open('data/followers_1.json', 'r') as f:
    followers_data = json.load(f)


# Function to extract usernames from the provided data structure
def extract_usernames_following(data):
    usernames = set()
    for item in data:
        usernames.add(item['title'])
    return usernames

def extract_usernames_followers(data):
    usernames = set()
    for item in data:
        for string_list_item in item['string_list_data']:
            usernames.add(string_list_item['value'])
    return usernames


# Extract the usernames
following_usernames = extract_usernames_following(following_data)
followers_usernames = extract_usernames_followers(followers_data)

# Find usernames that are in following but not in followers
unique_following_usernames = following_usernames - followers_usernames

# Print the results
print(f'Your followers: {len(followers_usernames)}')
print(f'Your subscriptions: {len(following_usernames)}')
print(f'You are not mutually subscribed: {len(unique_following_usernames)}')
for username in unique_following_usernames:
    print(f'https://www.instagram.com/{username}')
