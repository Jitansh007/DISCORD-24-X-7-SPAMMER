from webserver import keep_alive
import requests

channelID = 930506194831933520
headers = {
    "authorization":
    "OTE0NDg5MTIwMDQ5NDcxNTYw.YkxBvA.nkhjBGlutYl61TsNYdrXG4M_52s
"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
