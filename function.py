
#funcao para cadastrar uma missao dentro da nossa lista
def cadastrarMissao(lista):
    print("seja bem vindo a pagina de cadastro");
    nave = input("digite o nome da nave");
    destino = input("digite o destino");
    tripulantes = int(input("diga a quantidade de tripulantes"));
    combustivel  = float(input("diga a quantidade de combustivel (litros)"))
    tempo = int(input("diga o tempo de duração da viagem (dias)"));

    missao = {
        "nave" : nave,
        "destino": destino,
        "tripulantes": tripulantes,
        "combustivel" : combustivel,
        "tempo": tempo
    }

    lista.append(missao);
    print("missão cadastrada com sucesso")



