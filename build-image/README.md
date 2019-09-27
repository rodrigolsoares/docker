## Criando a imagem
sudo docker image build -t ex-build .

## Visualizando a imagem
sudo docker image ls

## executando o container desta imagem
sudo docker container run -p 80:80 ex-build
