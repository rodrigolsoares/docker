## Criando a imagem com valor da variavel padrao
sudo docker image build -t ex-build-arg .

## Criando a imagem alterando o valor da variavel padrao
sudo docker run ex-build-arg bash -c 'echo $S3_BUCKET'

## Visualizando a imagem
sudo docker image ls

## executando o container desta imagem 
sudo docker run ex-build-arg bash -c 'echo $S3_BUCKET'
