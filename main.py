
import function from *


missoes = []

#criando a funcao de criar um menu
def menu():
 while(true):
    print("seja bem vindo(a) ao sistema de cadastro");
    print("1.cadastrar um usuario")
    print("2.listar missoes")
    print("3.simular lancamentos")
    print("4.sair");
    
    opcao = input("escolha uma dessas opcoes");
    
    if opcao == '1':
        cadastrarMissao(missao);
    elif opcao=='2':
        ListarMissoes(missao);
    elif opcao =='3':
        SimularLancamento(missao);
    elif opcao =='4':
        print("saindo....")
        break
    else:
        print("missao encerrada")

menu()

  