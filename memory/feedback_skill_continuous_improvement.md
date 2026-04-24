---
name: Skill de melhoria contínua via git
description: A talent-construction-quote skill deve aprender com cada orçamento, commitar os aprendizados e sincronizar entre máquinas via GitHub
type: feedback
---

A skill `talent-construction-quote` foi projetada para melhorar continuamente a cada uso.

**Why:** O usuário e outra pessoa usam a skill em máquinas diferentes com a mesma conta JobTread. Cada orçamento pode trazer novos rates confirmados, escopos novos ou correções. Esse conhecimento deve ser compartilhado automaticamente entre as máquinas.

**How to apply:**
- **FASE 0 (início de toda sessão):** sempre executar `git pull --rebase origin main` no PROJECT_DIR antes de iniciar qualquer intake
- **FASE 4 (fim de toda sessão):** após cada quote criado, perguntar ao usuário se há observações, atualizar os arquivos relevantes (`references/pricing.md`, `memory/project_estimator_patterns.md`, `memory/project_jobtread_api.md`), e commitar + push com mensagem `"Learn: [escopo] — [cliente] ([data])"`
- **Nunca pular a FASE 4** mesmo que o usuário não tenha correções — ao menos confirmar que não há aprendizados novos
- O `.skill` packaged em `talent-construction-quote.skill` precisa ser regerado manualmente se o SKILL.md mudar estruturalmente
