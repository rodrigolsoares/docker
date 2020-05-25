# Hbase Comandos


## Entrando no container do Hbase
sudo docker exec -i -t hbase-master hbase shell


## Verificando o HBase
* status
* status 'simple'
* status 'summary'
* status 'detailed'
* version
* table help
* list

## Criando Namespace
create_namespace 'nome do namespace'

## Visualizando todos os namespace
list_namespacescan

## Removendo namespace
drop_namespace 'nome do namespace'

## Criando Column Family
* create "table1", {NAME => "cf1"}, {NAME => "cf2"}


## Desabilitando uma tabela
*disable 'Nome da tabela'


## Habilitando uma tabela
* enable 'Nome da tabela'


## Drop table
* drop 'nome da tabela'


### Observação
* Para remover uma tabela é preciso desabilitar o objeto primeiro


## Descrição da table
* describe 'Nome da tabela'


## Contando registros
* count 'Nome da tabela'


## Criando/Atualizando
* put 'Nome da tabela', 'linha', 'coluna', 'valor'


## truncate table 
* truncate 'nome da tabela'


## Visualizando registros
* scan 'Nome da tabela', {RAW=>true,VERSIONS =>1000}


### Referências
* https://hub.docker.com/r/tobegit3hub/hbase-shell/
* https://www.guru99.com/hbase-shell-general-commands.html


