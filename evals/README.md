# Evals e regressão

`cases.json` define roteamento, agentes obrigatórios, resultado qualitativo e anti-patterns. Rode:

```bash
python3 evals/run_evals.py
```

O runner verifica deterministicamente roteamento e contratos esperados. Os critérios de conteúdo são revisão humana/model-based futura: compare a resposta do Orchestrator com `qualitative` e `forbidden`, registrando pass/fail e justificativa. Toda mudança em agente central, roteamento, workflow, scoring ou Brand OS deve rodar os mesmos casos; acrescente caso para bugs novos antes de mudar comportamento.
