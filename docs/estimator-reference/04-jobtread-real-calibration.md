# Referência 4 — Calibração real da Talent Construction no JobTread

**Fonte:** export completo da API JobTread em `data/jobtread_jobs_full.json`
**Data:** 2026-04-24
**Jobs analisados:** 29 (números 2001–2030)
**Cost items totais:** 683

---

## 1. Cost Types — distribuição e margem REAL observada

| Cost Type | # items | Preço médio | Mediano | Margem |
|---|---|---|---|---|
| **Labor** | 558 | $3,735 | $1,462 | **40%** ✓ |
| **Materials** | 85 | $766 | $165 | **40.91%** ✓ |
| **Equipment** | 34 | $815 | $632 | **20%** ✓ |
| **Subcontractor** | 6 | $950 | $950 | **50%** ✓ |

Margens batem exatamente com `config.py` — sistema calibrado.

---

## 2. Cost Codes mais usados

| Cost Code | # items | Notas |
|---|---|---|
| Uncategorized | 386 | Muitos items sem código — uso padrão quando não há match óbvio |
| Doors & Windows | 51 | Impact windows, entry doors |
| Miscellaneous | 36 | Shower remodeling, general repairs, permit fees |
| Painting | 31 | Interior/exterior |
| Drywall | 26 | Repair + full install |
| Flooring | 24 | LVP, tile |
| Foundation | 24 | Usado como placeholder em "Inspection" genérico |
| Patio Screen | 16 | — |
| Electrical | 16 | — |
| Demolition | 12 | — |
| Framing | 11 | — |
| Plumbing | 10 | — |

---

## 3. Unit Rates REAIS usados pela Talent (ampliação do guia Sonar Labs)

### Masonry
| Item | Rate Talent (real) | Rate Sonar GPT | Diferença |
|---|---|---|---|
| Cement block wall (Labor, inclui material+labor) | **$4,990 LS** (11×7 = 77 SF ≈ $64/SF) | $27/SF + stucco + paint = $38.25/SF | **Talent cobra ~70% mais** |

### Painting
| Item | Rate Talent (real) | Rate Sonar GPT |
|---|---|---|
| Interior painting full (residência média) | **$15,800 LS** | ~$3.00/SF |
| Drywall repair (por ocorrência significativa) | **$3,890 LS** | — |
| Crack repair + touch-up (small) | **$1,100 LS** | $675–$1,100 |

### Tiling (Job 2027, 1,170 SF)
| Item | Rate Talent |
|---|---|
| Tile material supply (tratado como Labor pelo sistema) | **$15/SF** |
| Tile installation labor | **$12.50/SF** |
| Total material + install | **$27.50/SF** |

### Windows (Impact, Miami certification)
| Item | Rate Talent |
|---|---|
| Size 72×44 | $2,555/EA (material) |
| Size 36×62 | $1,321/EA (material) |
| Size 18×62 (std) | $1,588/EA (material) |
| Size 25×37 | $724/EA (material) |
| Installation labor | **$450/EA** |

### Shower Remodeling
| Item | Rate Talent |
|---|---|
| Shower remodel (Labor LS, inclui demo + tile + plumbing) | **$8,965 LS** |
| Permit fees and inspections | **$1,250 LS** |

### Decking
| Item | Rate Talent |
|---|---|
| New deck material/draws/labor (~10x20 deck) | **$7,890 LS** |
| Engineering plans (subcontractor) | **$950 LS** |

---

## 4. Padrões estruturais observados em TODO job

### Padrão 1 — "Inspection and evaluation labor" (placeholder inicial)
Quase todo job tem:
```
qty=0, price=0, Labor / Foundation ou Uncategorized
name: "Inspection and evaluation labor"
```
**Provável propósito:** marcador de etapa inicial que o PM preenche depois.

### Padrão 2 — "Final inspection" (placeholder final)
Mesmo padrão, aparece no final de quase todo job:
```
qty=0, price=0, Labor / Foundation ou Uncategorized
name: "Final inspection"
```

