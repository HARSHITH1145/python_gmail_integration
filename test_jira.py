# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://pytestbot.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0omh9_MWSk-zM9ba6oXnxoymKAQ4BY70pV41mPaPVkxIKlo1BMqAfwPiHdv2SoJI_yuLfnGuKCVHqumHHDMDxx5NwP_Qm3u9ZyEdKFPjoyyJbDrWGudt1UBvT2GIhZvX_OI8LAU3bOf_fI8R1hpFS_UuwRRBVDJS_INi0sGOcmvw=5EC26CA1"

auth = HTTPBasicAuth("pytestbot333@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first Bug Report",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "BTG"
    },
    "issuetype": {
      "id": "10013"
    },
    "summary": "First JIRA Bug Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))