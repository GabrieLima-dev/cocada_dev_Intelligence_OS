# Interface de comandos

Os comandos são uma convenção conversacional, não dependem de parser. Texto livre equivalente deve rotear da mesma forma.

| Comando | Exemplo | Rota principal |
|---|---|---|
| `/idea` | `/idea java` | Strategist → Idea Lab |
| `/news` | `/news Java 26` | News to Content |
| `/script` | `/script CNT-2026-0001` | Hook → Script → Review |
| `/hooks` | `/hooks Kafka` | Hook Lab |
| `/analyze` | `/analyze CNT-2026-0001` | Metrics to Learning |
| `/research` | `/research virtual threads` | Radar/Technical Reviewer |
| `/calendar` | `/calendar 7 dias` | Content Strategist |
| `/story` | `/story bastidor da aula` | Story or Reel |
| `/review` | `/review roteiro.md` | Brand/Technical/Creative conforme risco |
| `/metrics` | `/metrics CNT-2026-0001` | Analytics Lab |
| `/experiment` | `/experiment hooks pessoais` | Experiment Lab |
| `/series` | `/series Backend Visual` | Strategist |
| `/strategy` | `/strategy review` | Strategist + Curator |

Sufixos opcionais: `--fast`, `--standard`, `--deep`. Na ausência, o Orchestrator escolhe e pode declarar o modo quando isso afetar escopo.

## Formato de resposta

Use somente seções necessárias, normalmente:

```text
RECOMENDAÇÃO
POR QUÊ
HOOK / ARTEFATO
EXECUÇÃO
PRÓXIMA AÇÃO
```

Não exponha “Agente A disse”. Divergência relevante vira trade-off sintetizado.
