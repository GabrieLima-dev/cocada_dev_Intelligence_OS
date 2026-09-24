---
id: STRATEGY-CURRENT
version: 1.0.0
status: active
effective_from: 2026-09-24
review_at: UNKNOWN
owner: Gabriel
---

# Estratégia atual

## Objetivo da fase

Construir uma base editorial reconhecível e gerar dados comparáveis sem sacrificar credibilidade. Até existirem métricas suficientes, priorizar consistência de posicionamento e testes controlados, não otimização prematura.

## Mix de referência

| Pilar | Alvo inicial | Papel |
|---|---:|---|
| Java | 30% | autoridade técnica e aplicação real |
| Backend/arquitetura | 30% | diferenciação central |
| Notícias relevantes | 20% | timing e interpretação |
| Educação | 20% | clareza, salvamentos e alcance qualificado |

Tolerância operacional: ±10 pontos por janela, principalmente quando o timing justificar. Janela e frequência atuais: `UNKNOWN`.

## Prioridades

1. Validar séries repetíveis que conectem prática e ensino.
2. Coletar baseline de retenção, conclusão, shares e saves por formato.
3. Testar hooks de experiência pessoal versus consequência/erro em conteúdos comparáveis.
4. Construir banco de conteúdos com IDs, origem e dados completos.

## Séries ativas

Java na Vida Real; Backend sem Enrolação; A Task Dizia que Era Simples; Bug da Semana; Agora Eu Entendi; Notícia para Dev; Código que Funciona, Mas...; Backend Visual.

## Hipóteses atuais

| ID | Hipótese | Confiança | Estado |
|---|---|---|---|
| HYP-001 | Experiência real + explicação aumenta identificação sem reduzir autoridade. | LOW | a testar |
| HYP-002 | Problema visível nos 3 primeiros segundos melhora retenção inicial. | LOW | a testar |
| HYP-003 | Diagramas simples elevam salvamentos em arquitetura/backend. | LOW | a testar |

São hipóteses de partida, não resultados observados.

## Experimentos ativos

Nenhum. Criar em `experiments/active/` antes de declarar teste ativo.

## Guardrails

- Notícias: fonte original, data, impacto e ângulo cocada.dev.
- Conteúdo técnico: revisão proporcional ao risco; exemplos executáveis quando a exatidão depender de código.
- Experiência pessoal: somente fatos fornecidos ou confirmados por Gabriel.
- Vida cotidiana sem insight: Stories.
- Não alterar pesos editoriais por menos de uma janela comparável definida.

## Critérios de revisão

Revisar após dados suficientes para comparação ou mudança explícita de objetivo. O review deve citar conteúdos, métricas normalizadas, limitações e decisão. Arquivar a versão anterior em `strategy/history/`.
