---
name: Padrões do estimator — Talent Construction
description: Regras de orçamento, unit rates reais, estrutura de quotes e padrões de criação de cost items para o estimator da Talent
type: project
---

Padrões descobertos a partir dos 29 jobs reais do JobTread + 3 conversas do ChatGPT Sonar Labs.

**Why:** Calibrar o estimator para reproduzir exatamente o padrão real da Talent.
**How to apply:** Usar ao gerar quotes — estrutura LS, descrições longas, margens corretas.

---

## Estrutura de quote (padrão real Talent)

- **Lump Sum (LS)** como padrão — 1 line item por escopo principal, não detalhado por fase
- **Descrições longas** passo-a-passo incluídas no campo `description` de cada costItem
- **Placeholders** no início e fim de todo job:
  - "Inspection and evaluation labor" (qty=null, price=null, Labor/Foundation)
  - "Final inspection" (qty=null, price=null, Labor/Foundation)
- **Margem:** Labor 40% / Materials 40.91% / Subcontractor 50% / Equipment 20%
- `unitCost = unitPrice × (1 - margem)`

## Unit rates reais (Sarasota/Bradenton, FL — 2026)

| Escopo | Tipo | Rate | CostCode |
|---|---|---|---|
| Cement block wall (inclui stucco+paint) | Labor LS | ~$4,990–$9,980 | Masonry |
| Interior painting full (residência) | Labor LS | ~$15,800 | Painting |
| Drywall repair (por ocorrência) | Labor LS | ~$3,890 | Drywall |
| Crack repair + touch-up | Labor LS | ~$1,100 | Uncategorized |
| Shower remodeling (completo) | Labor LS | ~$8,965 | Miscellaneous |
| Permit fees | Labor LS | ~$1,250 | Miscellaneous |
| Deck construction (material+labor) | Labor LS | ~$7,890 | Decking |
| Engineering plans | Subcontractor LS | ~$950 | Uncategorized |
| Tile material | Labor SF | $15/SF | Tiling |
| Tile installation | Labor SF | $12.50/SF | Tiling |
| Impact window (material, por tamanho) | Materials EA | $724–$2,555 | Doors & Windows |
| Window installation | Labor EA | $450/EA | Foundation |

## Referência Sonar GPT (unit rates mercado Sarasota)

| Item | Rate |
|---|---|
| Layout/excavation/footing | $38/LF |
| Concrete footer w/ rebar | $78/LF |
| CMU wall 8" | $27/SF |
| Stucco new finish | $7.75/SF |
| Skim coat smooth | $7.25/SF |
| Surface prep/patch | $2.40/SF |
| Prime + paint new | $3.50/SF |
| Prime + repaint existing | $3.00/SF |
| Retaining wall paint | $7.50/SF |
| LED rough-in | $210/EA |
| LED fixture standard | $85/EA |
| Mobilization small job | $650 LS |

## Apresentação visual ao cliente (formato ChatGPT)

Mesmo usando LS no JobTread, a proposta ao cliente deve mostrar:
1. Scope description por seção
2. Line items com valor (LS)
3. Subtotais por seção
4. Total geral
5. Assumptions
6. Exclusions
7. Payment terms (50% down / 50% end of job — padrão Talent)
8. Schedule estimado
9. Validity: 15 days

## Perguntas obrigatórias para gerar quote

### Cliente
- Nome, endereço da obra, telefone, email
- Type: Commercial / Residential / Other
- Needs: (lista)

### Escopo
- Descrição livre do trabalho
- Dimensões quando relevante (LF, SF, EA)
- Localização (Sarasota, Bradenton, Venice, etc.)
