# COCADA Content Intelligence OS — instruções do repositório

Este arquivo orienta Codex e qualquer agente que trabalhe neste repositório. Não copie conhecimento editorial para cá: identidade vive no Brand OS, apostas vivem na estratégia e evidências vivem na memória.

## Missão operacional

Construir e operar uma rede de inteligência que transforma:

```text
dado → análise → padrão → mecanismo → princípio → estratégia
     → ideia → produção → publicação → métricas → aprendizado
```

O produto é o ciclo fechado, não o roteiro isolado.

## Bootstrap obrigatório

Antes de decidir ou criar:

1. Leia `brand/BRAND_OS.md`.
2. Leia `strategy/CURRENT_STRATEGY.md`.
3. Leia `memory/creator/profile.md`.
4. Consulte somente a memória e o conhecimento pertinentes.
5. Use `agents/orchestrator/AGENT.md` e o workflow correspondente.

Todos os especialistas devem ler o Brand OS. O usuário conversa com o Orchestrator, que escolhe a menor cadeia suficiente e sintetiza os handoffs.

## Hierarquia de verdade

```text
BRAND_OS
> CURRENT_STRATEGY
> memória validada e dados observados
> tarefa atual
> conhecimento geral
```

Uma instrução explícita de Gabriel prevalece para a tarefa atual. Fatos recentes pesquisados podem corrigir conhecimento factual desatualizado, mas não redefinem a marca. Conflitos relevantes devem ser apresentados ou registrados, nunca resolvidos silenciosamente por conveniência.

## Regras editoriais invariantes

- Posicionamento: “Backend e Java como eles aparecem fora do tutorial.”
- Comece pelo motivo para se importar, não pelo nome do assunto.
- Autoridade vem de experiência verificável, raciocínio, investigação, didática e demonstração; nunca de pose de guru.
- Não invente vivências de Gabriel. Se não estiver no perfil ou na tarefa, confirme ou marque `UNKNOWN`.
- Rotina pura tende a Story; rotina + conflito/aprendizado/insight pode virar conteúdo principal.
- Notícias exigem pesquisa atual, fonte primária, data, impacto e distinção `FACT/INTERPRETATION/HYPOTHESIS`.
- Conteúdo técnico exige revisão proporcional ao risco. Simplificação pedagógica não pode criar modelo mental falso.
- Engenharia reversa abstrai `conteúdo → padrão → mecanismo → princípio → adaptação`; nunca copia expressão criativa.

## Roteamento e profundidade

Use `workflows/request_routing.md`.

- `FAST`: decisão reversível, baixo risco, 1–2 especialistas.
- `STANDARD`: fluxo normal e gates pertinentes.
- `DEEP`: pesquisa, comparação, alto risco ou mudança estrutural.

O modo muda a profundidade, não a exigência de verdade. Notícias e fatos voláteis continuam exigindo pesquisa; claims técnicos materiais continuam exigindo revisão.

## Ciclo de conteúdo

```text
content/inbox
→ content/ideas
→ content/selected
→ content/scripts
→ content/production
→ content/published
→ content/archive
```

Use ID imutável `CNT-AAAA-NNNN`. Mover de estágio não muda ID. Não promova uma ideia sem score justificado e decisão editorial; score apoia julgamento e não o substitui.

Pipeline de qualidade padrão:

```text
IDEA → STRATEGIC REVIEW → HOOK/SCRIPT → TECHNICAL OR FACTUAL REVIEW
     → CREATIVE REVIEW → HUMAN APPROVAL → DISTRIBUTION PACKAGE
```

Conteúdo simples pode pular gates dispensáveis com motivo. Conteúdo técnico ou notícia não pula verificação. Publicação externa sempre requer ação/autorização humana.

## Evidência e memória

- Dados ausentes são `UNKNOWN`/`null`, nunca zero.
- Snapshots brutos em `analytics/events/` são append-only.
- Uma observação isolada não vira regra.
- Estágios: `OBSERVATION → HYPOTHESIS → STRONG_HYPOTHESIS → PATTERN → VALIDATED_PRINCIPLE`.
- Confiança: `LOW`, `MEDIUM`, `HIGH`, `VALIDATED`.
- Claims citam IDs/fontes, métrica, valor, janela, amostra, limites e revisão.
- Atualize o grafo por IDs e relações estáveis; não duplique a fonte canônica em outro diretório.

Depois de métricas maduras, use:

```text
Analytics Lab → Experiment Lab → Knowledge Curator → Content Strategist
```

Estratégia só muda após decisão aprovada e registrada.

## Limites de escrita

- Especialistas escrevem somente nos destinos declarados em seus contratos.
- Orchestrator consolida artefatos e decisões, não raciocínio privado.
- `content/inbox/` recebe captura; `ideas/` recebe estrutura; `selected/` exige escolha.
- Não mover nem reescrever `java_arquitetura_ms/`; são fontes locais, não prova final de claim recente.
- Não criar integração falsa, segredo no repositório, publicação automática ou autoaprovação.

## Evolução e versionamento

Brand OS, estratégia, agentes, workflows, schemas, mecanismos e pesos são versionados.

```text
observação → evolution/proposals → evidência → avaliação
          → aprovação de Gabriel → implementação → evals → changelog
```

Agentes nunca alteram suas próprias regras silenciosamente. O System Architect pode propor novo agente, remoção, fusão, divisão, prompt, critério, peso, workflow ou schema; não pode aprovar a proposta.

Ao mudar comportamento:

1. faça a menor alteração suficiente;
2. atualize a versão do artefato;
3. preserve estratégia anterior em `strategy/history/` quando aplicável;
4. atualize `CHANGELOG.md`;
5. rode `python3 scripts/cocada_os.py doctor`;
6. rode `python3 evals/run_evals.py`.

## Convenções

- Conteúdo: `CNT-AAAA-NNNN`.
- Decisão: `DEC-NNNN`.
- Experimento: `EXP-AAAA-NNNN`.
- Aprendizado: `LRN-AAAA-NNNN`.
- Proposta: `EVO-AAAA-NNNN`.
- Datas: ISO 8601; timestamps em UTC quando possível.
- Markdown + YAML front matter para artefatos humanos; JSON/JSON Schema para eventos e contratos formais.
- Arquivos e IDs em inglês técnico estável; conteúdo e documentação podem usar português.

## Resposta ao usuário

Não exponha a conversa entre agentes. Entregue apenas o necessário, normalmente:

```text
RECOMENDAÇÃO
POR QUÊ
HOOK / ARTEFATO
EXECUÇÃO
PRÓXIMA AÇÃO
```

Se houver direção claramente melhor, escolha. Se uma decisão material depender de dado que não existe, declare a suposição ou peça a informação mínima.

## Auditoria rápida

```bash
python3 scripts/cocada_os.py doctor
python3 evals/run_evals.py
```

`evidência > opinião`, `mudança pequena > reescrita`, `evolução versionada > mutação silenciosa`, `aprendizado acumulado > prompt gigante`.
