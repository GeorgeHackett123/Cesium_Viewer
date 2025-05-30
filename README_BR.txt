Visualizador Automatizado 360 Cesium + Marzipano

Este projeto automatiza a criação de um visualizador de imagens 360° usando CesiumJS + Marzipano para novos pontos de câmera, overlays e imagens.

------------------------------------------------------------------------------

ESTRUTURA DE PASTAS

sua-pasta-do-projeto/
├── build_cesium_index.py        # Script de automação (execute este)
├── index_template.html          # Template HTML com espaços reservados
├── camera_points_final.geojson  # GeoJSON principal dos pontos de câmera (pode ser renomeado)
├── layer_0.geojson              # GeoJSON(s) de overlay (detectados automaticamente)
├── layer_C-TOPO-MAJR.geojson
├── ... mais arquivos layer_*.geojson ...
├── images/                      # Pasta com todas as imagens 360
│    ├── IMG_0001.JPG
│    ├── IMG_0002.JPG
│    └── ...
└── index.html                   # Saída gerada (visualizador)

------------------------------------------------------------------------------

COMO USAR

1. Prepare seus dados:
   - Coloque seu arquivo GeoJSON principal dos pontos de câmera na pasta (padrão: camera_points_final.geojson).
     - O nome do arquivo é definido em build_cesium_index.py (CAMERA_POINTS_GEOJSON).
     - Cada feature deve ter uma propriedade #Label igual ao nome do arquivo da imagem e um valor Yaw_est.
   - Coloque todos os arquivos GeoJSON de overlay/anotação (com padrão layer_*.geojson) na pasta.
   - Copie a pasta 'images' da pasta '2 - Image_EXIF'.
     - Os nomes dos arquivos devem ser iguais ao valor #Label no GeoJSON dos pontos de câmera, incluindo a extensão .jpg.

2. Atualize a configuração (se necessário):
   - Se o seu GeoJSON dos pontos de câmera tiver outro nome, atualize a variável CAMERA_POINTS_GEOJSON no build_cesium_index.py.
   - Adicione/alterne nomes de overlays ou cores personalizadas de overlays no dicionário CUSTOM_COLORS do script.
   - Cole seu token Cesium Ion na variável CESIUM_ION_TOKEN.

3. Gere seu visualizador:
   - No terminal/Prompt de Comando na pasta, execute:
     python build_cesium_index.py
   - Isso irá:
     - Escanear seus arquivos GeoJSON de overlay,
     - Preencher o template,
     - Gerar um arquivo index.html completo do visualizador.

4. Crie o repositório GitHub online
   - Clone o repositório no GitHub Desktop.
   - Abra a pasta do repositório no Explorer ('Mostrar no Explorer' ou 'Ctrl + Shift + F').
   - Copie todo o conteúdo desta pasta para a pasta do repositório.
   - Faça push (envie) para o repositório online no GitHub.
   - Gere a página web.

5. Acesse seu site

------------------------------------------------------------------------------

ATUALIZAÇÃO COM NOVOS DADOS

1. Substitua ou adicione seu novo camera_points_final.geojson e/ou overlays.
2. Coloque as novas imagens 360 na pasta images/ (certifique-se que os nomes estão corretos).
3. Execute novamente:
   python build_cesium_index.py
4. Faça upload/publicação conforme necessário.

------------------------------------------------------------------------------

RESOLUÇÃO DE PROBLEMAS

- Imagens ausentes:  
    Certifique-se que cada #Label no GeoJSON dos pontos de câmera tenha uma imagem correspondente na pasta images/.

- Novos arquivos de overlay:  
    GeoJSONs de overlay com o padrão layer_*.geojson são detectados automaticamente. Adicione novos conforme necessário.

- Cores personalizadas:  
    Atualize o dicionário CUSTOM_COLORS no script se quiser que overlays tenham cores específicas.

------------------------------------------------------------------------------

AVANÇADO

- Você pode mudar o padrão dos arquivos GeoJSON de overlay ou adicionar mais lógica de configuração no build_cesium_index.py.
- Para grandes conjuntos de dados, considere automatizar a criação dos pontos de câmera e imagens com seus próprios scripts.

------------------------------------------------------------------------------

REQUISITOS

- Python 3.x
- Conta/token Cesium Ion (https://cesium.com/ion/)

------------------------------------------------------------------------------

CONTATO

Para melhorias ou suporte, peça ao administrador do projeto ou ao ChatGPT da OpenAI para ajustes no script!
