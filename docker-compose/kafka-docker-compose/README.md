# Comandos Kafka com Zookepper 

## Subindo em background o ambiente
sudo docker-compose up -d

## Finalizando o ambiente
sudo docker-compose down

## Verificando os containers
sudo docker-compose ps

## Verificando o zookeeper
sudo docker-compose logs zookeeper | grep -i binding

### Deve mostrar algo assim
#zookeeper_1  | [2018-06-26 01:06:59,447] INFO binding to 
#port 0.0.0.0/0.0.0.0:32181 (org.apache.zookeeper.server.NIOServerCnxnFactory)

## Verificando o kafka
sudo docker-compose logs kafka | grep -i started

## Criando um topico
sudo docker-compose exec kafka  \
kafka-topics --create --topic meu-topico-legal --partitions 1 --replication-factor 1 \
--if-not-exists --zookeeper localhost:32181

## Confirmando o topico
sudo docker-compose exec kafka  \
  kafka-topics --describe --topic meu-topico-legal --zookeeper localhost:32181

## Removendo um TOPIC
sudo docker-compose exec kafka  kafka-topics --delete --topic LOJA.CMC_FIL --zookeeper localhost:32181


### Deve exibir algo parecido com isso
#Topic:meu-topico-legal PartitionCount:1 ReplicationFactor:1 Configs:
#Topic: meu-topico-legal Partition: 0 Leader: 1 Replicas: 1 Isr: 1

## Produzindo mensagens
sudo docker-compose exec kafka  \
bash -c "seq 100 | kafka-console-producer --request-required-acks 1 --broker-list localhost:29092 --topic meu-topico-legal && echo 'Produced 100 messages.'"

### Se tudo estiver certo vai mostrar: Produced 100 messages.

## Consumindo mensagens
docker-compose exec kafka  \
  kafka-console-consumer --bootstrap-server localhost:9092 --topic meu-topico-legal --from-beginning --max-messages 100

### Deve aparece isso
#1 
#....
#....
#100
#Processed a total of 100 messages
