Spotify Trends Analytics
Análise exploratória de tendências musicais no Spotify utilizando Python, análise de dados e visualização interativa.

📌Sobre o projeto

Este projeto foi desenvolvido como atividade acadêmica de Big Data no curso de Ciência da Computação. O objetivo é explorar características das músicas e observar como alguns indicadores musicais variaram ao longo das décadas.

🎯Objetivos

* Analisar tendências de popularidade das músicas.
* Comparar níveis de energia e dançabilidade.
* Investigar mudanças na duração das músicas.
* Observar a proporção de músicas com conteúdo explícito.
* Apresentar os resultados por meio de gráficos e indicadores visuais.

🗂️Dados utilizados

O projeto utiliza uma base de dados de músicas do Spotify, complementada por informações de ano de lançamento obtidas em uma segunda base pública.

A base principal continha originalmente 114.000 registros. Após a limpeza e o tratamento dos dados, foram mantidos 113.549 registros.

As etapas de preparação incluíram:

* Verificação de valores ausentes.
* Remoção de registros sem informações essenciais.
* Identificação e tratamento de repetições de identificadores de músicas dentro dos gêneros.
* Preparação dos dados para as análises e visualizações.

Limitação: o ano de lançamento está disponível apenas para parte das músicas. Por isso, as análises históricas consideram somente os registros com ano identificado. Os resultados também devem ser interpretados considerando a quantidade de dados disponível em cada década.

🛠️Tecnologias utilizadas

* Python
* Pandas
* Google Colab
* Streamlit
* Plotly
* GitHub

📊Análises realizadas

1. Popularidade média das músicas por década.
2. Evolução da energia musical.
3. Variação da dançabilidade.
4. Mudanças na duração média das músicas.
5. Proporção de músicas com conteúdo explícito.

📈Principais resultados

Entre os registros com ano de lançamento identificado, foram observados os seguintes padrões:

* A popularidade média foi de 51,61 nos anos 2000, 59,25 nos anos 2010 e 64,12 nos anos 2020.
* A energia média foi maior nos anos 2000 do que nas décadas mais antigas analisadas.
* A dançabilidade média aumentou de 0,538 nos anos 2000 para 0,649 nos anos 2020.
* A duração média das músicas diminuiu de aproximadamente 4,28 minutos nos anos 1990 para 3,41 minutos nos anos 2020.
* A proporção de músicas com conteúdo explícito aumentou nas décadas mais recentes.

Os resultados representam os dados disponíveis no projeto, não necessariamente toda a produção musical de cada década. A popularidade corresponde ao indicador presente na base e não à popularidade histórica da música no momento de seu lançamento.

📱Dashboard interativo

O dashboard permite explorar os dados por meio de gráficos e indicadores.

Acessar o Spotify Trends Analytics

📁Arquivos do repositório

* Spotify_Trends_Analytics.ipynb: notebook com o desenvolvimento e as análises.
* app.py: código do dashboard interativo.
* requirements.txt: bibliotecas necessárias para executar o aplicativo.
* spotify_dashboard.csv: dados utilizados pelo dashboard.
* README.md: documentação do projeto.

▶️Como executar o dashboard localmente

1. Instale o Python.
2. Instale as dependências:

pip install -r requirements.txt

3. Execute o aplicativo:

streamlit run app.py

📚Fontes de dados

* Base principal de músicas do Spotify — Hugging Face
* Base complementar de músicas e datas de lançamento — Hugging Face

👩‍💻Autoria

Projeto acadêmico desenvolvido para a disciplina de Big Data do curso de Ciência da Computação.
