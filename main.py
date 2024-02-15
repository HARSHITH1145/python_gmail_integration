import signal
import sys
from simplegmail import Gmail
from simplegmail.query import construct_query
import requests
from requests.auth import HTTPBasicAuth
import json
import time
import os
import logging
import traceback
from config import *

# Global constant to indicate if the current iteration has been interrupted
isInterrupted = False

# Set up logging
logging.basicConfig(
    level=logging.DEBUG,
    filename="app.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# Signal Handler to handle signals like SIGINT, SIGTERM
def signal_handler(sig, frame):
    global isInterrupted
    logging.critical("Caught signal of an Interrupt")
    isInterrupted = True


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)


# Method to fetch all available issue types to configure issue type for a particular project in Jira
def get_jira_issue_types():
    headers = {"Accept": "application/json"}

    response = requests.request("GET", url, headers=headers, auth=auth)

    print(
        json.dumps(
            json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")
        )
    )


# Your Generated Domain Nam

url = f"https://{domain_name}/rest/api/3/issue"

auth = HTTPBasicAuth(JIRA_USERNAME, JIRA_API_TOKEN)

SLEEP_INTERVAL = 10

ISSUE_ID_TYPE = "10011"

PROJECT_KEY = "AUT"

headers = {"Accept": "application/json", "Content-Type": "application/json"}

gmail = Gmail()

# Query Parameters to be tweaked for further customization
query_params = {"unread": True}

# Infinite loop interrupted on SIGINT or SIGTERM handled to finish the current iteration
while True:

    # Exit if Interrupted
    if isInterrupted:
        logging.exception("Exitting due to Interrupt")
        sys.exit(1)

    # Check for new message
    messages = gmail.get_messages(query=construct_query(query_params))
    # messages = gmail.get_unread_inbox()
    print(messages)
    # Wait if no messages
    if len(messages) == 0:
        time.sleep(SLEEP_INTERVAL)
        logging.info("No messages")
        continue

    # Iterate through all messages and perform the required functionality
    for message in messages:
        logging.info("Current Mail: " + str(message))

        # Mark it as read to avoid further processing
        message.mark_as_read()

        # Current Details
        curr_subject = message.subject
        curr_body = message.plain
        curr_attachments = message.attachments

        payload = json.dumps(
            {
                "fields": {
                    "description": {
                        "content": [
                            {
                                "content": [{"text": curr_body, "type": "text"}],
                                "type": "paragraph",
                            }
                        ],
                        "type": "doc",
                        "version": 1,
                    },
                    "project": {"key": PROJECT_KEY},
                    "issuetype": {"id": ISSUE_ID_TYPE},
                    "summary": curr_subject,
                },
                "update": {},
            }
        )
        try:
            response = requests.request(
                "POST", url, data=payload, headers=headers, auth=auth
            )

            # Issue Created
            logging.info("Issue Creation: " + response.text)
        except Exception as e:
            logging.error(f"An error occurred in Creating Issue: {e}")
            traceback.print_exc()
        print(response.text)
        # Parse the returned JSON to extract key information for further processing
        curr_issue_creation_response = json.loads(response.text)
        curr_issue_id = curr_issue_creation_response["id"]
        curr_issue_key = curr_issue_creation_response["key"]
        curr_issue_self_url = curr_issue_creation_response["self"]
        curr_issue_url = "https://" + domain_name + "/browse/" + curr_issue_key
        logging.critical("Current Issue Key: " + curr_issue_key)
        logging.critical("Current Issue Self URL: " + curr_issue_self_url)
        logging.critical("Current Issue URL: " + curr_issue_url)

        # Process Attachments in the current email
        attachment_files = []
        attachment_file_names = []

        for attachment in curr_attachments:
            attachment.save()
            attachment_files.append(
                ("file", (attachment.filename, attachment.data, attachment.filetype))
            )
            attachment_file_names.append(attachment.filename)

        logging.info("Attachment files: " + str(attachment_file_names))

        # Modify the issue to include attachments
        if len(attachment_files) > 0:

            attachments_url = (
                f"https://{domain_name}/rest/api/3/issue/{curr_issue_id}/attachments"
            )

            attachments_headers = {
                "Accept": "application/json",
                "X-Atlassian-Token": "no-check",
            }

            try:
                response = requests.request(
                    "POST",
                    attachments_url,
                    headers=attachments_headers,
                    files=attachment_files,
                    auth=auth,
                )

                logging.info(response.text)
            except Exception as e:
                logging.error(f"An error occurred in Addition of Attachments: {e}")
                traceback.print_exc()

            for file in attachment_file_names:
                os.remove(file)

        else:
            logging.info("No Attachments in current email")

        # Generate a message of issue's url and post it on Slack Channel
        slack_payload = '{"text": "%s"}' % curr_issue_url
        try:
            response = requests.post(SLACK_WEBHOOK, data=slack_payload)
            logging.info("Slack Addition: " + response.text)
        except Exception as e:
            logging.error(f"An error occurred in Posting Link to Slack Channel: {e}")
            traceback.print_exc()
