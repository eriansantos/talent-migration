# Talent Construction — Migration Tool
## Jobber → JobTread

Ferramenta de migração de quotes do Jobber para o budget do JobTread via API.

---

## Estrutura

```
talent-migration/
├── migrate.py              # CLI principal
├── config.py               # Credenciais e IDs da organização
├── src/
│   ├── jobber_client.py    # Cliente GraphQL Jobber (OAuth 2.0)
│   ├── jobtread_client.py  # Cliente Pave API JobTread
│   ├── mapper.py           # Mapeamento line items → cost items
│   └── migrator.py         # Motor de migração
├── data/
│   └── jobs.json           # Lista de jobs para batch migration
└── logs/                   # Logs de execução (gerados automaticamente)
```

---

## Instalação

```bash
pip install requests
```

---

## Uso

### Migrar um job específico
```bash
python migrate.py run --quote 57649446 --job 22PVxgFHbqdU
```

### Forçar costType (ex: todos como Labor)
```bash
python migrate.py run --quote 57674580 --job 22PW2eZiNRyH --type Labor
```

### Preview sem inserir
```bash
python migrate.py run --quote 57649446 --job 22PVxgFHbqdU --dry-run
```

### Preview somente (sem JT job)
```bash
python migrate.py preview --quote 57649446
```

### Batch via arquivo JSON
```bash
python migrate.py batch --file data/jobs.json
```

### Batch inline
```bash
python migrate.py batch --pairs "57649446:22PVxgFHbqdU,57674580:22PW2eZiNRyH" --type Labor
```

---

## Mapeamento de costType

| Palavras-chave no nome/descrição | costType | Margem |
|----------------------------------|----------|--------|
| install, labor, service, repair, paint, demo... | Labor | 40% |
| window, door, material, glass, tile material... | Materials | 40.91% |
| electrici, plumb, hvac, roofing contractor... | Subcontractor | 50% |
| equip, tool, rental, dumpster... | Equipment | 20% |

Usar `--type Labor` para forçar todos os itens como Labor (padrão na Talent Construction).

---

## Mapeamento de costCode

Detecção automática por palavras-chave no nome do item:
- window/door/glass/impact → Doors & Windows
- floor/lvp/laminate → Flooring
- tile/ceramic/porcelain → Tiling
- paint/texture → Painting
- drywall/sheetrock → Drywall
- electric/circuit → Electrical
- plumb/pipe/drain → Plumbing
- cement/block/masonry → Masonry
- frame/framing/stud → Framing
- demo/remov/tear → Demolition
- ...e outros 20+ mapeamentos

---

## Credenciais

Configuradas em `config.py`:
- **Jobber**: OAuth 2.0 (Client ID + Client Secret + Refresh Token)
- **JobTread**: Grant Key

O refresh_token do Jobber tem longa duração e é renovado automaticamente.

---

## Logs

Cada migração gera um arquivo JSON em `logs/`:
- `migration_{quote_id}_{timestamp}.json` — migração individual
- `batch_{timestamp}.json` — relatório de batch

---

## Organização: Talent General Services Inc
- JobTread Org ID: 22PTSCpmQVf5
- Jobber Account: 1286676
