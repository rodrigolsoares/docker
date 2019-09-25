# Hbase Comandos

## Entrando no container do Hbase
sudo docker exec -i -t hbase-master hbase shell

## Criando tabela
create "table1", {NAME => "cf1"}, {NAME => "cf2"}


### Referências
* https://hub.docker.com/r/tobegit3hub/hbase-shell/

