## Criando a imagem com valor da variavel padrao
sudo docker image build -t ex-build-copy .

## Visualizando a imagem
sudo docker image ls

## Executando o container desta imagem 
sudo docker container run ex-build-copy -p 80:80
