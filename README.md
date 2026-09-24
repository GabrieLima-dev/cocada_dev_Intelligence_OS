# COCADA Content Intelligence OS

Sistema operacional de inteligência de conteúdo da cocada.dev. A V1 organiza uma rede de agentes, memória baseada em evidência e workflows fechados para transformar pesquisa e experiência real em conteúdo, produção, métricas e aprendizado.

```text
observar → analisar → decidir → criar → revisar → produzir → medir → aprender → ajustar
```

Não é uma automação de postagem nem um conjunto solto de prompts. É uma arquitetura local, legível por humanos e preparada para automação futura sem depender de um fornecedor de modelo.

## Começo rápido

```bash
python3 scripts/cocada_os.py doctor
python3 scripts/cocada_os.py route "Não sei o que postar hoje" --mode STANDARD
python3 scripts/cocada_os.py new-content --title "DTO fora do tutorial" --pillar backend_architecture --objective authority
python3 scripts/cocada_os.py score --input examples/idea-score.json
```

Fluxo diário recomendado:

1. Converse com o Orchestrator descrito em `agents/orchestrator/AGENT.md` ou use um comando de `docs/COMMANDS.md`.
2. O Orchestrator lê marca, criador, estratégia, memória e contexto atual; escolhe o menor workflow suficiente.
3. A ideia selecionada percorre `workflows/idea_to_publish.md`.
4. Depois da publicação, registre métricas com `record-metrics`; o evento alimenta `workflows/metrics_to_learning.md`.
5. Só evidência acumulada altera hipóteses, pesos ou estratégia.

## Mapa da arquitetura

- `brand/`: identidade estável e limites editoriais.
- `strategy/`: objetivos e hipóteses em vigor; histórico separado.
- `agents/`: contratos dos 18 especialistas, incluindo Orchestrator e Meta Agent.
- `workflows/`: sequências, decisões, gates e handoffs, incluindo varredura de mercado sem automação fictícia.
- `memory/`: fatos do criador, audiência, decisões, padrões e aprendizados.
- `knowledge/`: mecanismos, hooks, creators, plataformas e fontes técnicas.
- `content/`: ciclo de vida dos conteúdos e séries editoriais.
- `analytics/` e `experiments/`: eventos brutos, baselines e testes.
- `schemas/` e `templates/`: contratos formais reutilizáveis.
- `evolution/`: propostas, aprovação e histórico de evolução segura.
- `evals/`: casos de regressão qualitativa.
- `scripts/`: utilitários locais sem dependências de terceiros.

Detalhes: `docs/ARCHITECTURE.md`, `docs/GOVERNANCE.md`, `docs/OPERATIONS.md` e `docs/PORTABILITY.md`.

## Como registrar conteúdo

Use `new-content` para gerar o próximo ID anual e um arquivo com front matter. Complete os campos `UNKNOWN`, pontue em `workflows/idea_scoring.md` e só mova o arquivo conforme os gates. O ID nunca muda quando o arquivo muda de estágio.

## Como inserir métricas e aprendizado

Exporte métricas da plataforma, preserve os valores brutos e execute:

```bash
python3 scripts/cocada_os.py record-metrics CNT-2026-0001 --input metrics.json
```

Isso cria um evento imutável em `analytics/events/`. Depois, siga `workflows/metrics_to_learning.md`; o Knowledge Curator registra afirmação, evidência, amostra e confiança em `memory/learnings/`. Não há promoção automática para regra.

## Como adicionar agente, workflow ou skill

- Agente: copie `templates/AGENT_TEMPLATE.md`, declare leituras/escritas, limites e handoffs; adicione ao catálogo e aos evals.
- Workflow: copie `templates/WORKFLOW_TEMPLATE.md`; defina trigger, entradas, sequência, decisões, saídas, atualizações de memória e gates.
- Skill: siga `skills/README.md`; uma skill empacota uma capacidade recorrente, mas não duplica Brand OS nem estado estratégico.
- Evolução: crie uma proposta por `templates/EVOLUTION_PROPOSAL_TEMPLATE.md` e siga `workflows/system_evolution.md`.

## Estado inicial honesto

Não existem métricas históricas importadas, baselines validados nem preferências de produção observadas. Esses campos estão marcados como `UNKNOWN`. Os dois guias em `java_arquitetura_ms/` são fontes locais úteis para pesquisa e roteiros técnicos, sujeitos a revisão e atualização factual.

## Requisitos

Python 3.10+ para a CLI. Nenhum pacote externo é necessário. A arquitetura em Markdown, YAML e JSON Schema continua utilizável sem a CLI.
