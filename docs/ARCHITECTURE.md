# Arquitetura

## Camadas

```text
Interface humana/comandos
          ↓
Orchestrator — intenção, profundidade, plano, síntese
          ↓
Especialistas — artefatos e pareceres estruturados
          ↓
Quality gates — estratégia, fatos, técnica, criação
          ↓
Content lifecycle — inbox → ideia → selecionado → roteiro → produção → publicado
          ↓
Eventos de métricas → análise → experimento → curadoria
          ↓
Memória + proposta de estratégia/evolução (aprovação humana)
```

## Princípios

- Estado em arquivos, contratos explícitos e IDs estáveis.
- Markdown para julgamento humano; YAML/JSON para interoperabilidade.
- Agente é um papel com input/output, não um processo autônomo permanente.
- Orchestrator revela decisão e justificativa, não conversa interna.
- Fluxos simples pulam gates dispensáveis de forma registrada; risco técnico/notícia nunca pula verificação.
- Integrações futuras entram por adaptadores; o núcleo não conhece APIs de plataforma.

## Knowledge graph

`memory/content/graph.yaml` representa nós e arestas simples: conteúdo usa hook/mecanismo, pertence a série/pilar, testa hipótese, recebe evento e produz aprendizado. O schema evita acoplamento e permite migração posterior para SQL ou graph database mantendo IDs.

## Source of truth

1. `brand/BRAND_OS.md`: identidade e limites.
2. `strategy/CURRENT_STRATEGY.md`: aposta atual.
3. Memória validada e eventos observados.
4. Solicitação atual de Gabriel.
5. Conhecimento geral do modelo.

Fato recente pesquisado pode corrigir conhecimento factual antigo, mas não muda marca. Conflitos relevantes são apresentados ao usuário ou registrados em decisão.
