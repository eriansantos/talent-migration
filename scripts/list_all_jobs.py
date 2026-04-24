#!/usr/bin/env python3
"""
Lista todos os jobs da Talent Construction no JobTread via Pave API.
Salva o resultado em data/jobtread_jobs_full.json para análise de calibração.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.jobtread_client import JobTreadClient
from config import JT_ORG_ID


def list_all_jobs(client: JobTreadClient) -> list:
    """Lista todos os jobs da organização via paginação por cursor."""
    all_jobs = []
    cursor = None
    while True:
        args = {"size": 100}
        if cursor:
            args["page"] = cursor
        data = client.pave({
            "organization": {
                "$": {"id": JT_ORG_ID},
                "jobs": {
                    "$": args,
                    "nodes": {
                        "id": {},
                        "name": {},
                        "number": {},
                        "createdAt": {},
                        "closedOn": {},
                        "status": {},
                        "description": {},
                        "location": {
                            "id": {},
                            "name": {},
                        },
                    },
                    "nextPage": {},
                },
            }
        })
        block = data.get("organization", {}).get("jobs", {})
        nodes = block.get("nodes", [])
        all_jobs.extend(nodes)
        cursor = block.get("nextPage")
        if not cursor:
            break
    return all_jobs


def fetch_full_job(client: JobTreadClient, job_id: str) -> dict:
    """Busca um job completo com todos os cost items."""
    return client.get_job(job_id)


def main():
    client = JobTreadClient()
    print(f"Listando jobs da org {JT_ORG_ID}...")

    jobs = list_all_jobs(client)
    print(f"Total: {len(jobs)} jobs")

    # Enriquecer cada job com seus cost items
    print("\nBuscando cost items de cada job...")
    enriched = []
    for i, job in enumerate(jobs, 1):
        print(f"  [{i}/{len(jobs)}] {job.get('name', '?')[:60]}")
        try:
            full = fetch_full_job(client, job["id"])
            if full:
                cost_items = full.get("costItems", {}).get("nodes", [])
                job["costItems"] = cost_items
            enriched.append(job)
        except Exception as e:
            print(f"    ERRO: {e}")
            job["costItemsError"] = str(e)
            enriched.append(job)

    # Salvar
    out_path = Path(__file__).resolve().parent.parent / "data" / "jobtread_jobs_full.json"
    out_path.parent.mkdir(exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(enriched, f, indent=2, default=str)

    print(f"\nSalvo em {out_path}")

    # Sumário
    total_items = sum(len(j.get("costItems", [])) for j in enriched)
    print(f"Total de cost items: {total_items}")


if __name__ == "__main__":
    main()
