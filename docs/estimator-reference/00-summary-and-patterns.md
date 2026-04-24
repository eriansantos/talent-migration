# Síntese — Padrões do Construction Estimator GPT (Sonar Labs)

Padrões extraídos das 3 conversas de referência, prontos pra serem codificados no `estimator.py`.

---

## 1. Estrutura de uma proposta

Toda proposta gerada tem esta estrutura:

1. **Project Scope** (breve descrição)
2. **Work Items** (lista do que será feito)
3. **Quantity Summary** (tabela de quantidades)
4. **Cost Breakdown** (line items com preço)
5. **Assumptions** (premissas técnicas)
6. **Exclusions** (o que NÃO está incluído)
7. **Risks** (riscos do trabalho)
8. **Payment Terms**
9. **Schedule** (duração estimada)
10. **Proposal Validity** (15 days padrão)

---

## 2. Unidades padronizadas

| Unidade | Quando usar |
|---|---|
| **LF** (Linear Feet) | Paredes, rodapés, footers, cracks |
| **SF** (Square Feet) | Áreas — paredes (L×H), piso, teto, pintura |
| **EA** (Each) | Itens unitários — fixtures, portas, janelas |
| **LS** (Lump Sum) | Mobilization, disposal, patch allowance |

---

## 3. Unit prices de referência (Sarasota/Venice, FL)

### Masonry
| Item | Unit Rate | Unidade |
|---|---|---|
| Layout, excavation, footing prep | $38 | LF |
| Concrete footer w/ rebar | $78 | LF |
| Reinforced 8" CMU wall install | $27 | SF |

### Stucco
| Item | Unit Rate | Unidade |
|---|---|---|
| Stucco finish (new, both sides incluídos no SF) | $7.75 | SF |
| Skim coat / smooth finish | $7.25 | SF |
| Surface prep, masking, patching, bonding | $2.40 | SF |
| Detail sanding and touch-up | $0.95 | SF |

### Painting
| Item | Unit Rate | Unidade |
|---|---|---|
| Prime and paint (new stucco) | $3.50 | SF |
| Prime and repaint (existing) | $3.00 | SF |
| Retaining wall prep+paint | $7.50 | SF |

### Electrical / LED
| Item | Unit Rate | Unidade |
|---|---|---|
| LED rough-in wiring and boxes | $210 | EA |
| Standard LED wall fixture | $85 | EA |
| Switch/connectors misc (LS) | $350 | LS |

### Misc
| Item | Unit Rate | Unidade |
|---|---|---|
| Small-job mobilization/cleanup | $650 | LS |
| Masonry cut-in / patch allowance | $450 | LS |

---

## 4. Overhead & Profit

### Regra
- **Overhead: 10%**
- **Profit: 10%**
- **Markup total: ~20%** sobre o custo direto

### Fórmula de aplicação
```
PreçoDeVenda = CustoDireto × 1.20
```

### Como apresentar ao cliente
Duas formas, o GPT aceita ambas:
- **(a)** Line item "Overhead & Profit" separado no final
- **(b)** Distribuído em cada line item (multiplicar cada custo × 1.20)

Talent Construction já usa margem de 40% (Labor) / 40.91% (Materials) no JobTread — a `mapper.py` trata isso no unitCost.

---

## 5. Payment Terms (opções)

### 3 parcelas (padrão)
- 50% Deposit (assinatura)
- 40% Progress Payment (rough work pronto)
- 10% Final Payment (walkthrough)

### 2 parcelas (alternativa, mais simples)
- 50% Down
- 50% End of Job

---

## 6. Schedule típico

| Tamanho do job | Duração |
|---|---|
| Pequeno (1 room) | 1–3 dias |
| Médio (cracks + repaint parede) | 1–2 dias |
| Grande (wall construction + stucco + LED) | 5–8 dias |

---

## 7. Waste factor (drywall e materiais)

| Complexidade | Waste % |
|---|---|
| Simples | 5% |
| Média | 8–10% |
| Alta (cuts/angles) | 12–15% |

---

## 8. Fluxo de geração de quote (o que o GPT faz)

1. **Entende o escopo** do que o cliente pediu
2. **Pergunta** informações faltantes (ver seção 10)
3. **Calcula quantidades** a partir das dimensões
4. **Aplica unit prices regionais** (Sarasota/Venice)
5. **Soma subtotais por escopo**
6. **Aplica markup O&P de 20%**
7. **Adiciona assumptions e exclusions**
8. **Formata como proposal** com header da empresa

---

## 9. Padrão de "2 opções" (mínima vs completa)

Quando fizer sentido, oferecer:
- **Option 1:** solução mínima/econômica (ex: touch-up só)
- **Option 2:** solução completa (ex: repaint inteiro)

Com recomendação profissional no final explicando o trade-off.

---

## 10. Perguntas que o estimator SEMPRE faz antes de firmar pricing

### Cliente e site
- Residential ou HOA/commercial?
- Localização exata (afeta labor rate)
- Access constraints (landscaping, tight areas, lifts needed?)
- HOA approval necessário?

### Condição existente
- Wall condition: bulging, hollow spots, water damage?
- Existing paint color code disponível?
- Estrutura existente é sound?
- Hidden conditions suspeitas?

### Escopo técnico
- Altura das paredes (>10ft aumenta custo)
- Level of finish (Level 4, 5)
- Stud spacing/type (drywall)
- Special materials (elastomeric, premium fixtures)?

---

## 11. Exclusions padrão (template para qualquer job)

- Permit fees, engineering, surveys, HOA submittals
- Structural redesign ou upgraded footing por engineer/city
- Major demolition de existing assemblies
- Electrical panel upgrade, trenching longo
- Waterproofing atrás de paredes existentes
- Specialty paints / elastomeric systems / premium fixtures
- Landscaping / irrigation / hardscape restoration
- HOA approvals ou architectural review fees

## 12. Assumptions padrão

- Site has reasonable access
- Existing structures structurally sound
- Electrical source accessible (se aplicável)
- No concealed conditions or hazardous materials
- No unusual demolition or protection required

---

## 13. Proposta de arquitetura do `estimator.py`

```
User entrada livre (ex: "build 11x7 CMU wall + stucco + LED")
       ↓
[scope_parser] extrai entidades: qty, dimensions, materials, location
       ↓
[clarification_engine] pergunta o que faltou (checklist seção 10)
       ↓
[pricing_engine] aplica unit prices (tabela seção 3)
       ↓
[markup_engine] multiplica × 1.20 (O&P)
       ↓
[proposal_builder] formata: scope, line items, assumptions, exclusions
       ↓
[mapper.py] converte line items → JobTread costItem format
       ↓
[jobtread_client.py] cria no JobTread: createAccount → createJob → createCostItem
       ↓
Retorna link https://app.jobtread.com/jobs/XXX/budget
```

---

## 14. Observações importantes

- Os unit prices extraídos são do **mercado Sarasota/Venice em 2025–2026**
- A Talent Construction já tem margem configurada no JobTread (40% Labor / 40.91% Materials) — o markup O&P de 20% do GPT é da apresentação comercial, já a margem da Talent é interna (unitCost = unitPrice × 0.60)
- **Decidir com o usuário:** vamos usar o markup do estimator (20%) ou a margem da Talent (40%)? Ou ambos — markup no preço apresentado e margem como referência de custo interno?
