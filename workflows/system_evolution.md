---
id: WF-SYSTEM-EVOLUTION
version: 1.0.0
status: active
owner: AGENT-SYSTEM-ARCHITECT
---

# Evolução segura do sistema

## Trigger
Falha repetida, gap, redundância ou melhoria proposta.

## Inputs
Problema, pelo menos três ocorrências quando não crítico, artefatos afetados, opções e evals.

## Agents
System Architect → dono do domínio → Orchestrator → Gabriel.

## Sequence
1. Registrar proposta a partir do template, sem editar sistema.
2. Diagnosticar se a causa é dados, contrato, workflow, peso, prompt ou agente.
3. Comparar não mudar, ajuste mínimo e alternativa estrutural.
4. Definir migração, versão, rollback e evals.
5. Gabriel aprova ou rejeita explicitamente.
6. Se aprovada, mover snapshot para `approved/`, implementar menor mudança, versionar e rodar doctor/evals.
7. Registrar changelog e resultado futuro; se rejeitada, mover para `rejected/` com motivo.

## Decision points
Risco crítico pode dispensar três ocorrências, mas não aprovação. Mudança grande deve ser fatiada.

## Outputs
Proposta, decisão, diff implementado, resultados de regressão e plano de observação.

## Memory updates
Decision log, pasta de evolução e changelog; nunca apagar proposta rejeitada.

## Quality gates
Aprovação humana, versão, testes, reversibilidade e ausência de mutação silenciosa.

## Failure and escalation
Evals pioram: reverter ou corrigir antes de marcar concluído. Falta de dados: manter proposta aberta, não adivinhar.
