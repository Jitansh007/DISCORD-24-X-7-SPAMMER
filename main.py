from webserver import keep_alive
import requests

channelID = 934476859255689236
headers = {
    "authorization":
    "OTM0NDc2ODU5MjU1Njg5MjM2.GosZQe._ot-qM9mGYJ7HW3Bx6lyWqxHTHVJYQ_QTB4nOw"
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
