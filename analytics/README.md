# Analytics

`events/` contém snapshots brutos imutáveis. `reports/` contém análises derivadas reproduzíveis. Baselines curados vivem em `memory/performance/baselines.yaml` e precisam de plataforma, formato e janela comparáveis.

Taxas devem declarar denominador. Saves e shares absolutos não são comparados entre alcances muito diferentes sem taxa correspondente. Dados indisponíveis são `null/UNKNOWN`, não zero.
