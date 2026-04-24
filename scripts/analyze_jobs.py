#!/usr/bin/env python3
"""Analisa os line items de todos os jobs para extrair padrões de calibração."""
import json
import re
from collections import defaultdict, Counter
from pathlib import Path
from statistics import mean, median


ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "jobtread_jobs_full.json"


def load_jobs():
    with open(DATA) as f:
        return json.load(f)


def normalize(name: str) -> str:
    """Chave de agrupamento: lowercase + primeiras palavras significativas."""
    if not name:
        return ""
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def main():
    jobs = load_jobs()
    print(f"Total jobs: {len(jobs)}")

    # ── 1. Resumo por job ────────────────────────────────────────────────────
    print("\n" + "=" * 90)
    print("RESUMO POR JOB")
    print("=" * 90)
    print(f"{'#':<4} {'Status':<12} {'Name':<25} {'Description':<40} {'#Items':<7} {'Total':>10}")
    print("-" * 90)

    for j in jobs:
        items = j.get("costItems", [])
        total = sum(
            (it.get("quantity", 0) or 0) * (it.get("unitPrice", 0) or 0)
            for it in items
        )
        desc = (j.get("description") or "")[:38]
        print(f"{j.get('number','?'):<4} {j.get('status','?'):<12} {j.get('name','?')[:23]:<25} {desc:<40} {len(items):<7} ${total:>9,.2f}")

    # ── 2. Cost Types usados ─────────────────────────────────────────────────
    print("\n" + "=" * 90)
    print("COST TYPES usados (freq + unit price stats)")
    print("=" * 90)
    by_type = defaultdict(list)
    for j in jobs:
        for it in j.get("costItems", []):
            ct = (it.get("costType") or {}).get("name", "—")
            up = it.get("unitPrice") or 0
            uc = it.get("unitCost") or 0
            by_type[ct].append((up, uc))

    for ct, vals in sorted(by_type.items(), key=lambda x: -len(x[1])):
        prices = [v[0] for v in vals if v[0]]
        costs = [v[1] for v in vals if v[1]]
        margem = None
        if prices and costs:
            ratio = [c/p for p, c in zip(prices, costs) if p and c]
            if ratio:
                margem = f"{(1 - mean(ratio))*100:.1f}%"
        print(f"  {ct:<20} n={len(vals):<4} preço médio=${mean(prices):>8.2f}  mediano=${median(prices):>8.2f}  margem≈{margem}")

    # ── 3. Cost Codes usados ─────────────────────────────────────────────────
    print("\n" + "=" * 90)
    print("COST CODES usados (freq)")
    print("=" * 90)
    by_code = Counter()
    for j in jobs:
        for it in j.get("costItems", []):
            cc = (it.get("costCode") or {}).get("name", "—")
            by_code[cc] += 1
    for cc, n in by_code.most_common():
        print(f"  {cc:<25} {n}")

    # ── 4. Padrões por palavra-chave no nome ─────────────────────────────────
    print("\n" + "=" * 90)
    print("PADRÕES DE PREÇO POR PALAVRA-CHAVE")
    print("=" * 90)
    keywords = [
        "paint", "drywall", "tile", "window", "door", "stucco", "floor",
        "electric", "plumb", "demo", "framing", "trim", "counter", "cabinet",
        "concrete", "install", "roof", "fence", "permit", "labor", "material",
        "light", "led", "texture", "pressure", "wash", "repair",
    ]

    kw_stats = defaultdict(list)
    for j in jobs:
        for it in j.get("costItems", []):
            name = (it.get("name") or "").lower()
            up = it.get("unitPrice") or 0
            qty = it.get("quantity") or 0
            desc = (it.get("description") or "")[:60]
            for kw in keywords:
                if kw in name:
                    kw_stats[kw].append((it.get("name"), qty, up, desc))
                    break  # só a primeira match

    for kw in sorted(kw_stats.keys()):
        items = kw_stats[kw]
        prices = [i[2] for i in items if i[2]]
        if not prices:
            continue
        print(f"\n  [{kw}]  n={len(items)}  preço range ${min(prices):.2f}–${max(prices):.2f}  médio ${mean(prices):.2f}")
        # amostra 3
        for name, qty, up, desc in items[:3]:
            print(f"     {qty:>6.1f} × ${up:>8.2f}  {name[:50]}")

    # ── 5. Exportar CSV para análise externa ─────────────────────────────────
    import csv
    csv_path = ROOT / "data" / "jobtread_line_items.csv"
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["job_name", "job_desc", "item_name", "description", "qty",
                    "unitPrice", "unitCost", "costType", "costCode", "isTaxable"])
        for j in jobs:
            for it in j.get("costItems", []):
                w.writerow([
                    j.get("name", ""),
                    j.get("description", ""),
                    it.get("name", ""),
                    (it.get("description") or "")[:200],
                    it.get("quantity", 0),
                    it.get("unitPrice", 0),
                    it.get("unitCost", 0),
                    (it.get("costType") or {}).get("name", ""),
                    (it.get("costCode") or {}).get("name", ""),
                    it.get("isTaxable", False),
                ])
    print(f"\n\nCSV exportado: {csv_path}")


if __name__ == "__main__":
    main()
