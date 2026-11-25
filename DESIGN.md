---
name: "Porsche Vendas Dashboard"
description: "Painel auditável de vendas com precisão automotiva."
colors:
  paddock-paper: "#f2efe6"
  panel-surface: "#fbf9f3"
  carbon-ink: "#171715"
  secondary-ink: "#5a5852"
  hairline: "#c9c4b9"
  chart-track: "#e4dfd5"
  signal-red: "#c8102e"
  signal-red-deep: "#a20c25"
  carbon-black: "#151513"
  warm-white: "#fffdf7"
typography:
  display:
    fontFamily: "\"Barlow Condensed\", \"Arial Narrow\", \"Liberation Sans Narrow\", sans-serif"
    fontSize: "clamp(2.8rem, 5vw, 4.6rem)"
    fontWeight: 600
    lineHeight: 0.92
    letterSpacing: "-0.025em"
  headline:
    fontFamily: "\"Barlow Condensed\", \"Arial Narrow\", \"Liberation Sans Narrow\", sans-serif"
    fontSize: "clamp(1.65rem, 2.5vw, 2.2rem)"
    fontWeight: 600
    lineHeight: 1.05
    letterSpacing: "-0.015em"
  title:
    fontFamily: "\"Barlow Condensed\", \"Arial Narrow\", \"Liberation Sans Narrow\", sans-serif"
    fontSize: "2rem"
    fontWeight: 600
    lineHeight: 1.05
  metric-revenue:
    fontFamily: "\"Barlow Condensed\", \"Arial Narrow\", \"Liberation Sans Narrow\", sans-serif"
    fontSize: "clamp(3.1rem, 6vw, 5.8rem)"
    fontWeight: 600
    lineHeight: 0.95
    letterSpacing: "-0.02em"
  metric-secondary:
    fontFamily: "\"Barlow Condensed\", \"Arial Narrow\", \"Liberation Sans Narrow\", sans-serif"
    fontSize: "clamp(1.8rem, 3vw, 2.6rem)"
    fontWeight: 600
    lineHeight: 0.95
    letterSpacing: "-0.02em"
  metric-leader:
    fontFamily: "\"Barlow Condensed\", \"Arial Narrow\", \"Liberation Sans Narrow\", sans-serif"
    fontSize: "clamp(1.55rem, 2.5vw, 2.15rem)"
    fontWeight: 600
    lineHeight: 1
  body:
    fontFamily: "\"Source Sans 3\", \"Segoe UI\", Arial, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "\"Source Sans 3\", \"Segoe UI\", Arial, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 700
    lineHeight: 1.5
    letterSpacing: "0.04em"
  wordmark:
    fontFamily: "\"Barlow Condensed\", \"Arial Narrow\", \"Liberation Sans Narrow\", sans-serif"
    fontSize: "1.05rem"
    fontWeight: 700
    lineHeight: 1
    letterSpacing: "0.08em"
rounded:
  surface: "3px"
  control: "2px"
  track: "1px"
spacing:
  field-label: "6px"
  compact: "8px"
  control: "10px"
  field: "12px"
  grid: "14px"
  base: "16px"
  rhythm: "18px"
  heading: "20px"
  section: "24px"
  panel: "28px"
  header: "32px"
  state: "40px"
  touch: "44px"
  gutter: "clamp(16px, 4vw, 48px)"
  page-bottom: "64px"
components:
  button-primary:
    backgroundColor: "{colors.carbon-ink}"
    textColor: "{colors.warm-white}"
    rounded: "{rounded.control}"
    padding: "10px 16px"
    height: "44px"
  button-primary-hover:
    backgroundColor: "{colors.signal-red}"
    textColor: "{colors.warm-white}"
    rounded: "{rounded.control}"
    padding: "10px 16px"
    height: "44px"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.carbon-ink}"
    rounded: "{rounded.control}"
    padding: "10px 16px"
    height: "44px"
  button-secondary-hover:
    backgroundColor: "#e9e4da"
    textColor: "{colors.carbon-ink}"
    rounded: "{rounded.control}"
    padding: "10px 16px"
    height: "44px"
  field-select:
    backgroundColor: "{colors.warm-white}"
    textColor: "{colors.carbon-ink}"
    rounded: "{rounded.control}"
    padding: "9px 30px 9px 10px"
    height: "44px"
  panel:
    backgroundColor: "{colors.panel-surface}"
    textColor: "{colors.carbon-ink}"
    rounded: "{rounded.surface}"
    padding: "28px"
  kpi-revenue:
    backgroundColor: "{colors.carbon-black}"
    textColor: "{colors.warm-white}"
    rounded: "{rounded.surface}"
    padding: "22px 24px"
    typography: "{typography.metric-revenue}"
  audit-table-header:
    textColor: "{colors.secondary-ink}"
    typography: "{typography.label}"
