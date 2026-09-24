# Operação

## Rotina editorial

1. Capture fatos/ideias em `content/inbox/`.
2. Para “o que postar hoje”, rode `workflows/daily_direction.md` com o modo adequado.
3. Registre a ideia escolhida, pontue e atribua prioridade `NOW/NEXT/LATER/EXPERIMENT/ARCHIVE`.
4. Execute hook, roteiro e produção pelo workflow `idea_to_publish`.
5. Após publicar, complete `published_at`, plataforma e URL/ID externo.
6. Registre snapshots de métricas sem sobrescrever eventos anteriores.
7. Rode análise quando a janela estiver madura; crie aprendizado ou mantenha como observação.

## Modo de profundidade

- `FAST`: decisão reversível, baixo risco, 1–2 especialistas e resposta curta.
- `STANDARD`: fluxo padrão, 3–5 especialistas/gates pertinentes.
- `DEEP`: pesquisa, comparação, alto risco ou mudança estrutural; múltiplos pareceres e revisão completa.

## Prioridade

- `NOW`: oportunidade com prazo ou melhor próxima ação.
- `NEXT`: evergreen forte pronto para o próximo ciclo.
- `LATER`: valor potencial sem urgência/preparo.
- `EXPERIMENT`: selecionado primariamente para testar hipótese.
- `ARCHIVE`: descartado com motivo, preservado para aprendizado.

## Recuperação e auditoria

Eventos e decisões não devem ser apagados. Corrija com novo evento/versão. Execute `doctor` após alterações estruturais e `evals/run_evals.py` após mudar prompts, workflows, scoring ou roteamento.
