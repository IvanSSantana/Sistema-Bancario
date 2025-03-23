#Depósito, Saque e Extrato
saques_realizados = 0
LIMITE_SAQUE = 500
saldo = 0
extrato_gerado = False
operacoes = []

def gerar_extrato ():
    extrato = """
       ===== Extrato =====
"""
    deposito = 1
    saque = 1

    #Adicionando operações no extrato
    for operacao in operacoes:
        if operacao > 0: #Depósito
            extrato += f"""
            Depósito {deposito}:
            Valor: R$ {operacao:.2f}
"""
            deposito += 1

        elif operacao < 0: #Saque
            extrato += f"""
            Saque {saque}:
            Valor: R$ {-operacao:.2f}
"""
            saque += 1

        else:
            pass

    #Saldo final
    extrato += f"""
        Saldo final: {round(saldo, 2)}"""
    
    return extrato

while extrato_gerado == False:
    opcao = input("""
        ===MENU===
                
        [D]epósito
        [S]aque
        [E]xtrato
        [Q]uit          
        Escolha: """).lower()
    
    try:
        if opcao == 'd': #Depósito
            valor = float(input('Valor: '))
            if valor > 0:
                saldo += valor
                operacoes.append(valor)
            else:
                print('Operação inválida.')

        elif opcao == 's': #Saque
            if saques_realizados < 3: #Verificação de limite
                valor = float(input('Valor: '))

                #Saque inválido -> força geração do extrato
                if valor > saldo:
                    print('Estourou o limite.')
                    print(gerar_extrato())
                    extrato_gerado = True
                    
                operacoes.append(-valor)
                saldo -= valor
                saques_realizados += 1

            else: #Limite de saques
                print('Você realizou o máximo de saques disponíveis. A seguir veja o extrato.')
                print(gerar_extrato())
                extrato_gerado = True

        elif opcao == 'e': #Extrato
            if operacoes == []: #Caso não haja operações
                print('\nVocê não realizou nenhuma operação.')
                break
            else: 
                print(gerar_extrato())
                extrato_gerado = True
        
        elif opcao == 'q':
            break
        
        else: #Operação inválida
            print('Opcão inválida. Tente novamente.')

    except ValueError:
        print('Valor inválido.')