---

# Design System: Porsche Vendas Dashboard

## Overview

**Creative North Star: "Motorsport premium"**

A dashboard trata a base como um painel de análise de concessionária, não como uma landing page. O clima é preciso, contido e automotivo: receita, volume e ticket médio aparecem antes dos gráficos, e cada visual responde a uma pergunta de negócio. A identidade textual mantém o projeto independente e auditável, sem apresentar a dashboard como um canal oficial da marca.

A força visual vem da hierarquia, da régua vermelha e do alinhamento comum, não de ornamentos. Off-white de paddock e preto carbono formam a estrutura; vermelho sinal marca dado dominante, estado e interação. Superfícies planas, bordas finas e raios pequenos preservam a leitura densa. O movimento se limita a respostas de interação, e a tabela filtrada permite reproduzir qualquer recorte.

**Key Characteristics:**
- Receita bruta é a primeira e dominante métrica.
- Paleta off-white de paddock, preto carbono e vermelho sinal.
- Barlow Condensed nos títulos; Source Sans 3 na leitura e nos dados.
- Superfícies planas, bordas finas e raios pequenos.
- Filtros nativos e tabela auditável no mesmo recorte.
- Movimento apenas de interação; layout responsivo em 1440/1024/768/375.

## Colors

A paleta é quente, técnica e econômica: neutros de papel e carbono sustentam a informação, enquanto o vermelho atua como sinal.

### Primary

- **Vermelho Sinal** (`signal-red`): preenchimento de barras de receita, régua numérica, linha inferior da receita, seleção de texto, foco e hover do botão primário. É cor de ênfase e interação, não fundo geral.
- **Vermelho Sinal Profundo** (`signal-red-deep`): textos pequenos de destaque sobre superfícies claras, como rankings, contagens, avisos de qualidade e datas inválidas.

### Neutral

- **Off-white Paddock** (`paddock-paper`): canvas da página e base da hierarquia clara.
- **Superfície de Painel** (`panel-surface`): fundo de filtros, painéis analíticos e tabela.
- **Tinta Carbono** (`carbon-ink`): texto principal, botão primário, cabeçalhos de tabela e barras de quantidade.
- **Preto Carbono** (`carbon-black`): banda de indicadores e rodapé, com texto claro.
- **Branco Quente** (`warm-white`): texto sobre carbono e fundo dos selects nativos.
- **Texto Secundário** (`secondary-ink`): descrições, notas, rótulos e metadados.
- **Linha Fina** (`hairline`): bordas de painéis, divisórias de linhas e trilhos discretos.
- **Trilha de Gráfico** (`chart-track`): fundo das barras, preservando a leitura da proporção.

### Named Rules

**The Signal Rule.** Vermelho sinal marca prioridade, dado ou interação; vermelho sinal profundo assume textos pequenos sobre fundos claros. Não transformar o acento em campo decorativo.

**The Cream Override Rule.** A paleta cream/off-white é override explícito do usuário. O warning `cream-palette` não é defeito e não autoriza substituí-la por branco puro ou por um tema escuro global.

## Typography

**Display Font:** Barlow Condensed, with Arial Narrow, Liberation Sans Narrow, sans-serif fallbacks.
**Body Font:** Source Sans 3, with Segoe UI, Arial, sans-serif fallbacks.

**Character:** Títulos condensados dão presença automotiva sem volume excessivo; a sans de leitura mantém dados, explicações e tabela legíveis. Números usam tabular figures para alinhar valores.

### Dependency and Fallbacks

Barlow Condensed e Source Sans 3 são carregadas do Google Fonts com `preconnect` e `display=swap`. A dependência de rede está registrada: sem conexão, as pilhas locais do sistema assumem a renderização, e o conteúdo permanece utilizável.

### Hierarchy

