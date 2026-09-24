---
id: WF-REQUEST-ROUTING
version: 1.0.0
status: active
owner: AGENT-ORCHESTRATOR
---

# Roteamento de solicitação

## Trigger
Qualquer pedido aberto ou comando dirigido ao sistema.

## Inputs
Texto do pedido, modo opcional, anexos, prazo e estado atual.

## Agents
Orchestrator e o menor subconjunto necessário do catálogo.

## Sequence
1. Classificar intenção: `direction`, `idea`, `news`, `research`, `hooks`, `script`, `review`, `production`, `distribution`, `metrics`, `experiment`, `strategy` ou `system`.
2. Avaliar risco: factual recente, técnico, reputacional, externo e irreversível.
3. Escolher profundidade: FAST, STANDARD ou DEEP.
4. Carregar Brand OS, estratégia, perfil e memória pertinente.
5. Executar workflow correspondente; agregar conflitos pela hierarquia de verdade.
6. Responder com recomendação, porquê, artefato e próxima ação.

## Decision points
- Pedido ambíguo mas reversível: assumir objetivo mais útil e declarar.
- Notícia/versão/tendência: Market Radar e pesquisa atual obrigatórios.
- Claim técnico material: Technical Reviewer.
- Mudança estrutural: System Architect + aprovação humana.

## Outputs
Plano interno de rota e resposta sintetizada; nunca transcrição da conversa entre agentes.

## Memory updates
Somente se surgir artefato, decisão ou preferência confirmada; perguntas exploratórias não sujam memória.

## Quality gates
Intenção atendida, modo proporcional, fontes quando exigidas, nenhuma experiência inventada.

## Failure and escalation
Se faltar uma escolha que altera materialmente o resultado, apresentar o trade-off e pedir direção. Falta de dados observacionais vira `UNKNOWN`, não bloqueio automático.