### Padrão 3 — Descrições detalhadas em cada line item
As descrições tipicamente listam o que ESTÁ incluído no escopo:
```
Build a Cement Block Wall
DESC: - Prep the floor - securely fastening the base of the wall to the existing footer
      - Construct cement block wall
      - Apply stucco finish
      - Prime and paint
      ...
```

### Padrão 4 — Line items DUPLICADOS (confirmado em múltiplos jobs)
- Job 2021: 2× "Build a Cement Block Wall" ($4,990 cada) → total $9,980
- Job 2011/2026: Todos items aparecem 2x
- Job 2029: 2× "SHOWER REMODELING" ($8,965 cada)
- Job 2020: Todos windows listados 2x

**⚠️ A decidir com o usuário:** esse padrão de duplicação é intencional ou erro? Afeta como o gerador deve compor os quotes.

---

## 5. Descrições padrão extraídas (templates pra reuso)

### Interior Painting – Full Painting
> Preparation, masking, filling cracks and holes, and caulking gaps.
> Painting (primer + 2 coats Sherwin-Williams Superpaint).

### Drywall Repair (detalhado)
> - Repair the drywall on the column next to the stairs on the first floor.
> - Repair [localizar].
> - Tape, mud, sand, prime.

### Cement Block Wall (escopo completo)
> - Prep the floor - securely fastening the base of the wall to the existing footer
> - Construct cement block wall
> - Apply stucco finish
> - Prime and paint

### Shower Remodeling (full scope)
> 1) DEMOLITION PREPARATION: Remove existing plastic shower walls and floor. Remove [...]
> 2) [fases técnicas]

### Crack Repair + Touch-Up Painting
> - Mobilization and site protection
> - Inspect and prep crack areas
> - Route and clean cracks
> - Apply elastomeric crack filler / stucco patch
> - Texture to match existing finish
> - Prime repaired areas
> - Spot paint to match existing color (feathered blend)

### Install New Drywall (Walls & Ceiling)
> 1- 1/2" drywall walls
> 2- 5/8" ceiling (if required)
> 3- Hang & fasten

### New Deck Construction
> - Processing of building permits with Sarasota County
> - Structural Framing
> - [siding, decking surface, railings, finish]

### Impact Windows
> - Impact Windows
> - Certification Type: Miami
> - Frame Type: Flange
> - Glass Lamina [...]

### Tile Material (exemplo real)
> - MLB Eastern Promise Marrakesh Palazzo 8x8
> - Color: Z0419 Palazzo-Milk-Dove-Smoke

---

## 6. Comparação Talent real vs Sonar GPT (calibração)

| Aspecto | Sonar GPT | Talent real (JobTread) |
|---|---|---|
| Markup/margem | 20% (OH+P) | **40% Labor / 40.91% Materials** |
| Detalhamento | Line item por fase | LS compostos (cement wall tudo junto) |
| Uso de costCode | — | Uncategorized muito usado |
| Inspections | implícito | Line items placeholder qty=0 |
| Descrições | curtas | Longas, passo-a-passo |
| Preço parede CMU 11×7 | ~$6,900 (detalhado) | **$9,980** (2× $4,990 LS) |
| Crack repair Venice-style | $675–$1,100 | **$1,100–$2,200** (pattern duplicado) |
| Interior painting (full) | — | **$15,800 LS** típico |

---

## 7. Ajustes necessários no estimator.py

Para replicar **exatamente** o padrão Talent (não o Sonar GPT):

1. ✅ **Margem: 40% Labor / 40.91% Materials** (já em `config.py`)
2. ⚠️ **Composição em LS** em vez de linha a linha quando for serviço padrão
3. ⚠️ **Descrições longas** passo-a-passo (templates da seção 5)
4. ⚠️ **Adicionar placeholders** de Inspection no início e Final Inspection no fim
5. ⚠️ **Decidir** se duplica line items (padrão observado) ou cria únicos
6. ✅ **Cost codes** podem defaultar pra Uncategorized quando não houver match claro
7. ⚠️ **Unit rates Talent > Sonar GPT** em ~30-70% — o Sonar é teórico de mercado, a Talent pratica preços reais mais altos
