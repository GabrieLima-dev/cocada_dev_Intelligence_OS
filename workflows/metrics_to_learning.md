---
id: WF-METRICS-TO-LEARNING
version: 1.0.0
status: active
owner: AGENT-KNOWLEDGE-CURATOR
---

# Métricas para aprendizado

## Trigger
Novo snapshot maduro de métricas, conclusão de experimento ou pedido `/analyze`.

## Inputs
Eventos brutos, content records, objetivos, baseline, janela, experimento e contexto de distribuição.

## Agents
Analytics Lab → Experiment Lab → Knowledge Curator → Content Strategist.

## Sequence
1. Validar integridade, unidade, denominador, plataforma e janela.
2. Calcular taxas e comparar apenas grupos equivalentes; declarar baseline `UNKNOWN` se ausente.
3. Identificar onde ocorreu o sinal: parar, assistir, concluir, compartilhar/salvar, visitar, seguir/converter.
4. Formular explicações alternativas; checar se havia experimento pré-declarado.
5. Criar claim com evidência e estágio conservador.
6. Atualizar grafo/memória; recomendar replicação ou ajuste estratégico.
7. Estratégia só muda após decisão aprovada e documentada.

## Decision points
- Um item: `OBSERVATION`.
- Repetição em amostra comparável: pode virar `HYPOTHESIS/STRONG_HYPOTHESIS` conforme qualidade.
- `PATTERN/VALIDATED_PRINCIPLE`: critérios definidos, replicação e revisão de alternativas.

## Outputs
Relatório, claim, confiança, limitações, próximo teste e impacto proposto.

## Memory updates
Evento bruto append-only; relatório versionado; learning/grafo curados; decisão separada.

## Quality gates
Rastreabilidade aos IDs, amostra explícita e nenhuma causalidade além do desenho.

## Failure and escalation
Dados incompatíveis ou incompletos: diagnóstico de qualidade e plano de coleta; não produzir falsa conclusão.
