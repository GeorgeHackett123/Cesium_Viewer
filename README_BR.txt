Cesium + Marzipano Visualizador 360 Automatizado
===============================================

Este projeto automatiza a criação de um visualizador de imagens 360° com CesiumJS + Marzipano para novos pontos de câmera, sobreposições (GeoJSON) e imagens.

-------------------------------------------------------------------------------

ESTRUTURA DE PASTAS

sua-pasta-do-projeto/
├── build_cesium_index.py        # Script de automação (execute este)
├── index_template.html          # Template HTML com marcadores de posição
├── camera_points_final.geojson  # GeoJSON principal dos pontos de câmera (pode ser renomeado)
├── layer_0.geojson              # Arquivo(s) GeoJSON de sobreposição (detectados automaticamente)
├── layer_C-TOPO-MAJR.geojson
├── ... mais arquivos layer_*.geojson ...
├── images/                      # Pasta com todas as imagens 360
│    ├── IMG_0001.JPG
│    ├── IMG_0002.JPG
│    └── ...
└── index.html                   # Saída gerada (visualizador)

-------------------------------------------------------------------------------

COMO USAR

1. Prepare seus dados:
   - Coloque seu arquivo GeoJSON principal dos pontos de câmera na pasta (padrão: camera_points_final.geojson).
     - O nome do arquivo é definido em build_cesium_index.py (CAMERA_POINTS_GEOJSON).
     - Cada feature precisa ter a propriedade #Label correspondente ao nome da imagem e o valor Yaw_est.
   - Coloque todos os arquivos GeoJSON de sobreposição/annotation (padrão layer_*.geojson) na pasta.
   - Coloque todas as imagens 360 na pasta images/.
     - Os nomes dos arquivos devem corresponder ao valor do campo #Label no GeoJSON dos pontos de câmera.

2. Atualize as configurações (se necessário):
   - Se seu arquivo GeoJSON principal tiver outro nome, altere o valor CAMERA_POINTS_GEOJSON no build_cesium_index.py.
   - Adicione/edite nomes de sobreposições ou cores personalizadas no dicionário CUSTOM_COLORS do script.
   - Cole seu token Cesium Ion na variável CESIUM_ION_TOKEN.

3. Gere seu visualizador:
   - No terminal/prompt de comando dentro da pasta, execute:
     python build_cesium_index.py
   - Isso irá:
     - Detectar os arquivos GeoJSON de sobreposição,
     - Preencher o template,
     - Gerar o arquivo index.html completo.

4. Visualize seu site:
   - Abra o index.html no navegador (ou faça upload do conteúdo para seu servidor web/GitHub Pages).

-------------------------------------------------------------------------------

ATUALIZANDO COM NOVOS DADOS

1. Substitua ou adicione seu novo camera_points_final.geojson e/ou arquivos de sobreposição.
2. Coloque novas imagens 360 na pasta images/ (garanta que os nomes correspondam ao #Label).
3. Execute novamente:
   python build_cesium_index.py
4. Faça upload ou publique conforme necessário.

-------------------------------------------------------------------------------

SOLUÇÃO DE PROBLEMAS

- Imagens ausentes:
    Verifique se cada #Label do GeoJSON de pontos de câmera tem uma imagem correspondente na pasta images/.

- Novos arquivos de sobreposição:
    GeoJSONs de sobreposição com padrão layer_*.geojson são detectados automaticamente. Basta adicionar novos arquivos conforme necessário.

- Cores personalizadas:
    Edite o dicionário CUSTOM_COLORS no script para definir cores específicas para novas sobreposições.

-------------------------------------------------------------------------------

AVANÇADO

- Você pode mudar o padrão dos arquivos GeoJSON de sobreposição ou adicionar mais lógica/configuração no build_cesium_index.py.
- Para grandes volumes de dados, considere automatizar a criação dos pontos de câmera e imagens com seus próprios scripts.

-------------------------------------------------------------------------------

REQUISITOS

- Python 3.x
- Conta/token do Cesium Ion (https://cesium.com/ion/)

-------------------------------------------------------------------------------

CONTATO

Para melhorias ou suporte, consulte o responsável do projeto ou use o ChatGPT da OpenAI para ajustes no script!
