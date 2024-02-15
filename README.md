
# Gmail-Jira-Slack Integration Bot

This Python service monitors a Gmail account for incoming emails, creates Jira tickets based on the email content, and sends the ticket URL to a Slack channel.


# Features

## Implementation Details
-Connect to Gmail Account: The service uses the Gmail API to fetch incoming emails.

-Create Jira Tickets: Upon receiving a new email, the service extracts relevant information (subject, body, attachments) and creates a new bug ticket in Jira using the Jira REST API.

-Send Ticket URL to Slack: Once the Jira ticket is created, the service sends the ticket URL to the Slack channel "support" using a webhook URL.

-Configurability: The service is configurable through environment variables, allowing customization of Gmail credentials, Jira instance details, and Slack webhook URL.

# Bonus Features
-Documentation: Detailed documentation is provided within the codebase to explain its functionality and usage.

-Security Features: The service implements secure handling of sensitive information such as passwords and API tokens.

-Logging: The codebase logging setup  to ensure code quality, reliability, and maintainability.


# Installation

1. Clone this repository

```bash
  https://github.com/SaiDheerajPeketi/Gmail_Jira_Slack_Integration
```

2. Install the required dependencies using pip
```bash
  pip install -r requirements.txt
```

    
# Usage

- Modify Values of Environment Variables with valid Domain Name of Jira, Jira API Token, Jira Username, Slack Webhook.

- Configure the sleep time if no emails were found.

```bash
  main.py
```

# Note

Ensure that your Gmail account allows access to "Less secure apps" or use app-specific passwords if two-factor authentication is enabled.
Make sure to grant necessary permissions and access to the Gmail, Jira, and Slack APIs when configuring the service.
# Contributing

Contributions to this project are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