- **Display** (600, `clamp(2.8rem, 5vw, 4.6rem)`, line-height 0.92, letter-spacing -0.025em, uppercase): título principal da dashboard.
- **Headline** (600, `clamp(1.65rem, 2.5vw, 2.2rem)`, line-height 1.05, letter-spacing -0.015em): perguntas e títulos de seção.
- **Title** (600, 2rem, line-height 1.05): títulos dos estados de carregamento e erro.
- **Metric Revenue** (600, `clamp(3.1rem, 6vw, 5.8rem)`, line-height 0.95, letter-spacing -0.02em): receita bruta, dominante na banda de indicadores.
- **Metric Secondary** (600, `clamp(1.8rem, 3vw, 2.6rem)`, line-height 0.95, letter-spacing -0.02em): vendas e ticket médio.
- **Metric Leader** (600, `clamp(1.55rem, 2.5vw, 2.15rem)`, line-height 1): nome do modelo líder.
- **Body** (400, 16px, line-height 1.5): leitura, descrições, controles e células da tabela.
- **Label** (700, 0.75rem, letter-spacing 0.04em, uppercase): cabeçalhos de tabela e rótulos técnicos.
- **Wordmark** (700, 1.05rem, line-height 1, letter-spacing 0.08em, uppercase): identidade textual compacta do cabeçalho.

### Named Rules

**The Two Voices Rule.** Barlow Condensed conduz títulos e métricas; Source Sans 3 conduz leitura e dados. Não usar a condensada em parágrafos nem substituir a dupla por uma única família.

**The Numeric Alignment Rule.** Valores monetários, contagens e percentuais usam tabular figures; colunas numéricas da tabela alinham à direita.

## Layout

O conteúdo usa uma régua comum de até 1440px, com gutters fluidos `clamp(16px, 4vw, 48px)`. `main` e `#dashboard` são grids com gap de 24px; abaixo de 560px, o gap cai para 18px. Painéis e filtros usam padding de 28px, reduzido para 18px no compacto; estados dedicados usam 40px, reduzidos para 24px.

Os cinco filtros nativos ocupam cinco colunas iguais, passam a três colunas em 1100px, duas em 760px e uma em 560px. A banda de KPIs começa em `1.8fr 0.8fr 0.9fr 1.1fr`; em 1100px, o modelo líder ocupa a linha seguinte; em 760px, a receita ocupa a linha inteira e os demais ficam em duas colunas; em 560px, todos empilham. A seção dupla usa `1.15fr 0.85fr` e empilha em 960px.

Os viewports de referência são 1440, 1024, 768 e 375px. Em 1024px, filtros usam três colunas e a seção dupla permane lado a lado; em 768px, filtros usam duas colunas, a seção dupla já está empilhada e a tabela vira lista rotulada; em 375px, filtros, ações e KPIs ficam em uma coluna, sem overflow horizontal.

### Named Rules

**The Revenue-First Rule.** A receita bruta abre a banda de indicadores, recebe a maior escala tipográfica e a única régua vermelha inferior. Vendas, ticket médio e modelo líder permanecem subordinados.

**The Native Filter Rule.** Os filtros são selects nativos com rótulos visíveis e altura mínima de 44px. Não substituí-los por menus decorativos ou chips de aparência customizada.

## Elevation & Depth

O sistema não usa sombras, gradientes ou elevação projetada. Profundidade vem do contraste tonal entre paper, surface e carbono, além de bordas de 1px. Foco é um outline vermelho de 3px com offset de 3px; hover altera cor ou fundo, e active desloca o botão 1px para baixo, sem levantar a superfície.

### Named Rules

**The Flat Surface Rule.** Painéis e controles são planos em repouso. Não introduzir sombras, glassmorphism ou profundidade decorativa para separar conteúdo.

## Shapes

A forma é retilínea e precisa: painéis, filtros e banda de KPIs usam raio de 3px; botões e selects usam 2px; trilhos de barras usam 1px. Bordas finas e divisórias horizontais organizam a densidade. Não há cards circulares, pílulas ou recortes que imitem um cockpit.

### Named Rules

**The Small Radius Rule.** Manter 3px para superfícies, 2px para controles e 1px para trilhos. O raio existe para suavizar a aresta técnica, não para criar uma linguagem arredondada.

## Components

### Buttons

- **Character:** compactos, diretos e operáveis por toque.
- **Shape:** raio de 2px, altura mínima de 44px, padding de 10px 16px, peso 600 e line-height 1.2.
- **Primary:** fundo carbono, texto branco quente e borda carbono; hover troca fundo e borda para vermelho sinal.
- **Secondary:** fundo transparente, texto carbono e borda carbono; hover usa o cinza quente `#e9e4da`.
- **States:** foco global vermelho de 3px com offset de 3px; active desloca 1px para baixo; disabled usa opacidade 0.45. Transições de cor e transform levam 160ms `ease-out`.

