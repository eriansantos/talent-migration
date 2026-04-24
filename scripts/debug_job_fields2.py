#!/usr/bin/env python3
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import requests
from config import JT_GRANT_KEY, JT_API_URL, JT_ORG_ID


def q(q_body):
    payload = {"query": {"$": {"grantKey": JT_GRANT_KEY}, **q_body}}
    resp = requests.post(JT_API_URL, json=payload)
    return resp.status_code, resp.text[:300]


# test closedOn only
print("closedOn:", q({
    "organization": {"$": {"id": JT_ORG_ID},
        "jobs": {"$": {"size": 1}, "nodes": {"id": {}, "closedOn": {}}}}
}))

# test closedOn WITH page
print("closedOn+page:", q({
    "organization": {"$": {"id": JT_ORG_ID},
        "jobs": {"$": {"size": 1, "page": 1}, "nodes": {"id": {}, "closedOn": {}}}}
}))

# test nextPage
print("nextPage:", q({
    "organization": {"$": {"id": JT_ORG_ID},
        "jobs": {"$": {"size": 1}, "nextPage": {}, "nodes": {"id": {}}}}
}))

# test full query from list_all_jobs minus nextPage
print("full-no-nextpage:", q({
    "organization": {"$": {"id": JT_ORG_ID},
        "jobs": {"$": {"size": 1},
            "nodes": {"id":{}, "name":{}, "number":{}, "createdAt":{}, "closedOn":{}, "status":{}, "description":{}, "location": {"id":{},"name":{}}}}}
}))
