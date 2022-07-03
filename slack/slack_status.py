from slack_sdk import WebClient
from dotenv import load_dotenv


client = WebClient(token=token)
resp = client.users_profile_get(user='UGNGQ498T')
print(resp.data['profile']['status_text'])