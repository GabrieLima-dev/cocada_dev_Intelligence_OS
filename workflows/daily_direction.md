---
id: WF-DAILY-DIRECTION
version: 1.0.0
status: active
owner: AGENT-CONTENT-STRATEGIST
---

# “O que devo produzir hoje?”

## Trigger
Falta de direção, `/idea` sem tema ou pedido explícito de prioridade diária.

## Inputs
Tempo/capacidade se conhecidos, backlog, mix recente, estratégia, notícias com prazo, experimentos e métricas.

## Agents
Orchestrator → Market Radar (se timing exigir) → Content Strategist → Idea Lab → Hook Lab; Brand Strategist como gate.

## Sequence
1. Verificar conteúdos `NOW`, produção pendente e compromisso existente.
2. Identificar lacuna estratégica e objetivo mais útil hoje.
3. Checar notícia apenas se puder superar a melhor opção evergreen.
4. Gerar no máximo cinco candidatas; pontuar e avaliar esforço.
5. Escolher uma recomendação e uma alternativa de menor esforço.
6. Gerar hook/primeiro frame da vencedora, sem roteiro completo salvo pedido.

## Decision points
- Deadline real vence score semelhante.
- Conteúdo já em produção vence ideia nova salvo perda clara de timing.
- Rotina pura vai para Story; conflito/aprendizado pode ir a Reel.

## Outputs
“Faça X hoje”, razão, hook, formato, duração, execução mínima, prioridade e alternativa.

## Memory updates
Só após Gabriel escolher: mover para `selected/` e registrar decisão quando relevante.

## Quality gates
Uma direção clara, não calendário genérico; consideração explícita de esforço e timing.

## Failure and escalation
Capacidade desconhecida: oferecer opção principal e fallback curto, marcando a suposição.
