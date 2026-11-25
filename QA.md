# Relatório de verificação

## Dados

- Fonte: 100 registros, 21 colunas, nove sanitizadas.
- Saída: 100 registros, nove campos, zero fórmulas.
- Datas inválidas: 24, convertidas para nulo.
- Datas válidas posteriores a 2026-11-25: 18, mantidas como ressalva.
- Receita bruta: US$ 12.827.800,50.
- Ticket médio: US$ 128.278,01.
- Cancelamentos: sete, US$ 625.250,00.
- Modelos distintos: 40. Famílias usadas no gráfico: seis.
- Pagamentos distintos: nove. Estados: 33. Cidades: 79.
- Privacidade: 164 valores únicos de nomes verificados contra os arquivos públicos, zero correspondências.

## Testes automatizados

Comando:

```bash
python3 -m unittest discover -s tests -v
```

Resultado: cinco testes passando. Cobre conversão de tipos, data inválida, campo sanitizado ausente, ano inválido, preço negativo e consistência entre JSON e CSV.

## HTML e JavaScript

- `html-validate index.html`: passou, zero erros.
- JavaScript extraído e validado com `node --check`: passou.
- Nenhum script de patch, build ou dependência de gráficos no repositório.
- O HTML abre por `file://` e por servidor HTTP local.

## Navegador

Roteiro Playwright com Chromium: 87 de 87 verificações passando.

- Receita, ticket médio, contagem, modelo líder e três agregações conferidos contra o JSON.
- Estados exibem receita, participação, quantidade e ticket médio; pagamentos exibem valores absolutos e percentuais.
- Cenário de receita zero testado sem `NaN`.
- Cinco filtros testados isoladamente e em combinação com lógica AND.
- Query string restaurada após recarregar.
- Estado vazio, exportação desabilitada e recuperação com Limpar filtros testados.
- Estado de erro forçado por falha no parsing do JSON.
- CSV baixado com cabeçalho e 100 linhas no recorte completo.
- Select, Limpar filtros e Exportar CSV operados por teclado.
- Hover, foco visível e movimento reduzido verificados.
- Console e runtime sem erros.

## Responsividade

| Largura | Overflow horizontal | Alvos menores que 44px |
|---:|---|---:|
| 1440px | não | não |
| 1024px | não | não |
| 768px | não | não |
| 375px | não | não |

A tabela vira uma lista rotulada em telas estreitas, sem rolagem horizontal da página.

## Acessibilidade

- axe-core com regras WCAG 2.0, 2.1 e 2.2 A/AA: zero violações.
- Contraste mínimo verificado: 6,19:1 para texto normal.
- Vermelho sobre off-white: 5,12:1. Vermelho escuro sobre off-white: 6,98:1.
- Texto claro sobre preto: 12,88:1 ou mais.
- Todos os controles possuem rótulo visível, nome acessível e foco de 3px.
- Gráficos têm listas rotuladas e valores textuais, não dependem só de cor.
- `prefers-reduced-motion` reduz transições a 0,01ms.

## Limitações

- Não houve teste em leitor de tela real ou dispositivo físico.
- As fontes Barlow Condensed e Source Sans 3 vêm do Google Fonts. Fallbacks locais mantêm a função, mas a identidade tipográfica pode mudar offline.
- As capturas são de viewport, não full-page. A tabela e o rodapé foram avaliados por código e pelos testes de interação.

## Impeccable

- Detector mecânico: nenhum erro. Um aviso `cream-palette` foi mantido como override explícito da direção Motorsport premium escolhida pelo usuário.
- Dials: ENERGY 2 / RHYTHM 2 / MOTION 1.
- Revisão independente: pendente.

## Publicação

Pendente.

## Delivery Gate antislop

- R-02 PASS: nenhum em dash ou en dash nos textos do projeto.
- R-03 PASS: 1440, 1024, 768 e 375px sem overflow; alvos de toque de pelo menos 44px.
- R-17 PASS: todos os números vêm do JSON sanitizado e da fonte registrada.
- R-18 PASS: nenhum depoimento, cliente ou avaliado fictício.
- R-23 PASS: nenhum logo, avatar ou ilustração foi inventado; as capturas são evidência solicitada.
- R-24 PASS: o único link interno leva a `#filters`, que existe.
- R-25 PASS: contraste mínimo de 6,19:1 para texto normal.
- R-26 PASS: filtros, limpeza, exportação, recarga e link de atalho têm comportamento real.
- R-27 PASS: loading, vazio e erro presentes; vazio e erro testados.
- R-28 PASS: não há FAQ.
- R-32 PASS: teclado, ordem de foco e indicador de 3px testados.
- R-33 PASS: nenhum recurso foi implementado por script que reescreve HTML ou CSS.
- R-34 PASS: não há alternância de tema.
- R-35 PASS: aplicação executada e 87 interações e estados verificados; publicação ao vivo ainda pendente.
- R-36 PASS: nenhuma métrica de performance, segurança ou conformidade foi inventada.
- R-37 PASS: direção Motorsport premium confirmada antes da implementação.
- R-38 PASS: conteúdo e números reais, sem placeholders fantasiados.
- R-39 PASS: semântica, rótulos, foco, cursor, motion e landmarks validados.
- R-40 PASS: sem mídia no HTML e sem scripts de terceiros; nenhum número de performance reportado.
- R-01 PASS: sem gradientes ou glows.
- R-04 PASS: sem ícones genéricos.
- R-06 PASS: Barlow Condensed e Source Sans 3 com funções de hierarquia documentadas.
- R-07 PASS: sem textura de fundo decorativa.
- R-08 PASS: sem setas decorativas em botões.
- R-09 PASS: sem badges decorativos; contadores são informação funcional.
- R-10 PASS: sem glassmorphism.
- R-12 PASS: sem sombras.
- R-13 PASS: sem glow.
- R-14 PASS: KPIs têm hierarquia; receita é dominante.
- R-19 PASS: movimento apenas em interação e desligado com preferência reduzida.
- R-22 PASS: sem ilustrações genéricas.
- Liveliness PASS: dials explícitos, receita como foco, contraste hierárquico, espaço estrutural, vermelho controlado e régua numérica como motivo.
- C-1 PASS: decisões documentadas no README e no surface brief.
- C-2 PASS: controles funcionais verificados.
- C-3 PASS: layout segue filtros, KPIs, perguntas e auditoria.
- C-4 PASS: estados, teclado e larguras verificados.
- C-5 PASS: fonte, capturas e resultados de teste registrados.
- R-05 PASS: composição de dashboard específica, sem shell genérico de sidebar.
- R-11 PASS: raio pequeno e consistente com a linguagem técnica.
- R-15 PASS: ações específicas: Limpar filtros, Exportar CSV e Recarregar página.
- R-16 PASS: sem buzzwords.
- R-20 PASS: paleta, tipografia e motivo visual próprios.
- R-21 PASS: tema claro fixo pela direção escolhida para o contexto de leitura.
- R-29 PASS: neutros, preto e vermelho dentro do sistema.
- R-30 PASS: nenhum produto conhecido foi clonado.
- R-31 PASS: razões das decisões registradas no README.
