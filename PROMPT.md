# Prompts e refinamentos

## Prompt inicial do agente

> Crie uma dashboard em HTML único para 100 vendas sanitizadas da Porsche. Escolha três perguntas de negócio úteis, crie filtros por modelo, estado, cidade, ano e pagamento, mostre receita, quantidade e ticket médio, e use uma direção visual Motorsport premium. Os dados devem ficar embutidos no HTML, sem backend e sem bibliotecas externas de gráficos.

## O que mudou até a versão final

1. As perguntas foram fechadas em mix de modelos, concentração geográfica e forma de pagamento. O mix usa famílias de modelos para evitar 40 barras fragmentadas, mas o filtro e o líder usam o modelo exato. Cada visual mostra receita, volume e ticket médio para evitar conclusões baseadas só em preço.
2. A moeda foi definida como USD, coerente com os estados e cidades da base.
3. A tabela auditável e a exportação CSV foram adicionadas para que qualquer indicador possa ser conferido.
4. Os filtros passaram a atualizar toda a página e a ser compartilhados por query string.
5. Foram explicitados os estados de carregamento, vazio e erro, além de teclado, contraste, movimento reduzido e mobile.
6. O tratamento passou a publicar somente as nove colunas sanitizadas. O XLSX bruto, que contém nomes, não entra no repositório.

## Prompt final usado na implementação

> Implemente `index.html` como um HTML único, completo e responsivo, sem bibliotecas externas de JavaScript ou gráficos. Leia `PRODUCT.md`, `.impeccable/surfaces/index-html.md` e o craft floor do Impeccable. Use `data/vendas_sanitizadas.json` e incorpore o array `rows` dentro do HTML. Não inclua o XLSX bruto nem nomes de clientes ou vendedores.
>
> Use a direção Motorsport premium confirmada: off-white, preto e vermelho, tipografia condensada e sans legível, painéis de bordas finas e precisão automotiva. Não use imagens, ícones decorativos ou em dash.
>
> Responda três perguntas: quais famílias de modelos puxam a receita, quais estados concentram as vendas e como os clientes pagam. O primeiro gráfico agrega 911, Taycan, Cayenne, Panamera, Macan e 718, enquanto o filtro de modelo e o KPI de líder usam o nome exato. Cada visual deve mostrar receita, quantidade e ticket médio. O KPI principal se chama Receita bruta e deixa claro que inclui os sete cancelamentos, sem representar lucro.
>
> Crie filtros nativos por modelo, estado, cidade, ano e pagamento. Eles devem atualizar KPIs, gráficos, contagem e tabela. Inclua Limpar filtros, Exportar CSV e sincronização com a query string. A tabela deve permitir auditar data, modelo, ano, cidade/UF, pagamento, entrega e preço. Trate as 24 datas inválidas sem afetar os demais cálculos.
>
> Garanta estados de loading, vazio e erro, acessibilidade por teclado, contraste AA, foco visível, `aria-live`, alternativas acessíveis para gráficos, `prefers-reduced-motion` e layout sem overflow a 375px. Formate valores em USD e datas em pt-BR. O rodapé deve dizer que o projeto é independente, usa dados sanitizados do desafio DIO e não tem vínculo oficial com a Porsche. Não crie links ou botões sem função.

## Ferramenta usada

Foi usado um agente de código no OpenCode, com as skills `antislop`, `impeccable` e `ui-ux-pro-max`, além de subagents para localizar a fonte, analisar os dados e implementar a interface. Não foi usado ChatGPT Canvas nem um agente pago.
