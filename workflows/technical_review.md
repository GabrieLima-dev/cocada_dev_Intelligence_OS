---
id: WF-TECHNICAL-REVIEW
version: 1.0.0
status: active
owner: AGENT-TECHNICAL-REVIEWER
---

# Revisão técnica

## Trigger
Roteiro/caption contém afirmação técnica material, código, versão, segurança, performance ou arquitetura.

## Inputs
Artefato, claims, stack/versão, fontes e nível de simplificação.

## Agents
Technical Reviewer; Market Radar para versões recentes; Scriptwriter para correção.

## Sequence
1. Extrair claims verificáveis e dar severidade de erro potencial.
2. Verificar primeiro os claims centrais em documentação primária ou teste reproduzível.
3. Marcar `correct`, `pedagogical_simplification`, `context_needed`, `incorrect` ou `unverifiable`.
4. Propor correção mínima mantendo voz e duração.
5. Revalidar versão corrigida; emitir verdict.

## Decision points
Simplificação é aceita se não induzir modelo mental errado no escopo declarado. Opinião arquitetural requer trade-off, não “certo/errado”.

## Outputs
Parecer estruturado, referências, testes e verdict.

## Memory updates
Parecer junto ao roteiro; errata reusable somente via curadoria.

## Quality gates
Todos os claims de alta severidade resolvidos; versão/escopo explícitos.

## Failure and escalation
Sem fonte/teste suficiente: bloquear claim ou reescrevê-lo como incerteza, nunca inferir certeza.
