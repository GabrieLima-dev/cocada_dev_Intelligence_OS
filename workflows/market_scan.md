---
id: WF-MARKET-SCAN
version: 1.0.0
status: active
owner: AGENT-MARKET-RADAR
---

# Varredura de mercado

## Trigger
Execução manual `/research radar`, revisão editorial ou agenda futura configurada. Cadência inicial: `UNKNOWN`; não alegar monitoramento contínuo sem automação real.

## Inputs
Janela desde a última varredura, territórios da marca, fontes/watchlists, conteúdos recentes e capacidade editorial.

## Agents
Market Radar → Creator Intelligence quando surgir player/formato → Content Strategist.

## Sequence
1. Carregar a última pesquisa para evitar duplicação.
2. Buscar fontes primárias de Java, frameworks, IA para desenvolvimento, GitHub, cloud/backend e ferramentas; observar discussões somente como sinal.
3. Registrar eventos com data/estado e descobrir players emergentes pertinentes.
4. Filtrar por impacto provável para a audiência, novidade, prazo e saturação.
5. Classificar `WATCH`, `RESEARCH_NOW`, `CONTENT_CANDIDATE` ou `DISMISS` com razão.
6. Encaminhar candidatos de notícia para `news_to_content`; creator para `reverse_engineer_creator`.

## Decision points
Popularidade não equivale a relevância. Um rumor pode entrar em `WATCH`, nunca como fato. Se nada superar o backlog evergreen, não forçar conteúdo.

## Outputs
Snapshot datado, itens deduplicados, fontes, classificação, prazo e próxima revisão proposta.

## Memory updates
Salvar em `knowledge/research/AAAA-MM-DD-market-scan.md`; atualizar watchlist somente como alvo de pesquisa, não conclusão.

## Quality gates
Fonte/data para cada fato, distinção entre sinal e conclusão, ligação clara com Java/backend ou descarte.

## Failure and escalation
Sem acesso atual a fontes: registrar que a varredura não ocorreu. Não reutilizar snapshot antigo como estado presente.
