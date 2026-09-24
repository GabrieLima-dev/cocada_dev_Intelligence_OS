# Contratos para integrações futuras

A V1 não finge conexão com plataformas. Adaptadores futuros devem apenas importar/exportar contratos do núcleo.

| Integração | Entrada/saída esperada | Regra |
|---|---|---|
| Instagram/TikTok/YouTube | `metrics-event` + external IDs | snapshots append-only; scopes mínimos |
| Google Sheets/Notion | views de content/strategy | não virar fonte concorrente sem owner |
| PostgreSQL | schemas e IDs existentes | migração preserva IDs/proveniência |
| n8n/Make | triggers de arquivo/evento | não aprovar publicação/evolução |
| Social APIs | pacote de distribuição | publicação exige autorização explícita |

Qualquer conector declara autenticação fora do repositório, idempotência, rate limits, retries, logs, privacidade e rollback. O domínio não importa SDK de fornecedor.
