# Detecção de Rachaduras usando YOLO



https://github.com/brunomleao/EntregaYoloBackend/assets/99328889/b825386b-f575-4d72-90fd-5e9812e99d84


Este projeto consiste em um sistema de detecção de rachaduras em tempo real utilizando o algoritmo YOLO (You Only Look Once). Além disso, há uma integração com um servidor local para salvar as imagens detectadas.

Pré-requisitos
Certifique-se de ter os seguintes requisitos instalados em seu ambiente:

- Python 3.x
- OpenCV (cv2)
- Ultralytics
- Requests
- base64

# Servidor
O servidor local é implementado em Node.js usando o framework Express. O servidor recebe as imagens detectadas em tempo real e as armazena em um diretório específico.

# Utilização
1. Inicie o servidor:
```
npm start
```
O servidor será iniciado na porta 3000 e você verá a mensagem "Servidor iniciado na porta 3000" no console.

2. Execute o script Python para iniciar o sistema de detecção de rachaduras em tempo real. Certifique-se de que a câmera esteja conectada e acessível:
```
python3 main.py
```
O sistema começará a capturar o vídeo da câmera e realizar a detecção de rachaduras. Se algum objeto for detectado, a imagem será enviada ao servidor local para armazenamento.

# Resultados

As imagens contendo as rachaduras detectadas serão salvas no diretório "./imagens/" no servidor local. Cada imagem será nomeada com o prefixo "imagem_" seguido de um timestamp.

Você também pode acessar as imagens salvas através da rota GET "/image-mostrar/:nomeArquivo" no servidor local, fornecendo o nome do arquivo desejado como parâmetro. O servidor retornará a imagem correspondente com o tipo de conteúdo definido como image/jpeg.

# Funcionamento do código

No script Python, a câmera é inicializada e o modelo YOLO é carregado. Em seguida, é iniciado um loop de captura de frames do vídeo. A detecção de rachaduras é aplicada em cada frame e, se rachaduras forem detectadas, a imagem é codificada em formato JPEG e enviada para o servidor local através de uma requisição POST.

O servidor em Node.js recebe as imagens enviadas pelo script Python e as salva em um diretório específico. Quando uma requisição POST é recebida, o servidor converte a imagem codificada em base64 em um buffer, carrega-a e a salva no diretório definido. O servidor também possui uma rota GET que permite visualizar as imagens salvas.
