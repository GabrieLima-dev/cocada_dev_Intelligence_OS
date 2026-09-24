---
id: WF-NEWS-TO-CONTENT
version: 1.0.0
status: active
owner: AGENT-MARKET-RADAR
---

# Notícia para conteúdo

## Trigger
Pedido sobre notícia, lançamento, versão, mudança recente ou tendência.

## Inputs
Tema/evento, data atual, plataforma, audiência e objetivo.

## Agents
Market Radar → Technical Reviewer quando técnico → Content Strategist → Idea Lab → Orchestrator.

## Sequence
1. Descobrir e abrir a fonte original.
2. Registrar data do anúncio, data do evento/release, versão e estado (proposta, preview, GA, depreciação).
3. Confirmar claims essenciais e separar `FACT`, `INTERPRETATION`, `HYPOTHESIS`.
4. Avaliar relevância para Java/backend: impacto, abrangência, ação e prazo.
5. Descartar se só houver novidade sem consequência.
6. Encontrar ângulo cocada.dev: “por que importa” + contexto + demonstração/decisão.
7. Criar e pontuar até três ideias; executar pipeline normal se selecionada.

## Decision points
- Fonte original indisponível: declarar limitação e não tratar rumor como fato.
- Impacto baixo: responder que não vale conteúdo principal; opcionalmente Story.
- Timing expirado: buscar ângulo evergreen ou arquivar.

## Outputs
Briefing datado, veredito `MAKE/CONSIDER/SKIP`, ângulo e ideia prioritária.

## Memory updates
Snapshot em `knowledge/research/` e origem no conteúdo. Nunca atualizar pesquisa antiga apagando o que era conhecido.

## Quality gates
Fonte, data, versão, impacto e distinção fato/interpretação/hipótese.

## Failure and escalation
Conflito entre fontes: citar ambos, buscar autoridade superior e marcar incerteza.
