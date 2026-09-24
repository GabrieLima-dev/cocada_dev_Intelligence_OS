# Portabilidade de runtime e modelos

O núcleo não depende de chamadas de API, formato proprietário de tool call ou banco específico. Agentes são contratos; workflows são sequências; memória usa IDs e arquivos.

## Envelope de execução

Todo runtime monta contexto na ordem de `config/runtime_profiles.yaml` usando `templates/RUN_CONTEXT_TEMPLATE.md`. O agente recebe apenas:

1. fontes canônicas;
2. contrato do seu papel;
3. workflow ativo;
4. artefatos da tarefa;
5. output esperado e gates.

Isso mantém a V1 adequada ao perfil preferencial GPT-5.6 Sol sem colocar decisões de modelo dentro de Brand OS ou memória. Claude, Codex, outros modelos OpenAI ou execução humana podem cumprir o mesmo contrato.

## Adaptação de fornecedor

Um adaptador futuro traduz nível de profundidade, tools, limites de contexto e structured output. Ele não pode mudar IDs, source of truth, autorização externa ou critérios de evidência. Se um modelo exigir mudança semântica no contrato, use o workflow de evolução e evals.

## Handoff mínimo

Handoffs devem ser pequenos e verificáveis: objetivo, input IDs, conclusão/artefato, evidência, incerteza, gate e próximo responsável. Não transportar cadeia de pensamento ou transcrição entre agentes.
