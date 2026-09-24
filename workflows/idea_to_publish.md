---
id: WF-IDEA-TO-PUBLISH
version: 1.0.0
status: active
owner: AGENT-ORCHESTRATOR
---

# Ideia até pacote de publicação

## Trigger
Gabriel escolhe uma ideia: “vamos fazer essa”.

## Inputs
Content ID, ideia selecionada, prazo, plataforma, capacidade e fontes.

## Agents
Strategist → Hook Lab → Scriptwriter → Technical Reviewer quando aplicável → Creative Director → Visual/Personal Brand → Video Editor → Distribution.

## Sequence
1. **Strategic review:** promessa, objetivo, público, mecanismo e prioridade.
2. **Hook:** variações; escolher fala + primeiro frame e payoff exigido.
3. **Script:** beat sheet e claims.
4. **Technical/factual review:** obrigatório para claim material; corrigir até `pass`.
5. **Creative review:** shot list, prova visual e gravabilidade.
6. **Production:** gravação e EDL; preservar versão do roteiro usada.
7. **Final review:** promessa entregue, clareza, marca, fonte/direitos e specs.
8. **Distribution package:** embalagem, CTA, plataformas e plano de medição.
9. Publicação só após ação/autorização humana; então mover cópia final para `published/` e manter ID.

## Decision points
- Conteúdo simples pode pular coach/editor formal com motivo registrado.
- Conteúdo técnico ou notícia nunca pula verificação.
- Falta de experiência pessoal concreta exige confirmação ou mudança de voz.

## Outputs
Roteiro aprovado, plano de gravação/edição, pacote de distribuição, claims/sources, versão e próximo checkpoint de métricas.

## Memory updates
Grafo recebe relações a série, mecanismos, hook, hipótese e fontes; publicação recebe timestamp/ID externo real.

## Quality gates
`strategic_pass`, `technical_or_factual_pass`, `creative_pass`, `final_human_approval`.

## Failure and escalation
Gate bloqueado retorna ao dono do artefato, não ao início inteiro. Conflito de marca/timing vai ao Orchestrator/Gabriel.
