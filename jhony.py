from time import sleep



loop = input("Deseja iniciar o programa CARROS.COM? s ou n?")
while loop ==  "s":


    import mysql.connector
    import time


    conexao = mysql.connector.connect(  #conexao para variavel evitar lerdeza
        host="localhost",    
        user="root",
        password="",
        database="jhony"
        )
    minha_conexao= conexao.cursor()




    print(conexao)


    print ("Sistema de cadastro de carros")
    print("1-Cadastrar")
    print("2-Visualizar")
    print("3-Deletar")
    print("4-Alterar")
    opcao = input("digite o cógico desejado: ")


#QUEBRA ------------------------------------------------------------------------------------------------


    if (opcao == "1") or (opcao.lower()=="cadastrar"):
        #bloco de cadastro no banco de dados
        print("Olá funcionários")
        time.sleep(2)
        print("Tela de cadastros ")
        print("----------------------------------")
        time.sleep(1)
        print("FABRICAS - IDs")
        time.sleep(5)
        print("FORD - 1 ")
        print("Honda - 2")
        print("Ferrari - 3")
        print("Mercedes - 4")
        print("BMW - 5")
        print("Jeep - 6")
        time.sleep(1)
        print("Oque deseja cadastrar?")
        time.sleep(1)
        print("1-Criador da Fabrica")
        print("2-Nome da Fábrica")
        print("3-Nome do Carro")
        print("4-Nome do Cliente")
       
        opcao = input("digite o cógico desejado: ")
       
       
        if (opcao == "1") or (opcao.lower()=="criador da fabrica"):
            #BLOCO DE CÓGICO DE CADASTRO DA TABELA CRIADOR DA FABRICA
           
            nome_criador = input("Digite o nome do Criador: ")
            idade = int(input("Digite a idade do criador: "))
            id_criador = int(input("Digite o ID do criador: "))
            cadastro = "INSERT INTO criadorf VALUES (%s,%s,%s)" # Não esqueça de mudar o nome da tabela após o INSERT INTO
            dados = (nome_criador, idade, id_criador)
             
           
            minha_conexao.execute(cadastro, dados)


            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "Parabéns você fez os novos cadastros!!")    
       
        elif (opcao == "2") or (opcao.lower()=="nome da fábrica"):
            #BLOCO DE CÓGICO DE CADASTRO DA TABELA CRIADOR DA FABRICA
           
            nome_fabrica = input("Digite o nome da Fábrica: ")
            id_criador = int(input("Digite o id do criador: "))
            id_fabrica = int(input("Digite o ID da Fábrica: "))
            cadastro = "INSERT INTO fabrica VALUES (%s,%s,%s)" # Não esqueça de mudar o nome da tabela após o INSERT INTO
            dados = (id_fabrica, nome_fabrica, id_criador)
             
           
            minha_conexao.execute(cadastro, dados)


            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "Parabéns você fez os novos cadastros!!")    
       
        elif (opcao == "3") or (opcao.lower()=="nome do carro"):
            #BLOCO DE CÓGICO DE CADASTRO DA TABELA CARROS
           
            nome_carro = input("Digite o nome do carro: ")
            id_carro = int(input("Digite o id do carro: "))
            id_fabrica = int(input("Digite o ID da Fábrica: "))
            cadastro = "INSERT INTO carros VALUES (%s,%s,%s)" # Não esqueça de mudar o nome da tabela após o INSERT INTO
            dados = (id_fabrica, nome_carro, id_carro)
             
           
            minha_conexao.execute(cadastro, dados)


            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "Parabéns você fez os novos cadastros!!")          
       
        elif (opcao == "4") or (opcao.lower()=="nome do cliente"):


            #BLOCO DE CÓGICO DE CADASTRO DA TABELA CLIENTES
           
            nome_dele = input("Digite o nome do cliente: ")
            id_do_cliente = int(input("Digite o ID  do cliente: "))
            id_do_carro = int(input("Digite o ID do carro: "))
            cadastro = "INSERT INTO clientes VALUES (%s,%s,%s)"
            dados = (id_do_carro, nome_dele, id_do_cliente)
             
            minha_conexao = conexao.cursor()
            minha_conexao.execute(cadastro,dados)


            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "Parabéns você fez os novos cadastros!!")    
   
        else:
            time.sleep(6)
            print("Opção invalida !")



