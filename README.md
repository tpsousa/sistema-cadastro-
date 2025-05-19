# sistema-cadastro-elotec
#passo-a-passo

1.criar nosso menu de cadastro
 cadastrar missao
 listar missoes
 simular lancamentos
 sair
 de acordo com a opcao escolhida,chamamos uma determinada função.

2.criar as nossas funcoes :
 cadastrar missoes:
  nave string,
  destino string,
  tripulantes int ,
  combustivel float,
  duracao int ,
  obs:e objeto missao que ira armazenar essas informacoes
  armazenar nossas missoes dentro de uma lista
  mostrar que o cadastro foi realizado
  
 listar as nossas missoes:
  verificar se ha missoes dentro da nossa lista
  se nao estiver vazia iremos percorrer a nossa lista e mostraremos as missoes que estao dentro da lista
  e as informacoes dessas missoes
  
 simular lancamento:
   verificar se existem missoes dentro da nossa lista
   percorremos a lista e mostramos a missao,nome da nave e o destino
   escolhemos a missao que queremos mostrar - 1
   verificar se o indice da missao escolhida existe
   se o usuario escolher uma missao que nao esta na nossa lista,mostrar missao invalida.
   chamamos a missao de acordo com o indice
   verificamos o consumo que e a quantidade de tripulantes vezes 500
   mostraremos a informacao da nave que queremos simular o lancamento: o nome,o consumo,e o combustivel
   verificar se a quantidade de combustivel disponivel e maior que o consumo
   se for maior que o consumo o lancamento sera autorizado
   se nao,mostrara que o combustivel e insuficiente
   
   
