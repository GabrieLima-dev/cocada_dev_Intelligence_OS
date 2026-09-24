---
id: WF-IDEA-SCORING
version: 1.0.0
status: active
owner: AGENT-CONTENT-STRATEGIST
---

# Scoring de ideias

## Trigger
Ideia estruturada precisa de comparação ou prioridade.

## Inputs
Campos do conteúdo, evidência, timing, capacidade e `config/idea_scoring.yaml`.

## Agents
Content Strategist; Brand Strategist em alinhamento duvidoso; Idea Lab para reformulação.

## Sequence
1. Dar nota 0–5 a cada dimensão com justificativa de uma linha.
2. Calcular `sum((rating / 5) * weight)`; pesos somam 100.
3. Aplicar gates mínimos de marca/audiência.
4. Atribuir `NOW/NEXT/LATER`; usar `EXPERIMENT` quando o valor principal for aprendizado; `ARCHIVE` quando gate falhar ou ideia estiver superada.
5. Comparar score com timing, custo absoluto e diversidade do mix. Score orienta; não decide sozinho.

## Decision points
- Campo sem evidência recebe nota conservadora, não “média por padrão”.
- Alto timing pode elevar prioridade, mas não atravessa brand gate.
- `production_efficiency=5` significa fácil/baixo custo.

## Outputs
Score 0–100, notas, justificativas, gate, prioridade, maior força, maior risco e melhoria recomendada.

## Memory updates
Salvar o snapshot de pesos/notas no conteúdo; futuras mudanças de peso não reescrevem score histórico.

## Quality gates
Toda nota tem razão; evidência e gosto não são confundidos; ranking inclui custo/timing.

## Failure and escalation
Ideias incomparáveis são segmentadas por objetivo/formato antes do ranking.