#QUEBRA ------------------------------------------------------------------------------------------------


   
    elif (opcao == "2") or (opcao.lower()=="visualizar"):
        #bloco de visualização no banco de dados
        print("Olá funcionários!!")
        time.sleep(2)
        print("registro carregados")
        time.sleep(4)
        print("Você quer carregar qual tabela existente? ")
        print("1-Criador da Fabrica")
        print("2-Nome da Fábrica")
        print("3-Nome do Carro")
        print("4-Nome do Cliente")
        time.sleep(2)
        opcao = input("digite o cógico desejado: ")


        if (opcao == "1") or (opcao.lower()=="criador da fabrica"):
            minha_conexao= conexao.cursor()

            minha_conexao.execute("SELECT * from criadorf")
             
            for linha in minha_conexao:
                print(linha) #criar um looping para mostrar o'que tenho dentro da tabela
                       
           
        elif (opcao == "2") or (opcao.lower()=="nome da fábrica"):
            minha_conexao= conexao.cursor()

            minha_conexao.execute("SELECT * from fabrica")
             
            for linha in minha_conexao:
                print(linha) #criar um looping para mostrar o'que tenho dentro da tabela
           
           
        elif (opcao == "3") or (opcao.lower()=="nome do carro"):
            minha_conexao= conexao.cursor()

            minha_conexao.execute("SELECT * from carros")
             
            for linha in minha_conexao:
                print(linha) #criar um looping para mostrar o'que tenho dentro da tabela
           
           
        elif (opcao == "4") or (opcao.lower()=="nome do cliente"):
            minha_conexao= conexao.cursor()

            minha_conexao.execute("SELECT * from clientes")
             
            for linha in minha_conexao:
                print(linha) #criar um looping para mostrar o'que tenho dentro da tabela


        else:
            time.sleep(6)
            print("Opção invalida !")
       
#QUEBRA ------------------------------------------------------------------------------------------------


    elif (opcao == "3") or (opcao.lower()=="deletar"):
        #bloco de exclusão no banco de dados
        print("Você deseja apagar a linha de dados de qual tabela ?")
        time.sleep(2)
        print("4 - Nome do Cliente")
        print("3 - Nome do carro")
        print("2 - Nome da Fábrica")
        print("1 - Criador da Fábrica")
        time.sleep(2)
        opcao = input("digite o cógico desejado: ")


        if (opcao == "1") or (opcao.lower()=="criador da fabrica"):
            minha_conexao= conexao.cursor()
            apagao = ( input("Digite o ID do criador que você quer excluir:"), )
            cadastro = "DELETE from criadorf where id_criador = %s" 
            minha_conexao.execute(cadastro, apagao)
            
            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "registro deletado !")        



        elif (opcao == "2") or (opcao.lower()=="nome da fábrica"):
            minha_conexao= conexao.cursor()
            apagao = ( input("Digite o ID da tabela que você quer excluir:"), )
            cadastro = "DELETE from fabrica where id_fabrica = %s" 
            minha_conexao.execute(cadastro, apagao)
            
            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "registro deletado !")  



        elif (opcao == "3") or (opcao.lower()=="nome do carro"):
            minha_conexao= conexao.cursor()
            apagao = ( input("Digite o ID da fabrica que você quer excluir:"), )
            cadastro = "DELETE from carros where id_carro = %s" 
            minha_conexao.execute(cadastro, apagao)
            
            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "registro deletado !")
           


        elif (opcao == "4") or (opcao.lower()=="nome do cliente"):
            minha_conexao= conexao.cursor()
            apagao = (input("Digite o ID do cliente que você quer excluir: "), )
            cadastro = "DELETE from clientes where id_clientes = %s" 
            minha_conexao.execute(cadastro, apagao)
            
            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "registro deletado !")
        
        else:
            time.sleep(6)
            print("Opção invalida !")


           
