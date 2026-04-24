#!/usr/bin/env python3
"""Descobre quais fields existem no nó Job."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import requests
from config import JT_GRANT_KEY, JT_API_URL, JT_ORG_ID


def try_field(field: str):
    payload = {
        "query": {
            "$": {"grantKey": JT_GRANT_KEY},
            "organization": {
                "$": {"id": JT_ORG_ID},
                "jobs": {
                    "$": {"size": 1},
                    "nodes": {
                        "id": {}, "name": {},
                        field: {} if field not in ("location", "customer", "client") else {"id": {}, "name": {}},
                    }
                }
            }
        }
    }
    resp = requests.post(JT_API_URL, json=payload)
    ok = resp.status_code == 200
    msg = resp.text[:120] if not ok else "OK"
    print(f"{field:25s} → {resp.status_code} {msg}")


# Testar vários campos possíveis
for f in ["account", "customer", "client", "contact", "owner", "address",
          "location", "phone", "email", "status", "description", "tags",
          "projectManager", "salesperson", "createdAt", "updatedAt",
          "closedAt", "startDate", "endDate", "number", "jobNumber",
          "jobType", "type", "budget", "total"]:
    try_field(f)
