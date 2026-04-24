#!/usr/bin/env python3
"""Explora a estrutura da Pave API para descobrir como listar jobs."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import requests
from config import JT_GRANT_KEY, JT_API_URL, JT_ORG_ID


def try_query(label: str, query: dict):
    print(f"\n{'=' * 70}")
    print(f"TEST: {label}")
    print("=" * 70)
    payload = {"query": {"$": {"grantKey": JT_GRANT_KEY}, **query}}
    print(f"Payload: {json.dumps(payload, indent=2)[:500]}")
    resp = requests.post(JT_API_URL, json=payload)
    print(f"Status: {resp.status_code}")
    try:
        body = resp.json()
        print(f"Body (first 2000 chars): {json.dumps(body, indent=2)[:2000]}")
    except Exception:
        print(f"Body (text): {resp.text[:2000]}")


# Teste 1: buscar organization básica
try_query("organization básica", {
    "organization": {
        "$": {"id": JT_ORG_ID},
        "id": {},
        "name": {},
    }
})

# Teste 2: organization + jobs sem paginação complexa
try_query("organization.jobs simples", {
    "organization": {
        "$": {"id": JT_ORG_ID},
        "jobs": {
            "nodes": {
                "id": {},
                "name": {},
            }
        }
    }
})

# Teste 3: organization + jobs com size
try_query("organization.jobs com size", {
    "organization": {
        "$": {"id": JT_ORG_ID},
        "jobs": {
            "$": {"size": 10},
            "nodes": {
                "id": {},
                "name": {},
            }
        }
    }
})

# Teste 4: adicionar createdAt
try_query("jobs com createdAt", {
    "organization": {
        "$": {"id": JT_ORG_ID},
        "jobs": {
            "$": {"size": 3},
            "nodes": {
                "id": {},
                "name": {},
                "createdAt": {},
            }
        }
    }
})

# Teste 5: adicionar location
try_query("jobs com location", {
    "organization": {
        "$": {"id": JT_ORG_ID},
        "jobs": {
            "$": {"size": 3},
            "nodes": {
                "id": {},
                "name": {},
                "location": {"id": {}, "name": {}},
            }
        }
    }
})

# Teste 6: adicionar account
try_query("jobs com account", {
    "organization": {
        "$": {"id": JT_ORG_ID},
        "jobs": {
            "$": {"size": 3},
            "nodes": {
                "id": {},
                "name": {},
                "account": {"id": {}, "name": {}},
            }
        }
    }
})

# Teste 7: size 500
try_query("jobs size 500", {
    "organization": {
        "$": {"id": JT_ORG_ID},
        "jobs": {
            "$": {"size": 500},
            "nodes": {"id": {}, "name": {}}
        }
    }
})
