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

## Cliente já existente no JobTread

Quando o usuário disser que o cliente já está no sistema, **pedir o account ID** em vez de seguir o intake completo. Buscar via API: `account(id=...)` retorna `name`, `locations.nodes`, `contacts.nodes`. Se confirmar, **pular** criação de account/location/contact e ir direto para o job.

Se o usuário não tiver o ID, fazer busca por nome com `organization.accounts` e listar matches para confirmar.

**Why:** Evita duplicar accounts e economiza várias perguntas do intake.

## Transcrição de orçamento externo (ChatGPT, planilha, PDF)

Quando o usuário trouxer quote pré-pronto de outra fonte:

1. Validar a aritmética antes de propor — orçamentos do ChatGPT frequentemente têm subtotais que não fecham com os itens detalhados (ex: ao "distribuir OH&P" os itens individuais inflacionam mas o subtotal mostrado fica desatualizado).
2. Apontar inconsistências numéricas explicitamente e perguntar qual versão usar.
3. **Oferecer duas estruturas** antes de criar:
   - **Detalhada** (item-a-item, com qty/unit/unit price reais)
   - **Resumida LS** (1 line item por escopo, descrição longa)
4. Se a soma dos subtotais não fechar com o "Recommended Proposal Price", perguntar ao usuário como tratar a diferença (linha de allowance, distribuir, ou eliminar).

**Why:** O padrão real Talent é LS resumido (memory acima), mas em transcrições o usuário às vezes quer preservar o detalhamento original. Perguntar antes evita retrabalho — já aconteceu de criar 17 itens detalhados e depois ter que apagar e refazer com 5 LS.

## Confirmação obrigatória antes de operações destrutivas

Antes de **deletar, sobrescrever ou recriar** cost items que já existem em um job, pedir confirmação explícita ao usuário. Exemplo: se o usuário pedir "cria os itens de novo resumido", perguntar se é para **substituir** (apagar os atuais) ou **adicionar alongside**.

**Why:** Cost items em produção podem ter sido editados/aprovados por terceiros. A reversão é manual e custosa.
