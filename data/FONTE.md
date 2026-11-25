# Fonte e inspeção da planilha Porsche

Data da coleta: 2026-11-25.

## Resultado

Localizada uma cópia pública de `porsche_database_sanitized.xlsx`, com 100 vendas, usada no desafio da DIO “Criando uma Dashboard da Porsche com Agentes de IA”. O arquivo foi copiado sem alterações para `data/porsche_database_sanitized.xlsx`. Por conter colunas brutas com nomes, ele fica apenas no ambiente local e está ignorado pelo Git.

A página oficial do desafio informa que a base possui 100 vendas e que a planilha é fornecida pronta. O repositório oficial público da DIO não hospeda o `.xlsx`; ele contém apenas `index.html`. Por isso, o arquivo foi obtido de um espelho público e identificado pelo nome, estrutura e correspondência integral com os dados do dashboard oficial.

## URLs da fonte

URL exata do arquivo baixado, fixada no commit do espelho:

https://raw.githubusercontent.com/Rogersamacedo/Dashboard-porsche-vendas/5e4a47ed6a64fdc5d2b4b5a1d580e931f78c1b9d/porsche_database_sanitized.xlsx

Página do arquivo no repositório de origem:

https://github.com/Rogersamacedo/Dashboard-porsche-vendas/blob/5e4a47ed6a64fdc5d2b4b5a1d580e931f78c1b9d/porsche_database_sanitized.xlsx

Repositório de origem:

https://github.com/Rogersamacedo/Dashboard-porsche-vendas

Página oficial do desafio:

https://www.dio.me/projects/criando-agentes-de-criacao-de-dashboards-com-excel-e-claude-code

Repositório oficial do dashboard da DIO:

https://github.com/digitalinnovationone/dashboard_porsche_sales

Arquivo oficial do dashboard, que cita `Base: porsche_database_sanitized.xlsx`:

https://github.com/digitalinnovationone/dashboard_porsche_sales/blob/main/index.html

Commit oficial do dashboard:

https://github.com/digitalinnovationone/dashboard_porsche_sales/commit/ce783e375162729efb1fd449a6357d9b36eb48a1

## Integridade

- Tamanho: 28.623 bytes.
- SHA-256 do arquivo local e do arquivo remoto: `f874650657ca4e1a99fd4462b297bfc5fd9915e8e693956d9cec47eda2cb2e2d`.
- Git blob SHA: `7f1007dece9a0239d60d524fa69e0b498c3bb256`.
- O mesmo Git blob SHA foi encontrado em outros três espelhos públicos:
  - https://github.com/WashingtonBM/Dashboard-da-Porsche/blob/54b90d084a58d39e167a9bd8bec58382bfc51807/Base%20de%20Dados
  - https://github.com/Urouge1/Projeto-Porsche/blob/ac9ddfb7409ba166960728a1acaa887aaee923b8/base.xlsx
  - https://github.com/mimelotti98/Projeto-DIO-Dashboard-com-IA/blob/da9b7ac1726581a21a382a484f07d4eac8eb0b7c/base-dados-excel
- O arquivo local foi comparado byte a byte com a cópia baixada da fonte. Os bytes são idênticos.

## Confirmação contra o dashboard oficial

O `index.html` oficial contém um array `rawRows` com exatamente 100 registros. A projeção das oito colunas sanitizadas usadas pelo dashboard (`SaleDateSanitized`, `PorscheModelSanitized`, `ModelYearSanitized`, `CitySanitized`, `StateSanitized`, `PayMethodSanitized`, `SalesPriceSanitized` e `DeliveryStatusSanitized`) foi comparada com esse array.

Resultado: 100 de 100 linhas correspondentes, zero divergências, na mesma ordem. No dashboard, datas `INVALID` aparecem como string vazia.

## Estrutura inspecionada

Método: Python 3.14 com biblioteca padrão (`zipfile` e `xml.etree.ElementTree`) para leitura direta do OOXML. `openpyxl` não estava instalado no ambiente e nenhuma dependência foi adicionada.

- Abas: 1.
- Nome da aba: `Sanitized`.
- Dimensão declarada: `A1:U101`.
- Linhas não vazias: 101, sendo 1 cabeçalho e 100 registros.
- Colunas: 21, sendo 12 campos originais e 9 campos sanitizados.
- `sale_id`: 100 valores únicos, de 6 a 105.
- Nenhuma célula vazia nas 100 linhas de dados.
- `SaleDateSanitized`: 24 valores `INVALID`.
- Das 76 datas válidas, 18 são posteriores a 2026-11-25, data do projeto. Elas podem representar agendamentos e não foram usadas para análise temporal.
- Demais colunas sanitizadas: nenhum valor `INVALID`.

Cabeçalhos, em ordem:

1. `sale_id`
2. `sale_date`
3. `SaleDateSanitized`
4. `customer_name`
5. `porsche_model`
6. `PorscheModelSanitized`
7. `model_year`
8. `ModelYearSanitized`
9. `sale_price`
10. `SalesPriceSanitized`
11. `vehicle_mileage`
12. `VehicleMileageSanitized`
13. `payment_method`
14. `PayMethodSanitized`
15. `city`
16. `CitySanitized`
17. `state`
18. `StateSanitized`
19. `salesperson`
20. `delivery_status`
21. `DeliveryStatusSanitized`

## Exemplos de campos sanitizados

| sale_id | Campo original | Valor original | Campo sanitizado | Valor sanitizado |
|---:|---|---|---|---|
| 6 | sale_date | `2024-02-30` | SaleDateSanitized | `INVALID` |
| 6 | sale_price | `$79,500.00` | SalesPriceSanitized | `79500.00` |
| 6 | vehicle_mileage | `9,800 miles` | VehicleMileageSanitized | `9800` |
| 6 | payment_method | `Credit card` | PayMethodSanitized | `Credit Card` |
| 6 | city / state | `boston` / `ma` | CitySanitized / StateSanitized | `Boston` / `MA` |
| 7 | model_year | `twenty twenty four` | ModelYearSanitized | `2024` |
| 7 | sale_price | `235000 USD` | SalesPriceSanitized | `235000.00` |
| 7 | vehicle_mileage | `1.200 mi` | VehicleMileageSanitized | `1200` |
| 7 | state | `Washington` | StateSanitized | `WA` |
| 8 | sale_date | serial Excel `45400` | SaleDateSanitized | `2024-04-18` |
| 8 | sale_price | `USD 112.750` | SalesPriceSanitized | `112750.00` |
| 8 | payment_method | `Financing plan` | PayMethodSanitized | `Financing` |
| 10 | sale_price | `$121k` | SalesPriceSanitized | `121000.00` |
| 10 | vehicle_mileage | `zero miles` | VehicleMileageSanitized | `0` |
| 10 | payment_method | `bank-transfer` | PayMethodSanitized | `Bank Transfer` |
| 10 | delivery_status | `delivered!!!` | DeliveryStatusSanitized | `Delivered` |

## Ressalva sobre “sanitizada”

Neste arquivo, “sanitizada” significa normalização de formatos e valores, com colunas originais preservadas ao lado das colunas tratadas. O arquivo não é anonimizado: as colunas `customer_name` e `salesperson` permanecem preenchidas. Os nomes não foram reproduzidos neste resumo.

Também foi localizada uma versão reduzida de 12 colunas em `DS-RFTA/dashboard_Porsche/dados.xlsx`, mas ela não é byte a byte o arquivo de 21 colunas identificado pelo nome `porsche_database_sanitized.xlsx` e não foi usada como fonte.
