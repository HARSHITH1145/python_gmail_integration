# from jira import JIRA


"""
# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

JIRA_API_TOKEN = "ATATT3xFfGF0omh9_MWSk-zM9ba6oXnxoymKAQ4BY70pV41mPaPVkxIKlo1BMqAfwPiHdv2SoJI_yuLfnGuKCVHqumHHDMDxx5NwP_Qm3u9ZyEdKFPjoyyJbDrWGudt1UBvT2GIhZvX_OI8LAU3bOf_fI8R1hpFS_UuwRRBVDJS_INi0sGOcmvw=5EC26CA1"

url = "https://pytestbot.atlassian.net//rest/api/3/project"

auth = HTTPBasicAuth("pytestbot333@gmail.com", JIRA_API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

output = json.loads(response.text)

name = output[0]['name']

print(name)

"""

# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://pytestbot.atlassian.net/rest/api/3/issue"

JIRA_API_TOKEN = "ATATT3xFfGF0omh9_MWSk-zM9ba6oXnxoymKAQ4BY70pV41mPaPVkxIKlo1BMqAfwPiHdv2SoJI_yuLfnGuKCVHqumHHDMDxx5NwP_Qm3u9ZyEdKFPjoyyJbDrWGudt1UBvT2GIhZvX_OI8LAU3bOf_fI8R1hpFS_UuwRRBVDJS_INi0sGOcmvw=5EC26CA1"

auth = HTTPBasicAuth("pytestbot333@gmail.com", JIRA_API_TOKEN)

# headers = {
#   "Accept": "application/json",
#   "Content-Type": "application/json"
# }
#
# payload = json.dumps( {
#   "fields": {
#     "description": {
#       "content": [
#         {
#           "content": [
#             {
#               "text": "My first JIRA Ticket",
#               "type": "text"
#             }
#           ],
#           "type": "paragraph"
#         }
#       ],
#       "type": "doc",
#       "version": 1
#     },
#     "issuetype": {
#       # Bug Type Issue
#       "id": "10005"
#     },
#     "project": {
#       "key": "SCRUM"
#     },
#     "summary": "First JIRA Ticket",
#     "versions": [
#       {
#         "id": "10000"
#       }
#     ]
#   },
#   "update": {}
# } )
#
# response = requests.request(
#    "POST",
#    url,
#    data=payload,
#    headers=headers,
#    auth=auth
# )
#
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

"""
WORKING CODE BUT CANT SEE TICKETS IN JIRA
"""
# headers = {
#   "Accept": "application/json",
#   "Content-Type": "application/json"
# }
#
# payload = json.dumps({
#   "fields": {
#     "description": {
#       "content": [
#         {
#           "content": [
#             {
#               "text": "My first jira ticket",
#               "type": "text"
#             }
#           ],
#           "type": "paragraph"
#         }
#       ],
#       "type": "doc",
#       "version": 1
#     },
#     "project": {
#       "key": "TEST"
#     },
#     "issuetype": {
#       "id": "10005"
#     },
#     "summary": "First JIRA Ticket",
#   },
#   "update": {}
# })
#
# response = requests.request(
#    "POST",
#    url,
#    data=payload,
#    headers=headers,
#    auth=auth
# )
#
# print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))

PROJECT_KEY = "BTG"
ISSUE_ID = ""