#QUEBRA ------------------------------------------------------------------------------------------------


    elif (opcao == "4") or (opcao.lower()=="alterar"):
        #bloco de alteração no banco de dados
        print("Olá você quer alterar qual tabela? ")
        print(" ")
        time.sleep(2)
        print("1-Criador da Fabrica")
        print("2-Nome da Fábrica")
        print("3-Nome do Carro")
        print("4-Nome do Cliente")
        time.sleep(2)
        opcao = input("digite o cógico desejado: ")
        if (opcao == "1") or (opcao.lower()=="criador da fabrica"):
            #BLOCO DE CÓGICO DE ATUALIZAÇÃO DA TABELA CRIADOR DA FABRICA
           
            nome_criador = input("Digite o nome do Criador: ")
            idade = int(input("Digite a idade do criador: "))
            id_criador = int(input("Digite o ID do criador: "))
            cadastro = "UPDATE criadorf VALUES (%s,%s,%s)" # Não esqueça de mudar o nome da tabela após o INSERT INTO
            dados = (nome_criador, idade, id_criador)
       
            minha_conexao.execute(cadastro, dados)
            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "\nParabéns você atualizou com os novos dados!!")  
           
        elif (opcao == "2") or (opcao.lower()=="nome da fábrica"):
            #BLOCO DE CÓGICO DE ATUALIZAÇÃO DA TABELA NOME DA FABRICA


            nome_fabrica = input("Digite o nome da Fábrica: ")
            id_criador = int(input("Digite o id do criador: "))
            id_fabrica = int(input("Digite o ID da Fábrica: "))
            cadastro = "UPDATE fabrica VALUES (%s,%s,%s)" # Não esqueça de mudar o nome da tabela após o INSERT INTO
            dados = (id_fabrica, nome_fabrica, id_criador)
           
            minha_conexao.execute(cadastro, dados)
            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "\nParabéns você atualizou com os novos dados!!")  
           
        elif (opcao == "3") or (opcao.lower()=="nome do carro"):
            #BLOCO DE CÓGICO DE ATUALIZAÇÃO DA TABELA NOME DO CARRO


            nome_carro = input("Digite o nome do carro: ")
            id_carro = int(input("Digite o id do carro: "))
            id_fabrica = int(input("Digite o ID da Fábrica: "))
            cadastro = "UPDATE carros VALUES (%s,%s,%s)" # Não esqueça de mudar o nome da tabela após o INSERT INTO
            dados = (id_fabrica, nome_carro, id_carro)
           
            minha_conexao.execute(cadastro, dados)
            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "\nParabéns você atualizou com os novos dados!!")


           
        elif (opcao == "4") or (opcao.lower()=="nome do cliente"):
            #BLOCO DE CÓGICO DE ATUALIZAÇÃO DA TABELA NOME DO CLIENTE


            nome_dele = input("Digite o nome do cliente: ")
            id_do_cliente = int(input("Digite o ID  do cliente: "))
            id_do_carro = int(input("Digite o ID do carro: "))
            cadastro = "UPDATE clientes VALUES (%s,%s,%s)"
            dados = (id_do_carro, nome_dele, id_do_cliente)
           
            minha_conexao.execute(cadastro, dados)
            conexao.commit() # como se eu tivesse encerrado para que não bugue, para que faça cadastramento de dados atoa
            print( minha_conexao.rowcount, "\nParabéns você atualizou com os novos dados!!")


        else:
            time.sleep(6)
            print("opção invalida !")
       


#QUEBRA ------------------------------------------------------------------------------------------------
       


    else:
            print("Opção invalida")
       
    loop = input("Deseja voltar ao menu s ou n?:")


print("Obrigado por usar o programa CARROS.com")