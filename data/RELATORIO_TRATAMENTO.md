# Relatório de tratamento

- Fonte: `porsche_database_sanitized.xlsx`
- SHA-256 da fonte: `f874650657ca4e1a99fd4462b297bfc5fd9915e8e693956d9cec47eda2cb2e2d`
- Registros preparados: 100
- Datas inválidas convertidas para nulo: 24
- Campos mantidos: `data`, `modelo`, `ano`, `preco`, `quilometragem`, `pagamento`, `cidade`, `estado`, `entrega`
- Campos descartados: todas as colunas brutas, incluindo nomes de clientes e vendedores.
- Preço convertido para número decimal; ano e quilometragem para inteiro.
- Data validada no formato ISO; `INVALID` virou nulo.
- Nenhuma fórmula foi mantida.
- Saídas: `vendas_sanitizadas.csv` e `vendas_sanitizadas.json`.