### Inputs / Fields

- **Style:** select nativo em fundo branco quente, texto carbono, borda `#8f8b82`, raio de 2px, padding de 9px 30px 9px 10px e altura mínima de 44px.
- **Label:** visível acima do campo, 0.86rem, peso 600 e gap de 6px.
- **Hover / Focus:** hover escurece a borda para carbono e usa `#fffefa`; foco mantém o outline global vermelho. A seta e o menu continuam nativos.

### Cards / Containers

- **Corner Style:** raio de 3px.
- **Background:** superfície de painel.
- **Shadow Strategy:** nenhuma sombra; ver Elevation & Depth.
- **Border:** 1px na cor de linha fina.
- **Internal Padding:** 28px, reduzido para 18px abaixo de 560px.

### Navigation

Não há navegação tradicional de seções. O cabeçalho é uma identidade textual compacta com escopo da base, separado por borda inferior de 1px. O skip link é o único atalho de navegação: aparece ao foco, usa fundo carbono e texto branco quente, com translação de 160ms `ease-out`.

### Revenue KPI Band

A banda usa fundo preto carbono, texto branco quente, borda de 1px e raio de 3px. Cada KPI tem padding de 22px 24px e divisórias `#45443f`. A receita recebe a régua vermelha de 3px na base; rótulos usam `#ddd8ce`, uppercase e letter-spacing de 0.06em. A hierarquia responsiva preserva a receita dominante em todos os tamanhos.

### Analytical Rankings

Famílias usam barras de receita de 14px com trilho `chart-track` e preenchimento vermelho; estados usam uma barra fina de 4px; pagamentos usam mini barras de 6px, vermelho para receita e carbono para quantidade. A régua numérica vermelha, os ranks e os insights ancoram a leitura. Barras mudam de largura em 220ms com `cubic-bezier(0.16, 1, 0.3, 1)`, apenas quando o recorte muda.

### Data Quality and Audit Table

O aviso de qualidade usa fundo `#eee9df`, borda fina, padding de 12px 14px e texto 0.88rem; o trecho forte usa vermelho sinal profundo. A tabela é o fechamento auditável da página: cabeçalhos uppercase com borda inferior de 2px, células com borda inferior de 1px, valores tabulares e hover `#f1ece3`. Datas inválidas recebem vermelho profundo, peso 600 e sublinhado pontilhado. Abaixo de 760px, cada registro vira uma lista rotulada por `data-label`, sem overflow horizontal.

### Named Rules

**The One Recorte Rule.** Filtros, indicadores, gráficos e tabela representam o mesmo conjunto de registros. Nenhum visual pode contar uma história diferente da tabela auditável.

**The Interaction-Only Motion Rule.** Movimento ocorre em hover, foco, active ou atualização de barras. Não adicionar animações ambientes, autoplay ou transições de entrada; `prefers-reduced-motion` reduz durações a 0.01ms e desativa rolagem suave.

## Do's and Don'ts

### Do:

- **Do** manter a receita bruta como primeira e dominante métrica, com a régua vermelha inferior.
- **Do** usar superfícies planas, bordas de 1px e raios de 3px, 2px ou 1px conforme o componente.
- **Do** preservar selects nativos, rótulos visíveis e altura mínima de 44px.
- **Do** registrar a dependência de Google Fonts e manter os fallbacks locais de Barlow Condensed e Source Sans 3.
- **Do** usar tabular figures e alinhar valores numéricos à direita na tabela.
- **Do** manter filtros, gráficos e tabela no mesmo recorte, com a tabela acessível como evidência final.
- **Do** verificar 1440/1024/768/375 e empilhar controles e KPIs abaixo de 560px sem overflow horizontal.

### Don't:

- **Don't** adicionar sombras, gradientes, vidro ou elevação decorativa.
- **Don't** transformar vermelho sinal em fundo geral ou usar o tom puro para textos pequenos sobre off-white.
- **Don't** substituir a paleta cream/off-white por causa do warning `cream-palette`; ela é override explícito do usuário.
- **Don't** adicionar movimento ambiente, autoplay ou animações de entrada.
- **Don't** esconder a tabela auditável atrás de abas ou substituí-la por uma lista sem os rótulos dos campos.
- **Don't** imitar um cockpit, criar cards decorativos ou apresentar a dashboard como canal oficial da Porsche.
