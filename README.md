# GeoFinder - Análise de Profundidade Geográfica com Visualização 3D

Descrição do Projeto:

Neste projeto, desenvolvi uma ferramenta de análise geográfica que lê dados de profundidade de um arquivo, calcula a distância entre coordenadas geográficas, determina a posição mais próxima a um ponto de interesse e visualiza os resultados em um gráfico 3D de contorno.

Funcionalidades e Metodologia:

Leitura de Dados:

Utilizei Python para ler e processar dados de um arquivo de texto contendo coordenadas de latitude, longitude e profundidade.

Os dados são organizados e os limites geográficos são determinados para posterior análise.

Cálculo de Distâncias:

Implementei a fórmula de Haversine para calcular a distância entre dois pontos na superfície terrestre.

Isso permite encontrar a posição mais próxima de um ponto fornecido pelo usuário.

Determinação da Posição Mais Próxima:

A ferramenta compara o ponto de interesse fornecido pelo usuário com todos os pontos do conjunto de dados para identificar a posição mais próxima e sua profundidade associada.

Visualização com Gráfico 3D:

Utilizei as bibliotecas Matplotlib e NumPy para criar uma visualização 3D das profundidades.

A interpolação de dados é realizada para gerar um gráfico de contorno suave, permitindo uma melhor visualização das variações de profundidade.

O gráfico 3D é interativo, permitindo uma análise mais detalhada dos dados geográficos.

Aplicações Práticas: Esta ferramenta pode ser aplicada em várias áreas, como estudos ambientais, planejamento urbano, pesquisas oceanográficas e qualquer cenário onde a análise de profundidade geográfica seja necessária. A visualização em 3D facilita a compreensão das variações topográficas e pode apoiar a tomada de decisões informadas.

Conclusão: Este projeto demonstra uma integração eficiente de processamento de dados geográficos e visualização avançada, proporcionando uma ferramenta robusta para análise e interpretação de dados de profundidade.