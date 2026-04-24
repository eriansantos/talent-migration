# Talent Construction — Reference Pricing
## Sarasota / Bradenton / Manatee County FL (2026)

Source: Empirical data from 29 real JobTread jobs + Sonar GPT market research.

---

## Lump Sum (LS) Rates — Padrão Talent

| Scope | CostType | LS Price | CostCode |
|-------|----------|----------|----------|
| Crack repair + touch-up painting | Labor | ~$1,100 | Uncategorized |
| Drywall repair (per occurrence, small-medium) | Labor | ~$3,890 | Drywall |
| Interior painting — full residence | Labor | ~$15,800 | Painting |
| Cement block wall (incl. stucco + paint) | Labor | $4,990–$9,980 | Masonry |
| Shower remodeling (complete) | Labor | ~$8,965 | Miscellaneous |
| Permit fees (standard residential) | Labor | ~$1,250 | Miscellaneous |
| Deck construction (material + labor) | Labor | ~$7,890 | Decking |
| Engineering / structural plans | Subcontractor | ~$950 | Uncategorized |
| Mobilization (small job) | Labor | $650 | Uncategorized |
| Patio screen installation (standard) | Labor | $2,500–$5,000 | Patio Screen |
| Kitchen remodel (full, mid-grade) | Labor | $18,000–$45,000 | Cabinetry |
| Bathroom remodel (full, mid-grade) | Labor | $8,965–$22,000 | Miscellaneous |

---

## Per-Unit Rates (SF / LF / EA)

### Tile
| Item | Unit | Price | CostType | CostCode |
|------|------|-------|----------|----------|
| Tile material (standard porcelain) | SF | $15.00 | Materials | Tiling |
| Tile installation | SF | $12.50 | Labor | Tiling |
| Tile demo (existing) | SF | $3.50 | Labor | Demolition |

### Painting
| Item | Unit | Price | CostType | CostCode |
|------|------|-------|----------|----------|
| Interior walls (2 coats, incl. material) | SF | $2.50–$3.50 | Labor | Painting |
| Exterior painting (prepared surface) | SF | $3.00–$5.00 | Labor | Painting |
| Ceiling painting | SF | $2.00–$3.00 | Labor | Painting |
| Cabinet painting | LF | $30–$45 | Labor | Cabinetry |

### Drywall
| Item | Unit | Price | CostType | CostCode |
|------|------|-------|----------|----------|
| New drywall install (1/2", taped, level 4) | SF | $3.50–$5.00 | Labor | Drywall |
| Texture only (knockdown/orange peel) | SF | $1.25–$2.50 | Labor | Drywall |
| Ceiling drywall replacement (full) | SF | $5.00–$7.00 | Labor | Drywall |

### Flooring
| Item | Unit | Price | CostType | CostCode |
|------|------|-------|----------|----------|
| LVP install (labor only) | SF | $3.50–$5.00 | Labor | Flooring |
| LVP material (standard) | SF | $2.50–$4.00 | Materials | Flooring |
| Hardwood install (labor only) | SF | $4.00–$8.00 | Labor | Flooring |
| Subfloor prep/leveling | SF | $2.00–$4.00 | Labor | Flooring |

### Windows
| Item | Unit | Price | CostType | CostCode |
|------|------|-------|----------|----------|
| Impact window material (standard) | EA | $724–$1,200 | Materials | Doors & Windows |
| Impact window material (large/premium) | EA | $1,500–$2,555 | Materials | Doors & Windows |
| Window installation | EA | $450 | Labor | Doors & Windows |

### Masonry (Sonar Market Rates)
| Item | Unit | Price | CostType | CostCode |
|------|------|-------|----------|----------|
| Layout/excavation/footing | LF | $38 | Labor | Foundation |
| Concrete footer w/ rebar | LF | $78 | Labor | Foundation |
| CMU wall 8" block | SF | $27 | Labor | Masonry |
| Stucco new finish | SF | $7.75 | Labor | Masonry |
| Skim coat smooth | SF | $7.25 | Labor | Masonry |
| Surface prep/patch | SF | $2.40 | Labor | Masonry |

### Electrical (sub-permit)
| Item | Unit | Price | CostType | CostCode |
|------|------|-------|----------|----------|
| LED rough-in | EA | $210 | Labor | Electrical |
| LED fixture (standard) | EA | $85 | Labor | Electrical |

---

## Pricing Philosophy

- **Lump Sum (LS)** is the standard — one cost item per scope area, NOT broken down by phase
- Descriptions should be multi-line bullet points in the cost item `description` field
- Price includes labor + material (unless noted "labor only" or "material only")
- Default CostType for most jobs: **Labor** (Talent markup 40%)
- Always use Lump Sum for jobs under ~$3K to avoid over-detailed invoices

---

## Markup Summary

| CostType | Margin | UnitCost Formula |
|----------|--------|-----------------|
| Labor | 40% | unitPrice × 0.60 |
| Materials | 40.91% | unitPrice × 0.5909 |
| Subcontractor | 50% | unitPrice × 0.50 |
| Equipment | 20% | unitPrice × 0.80 |

**Example:** Labor item at $1,100 → unitCost = $1,100 × 0.60 = $660.00
