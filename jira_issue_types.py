# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json


url = "https://harshithp124.atlassian.net//rest/api/3/issue/createmeta"

API_TOKEN = "ATATT3xFfGF0kAsQjiHZYDp-AfxSRELWQ0XXJYnIybs3VXLC8mOedxrytZSvuSJorqfRs5nj3Mo3_xnskH0pxriTGUfTRljX--DZUWZjg9_bdqOM60diWBjXUm9jzoUKw-b3Q4AGkGblsfTwvQyX9d0uc7QXWoXE8f78snbrwqis2c2tQQO8hvY=647E9EC5"


auth = HTTPBasicAuth("harshithp124@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))