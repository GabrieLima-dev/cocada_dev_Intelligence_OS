---
id: WF-REVERSE-ENGINEER-CREATOR
version: 1.0.0
status: active
owner: AGENT-CREATOR-INTELLIGENCE
---

# Engenharia reversa de creator

## Trigger
Pesquisa de referência, formato ou novo player.

## Inputs
Creator, plataforma, período, objetivo e tamanho de amostra.

## Agents
Creator Intelligence → Brand Strategist → Content Strategist.

## Sequence
1. Definir amostra e viés conhecido.
2. Codificar posicionamento, pilares, temas, hook/primeiro frame, storytelling, duração, edição, CTA, comentários, séries e sinais públicos.
3. Identificar outliers somente contra baseline público disponível; retenção não visível é `NOT_CONFIRMABLE`.
4. Classificar cada conclusão: `OBSERVABLE_DATA`, `PATTERN`, `STRONG_HYPOTHESIS`, `HYPOTHESIS`, `NOT_CONFIRMABLE`.
5. Abstrair `content → pattern → mechanism → principle`.
6. Propor adaptação original coerente com cocada.dev e risco de cópia.

## Decision points
Menos de cinco itens pode gerar observação, não padrão. Similaridade expressiva alta bloqueia adaptação.

## Outputs
Dossiê com amostra, evidência, mecanismos, princípios, adaptações e limites.

## Memory updates
`knowledge/creators/<slug>/AAAA-MM-DD.md`; princípio interno somente após curadoria.

## Quality gates
Links/datas, classificação epistêmica e ausência de cópia textual/visual.

## Failure and escalation
Dados removidos ou privados: registrar indisponibilidade, nunca preencher por memória vaga.
