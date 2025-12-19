import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from slack_sdk.errors import SlackApiError
from slack_sdk.models.blocks import SectionBlock, ActionsBlock, ButtonElement
import json
from utils import parse_channel_messages

load_dotenv()

# This sample slack application uses SocketMode
# For the companion getting started setup guide, 
# see: https://slack.dev/bolt-python/tutorial/getting-started 

# GLOBAL VARS
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))
USER_ID = os.getenv("USER_ID")
USERNAME = os.getenv("USERNAME")
deadline = None
messages = parse_channel_messages("messages.txt")

# Test slash command
@app.command("/testcommand")
def uh(ack, respond, command):
    ack()
    respond("✅ ur test command worked!")



# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
