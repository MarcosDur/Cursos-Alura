import os #importar ferramenta de fora 

# pessoas_cadastradas = ['Matheus', 'Breno'] declaração de lista de valores.
pessoas_cadastradas = [ {'nome':'João', 'gosto':'Amo Python', 'ativo':True},
                        {'nome':'Paula', 'gosto':'Não gosto', 'ativo':True},
                        {'nome':'Matias', 'gosto':'Mais ou menos', 'ativo':False}] 




def exibir_nome_do_programa():
    print('/n''''
╭━━━╮╱╱╭╮╱╱╱╱╱╱╱╱╱ ╭╮╱╱╱/╭━━━╮╱╱╱╭╮╭╮
┃╭━╮┃╱╱┃┃╱╱╱╱╱╱╱╱╱ ┃┃╱╱╱/┃╭━╮┃╱╱╭╯╰┫┃
┃╰━━┳━━┫╰━┳━━┳━╮ ╭━╯┣━━╮ ┃╰━╯┣╮╱┣╮╭┫╰━┳━━┳━╮
╰━━╮┃╭╮┃╭╮┃╭╮┃╭╯ ┃╭╮┃╭╮┃ ┃╭━━┫┃╱┃┃┃┃╭╮┃╭╮┃╭╮╮
┃╰━╯┃╭╮┃╰╯┃╰╯┃┃╱ ┃╰╯┃╰╯┃ ┃┃╱╱┃╰━╯┃╰┫┃┃┃╰╯┃┃┃┃
╰━━━┻╯╰┻━━┻━━┻╯╱ ╰━━┻━━╯ ╰╯╱╱╰━╮╭┻━┻╯╰┻━━┻╯╰╯
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱/╭━╯┃
╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱╱/╰━━╯'
''''/n');#precisamos colocar aspas triplas para poder incluir diversos texto sem perder a quebra de linha dentro do selecionado. No exemplo o título a cima 


def exibir_opcoes():
    '''Opção para o menu principal'''
    print('1 Adicione o nome e o quanto você ama PY')
    print('2 Ver pessoas que amam PY')
    print('3 Alterar status dos apaixonados por PY')
    print('4 Sair')


def finalizar_app():
    '''Essa mensagem irá aparecer após finalziar o aplicativo'''
    os.system('cls')
        # os.system('clear')#limpar o promptde comando em py no Apple
    print('Abraço ^_^\n ')

def volar_ao_menu_principal():
    '''No final de cada ação, retorna ao meno princ'''
    input("\nDigite uma tecla para voltar ao menu ")
    main()

def opcao_invalida():
    '''Exibe uma mensagem de erro e retorna para o menu
    Output: 
    - Rentornar ao menu principal

    '''
    print('Opção inválida!\n')
    volar_ao_menu_principal()


def exibir_subtitulo(texto):
    '''Títulos personalizados nas telas
    Input:
     - texto: string - O texto do subtítulo

       '''
    os.system("cls")
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_pessoa():
    '''Cadastramento dos amantes de Py
    Input: 
    - Nome das pessoas
    - Gosto 

    Output:
    - Adiciona uma pessoa noma com uma frase 
    '''
    exibir_subtitulo('Qual o nome da nova pessoa que ama Python?')
    nome_da_pessoa = input('Digite seu nome: ')
    # pessoas_cadastradas.append(nome_da_pessoa)
    categoria = input(f'O quanto que o(a) {nome_da_pessoa} gosta de Python? ')
    dados_pessoa = {'nome':nome_da_pessoa, 'gosto':categoria, 'ativo':False}
    pessoas_cadastradas.append(dados_pessoa)
    print(f'Parabéns {nome_da_pessoa}, você agora tem seu cadastro no Sabor de Python\n ')

    volar_ao_menu_principal()

def ver_pessoas_cadastradas():
    '''Consultar pessoas cadastradas e ver seu status e gosto'''
    exibir_subtitulo('Aqui estão as pessoas que amam PY: ')

    print(f'{'Nome'.ljust(12)} | {'O amor por Python'.ljust(25)} | Status')
    for pessoas in pessoas_cadastradas:
        pessoas_salvas = pessoas['nome']
        gosto_da_pessoa = pessoas['gosto']
        status = pessoas['ativo'] 
        print(f'- {pessoas_salvas.ljust(10)} - {gosto_da_pessoa.ljust(25)} - {status}')
        # print(" -  " + item) #Posso fazer assim ou fazer com o f string
        # print(f'. {pessoas}')
        
    volar_ao_menu_principal()

def alterar_estado_pessoa():
    '''Alterar o status de cada pessoa'''
    exibir_subtitulo('Alternando estado do apaixonado por Puthon')
    nome_pessoa = input('Digite o nome do apaixonado em Python que deseja alternar: ')
    pessoa_encontrada = False

    for pessoa in pessoas_cadastradas:
        if nome_pessoa == pessoa['nome']:
            pessoa_encontrada = True 
            pessoa['ativo'] = not pessoa['ativo'] 
            mensagem = f'O(a) {nome_pessoa} foi alterado com sucesso!' if pessoa['ativo'] else f'O(a) {nome_pessoa} foi desativado com sucesso!'
            print(mensagem)
    if not pessoa_encontrada:
        ('Poxa, que pena. O apaixona por Python não foi encontrado!')


    volar_ao_menu_principal()


def escolher_opcao():
    try:#aqui fazemos com que o programa tente realizar tudo que esta aqui, caso ele não consiga, irá excutar o except, que é a def q agente criou
        opcao_escolhida = int(input('Escolha uma opção: '))# = é utilizado para atribuição de valor; no input ele enra como string, mas após ser preenchido irá sair como um número inteiro
        #opcao_escolhida = int(opcao_escolhida) aqui ja deixamos ele como int na hr de preencher  

        #print('Você escolhei a opção:', opcao_escolhida) #posso usar assim para declarar a variável
        #print(f'A opção escolhida foi:{opcao_escolhida}') a forma mais facil de demonstrar a opção escolhida 


        # print(type(opcao_escolhida))#fazemos isso aqui para verificar qual o tipo da variável 
        # print(type(1))

        if opcao_escolhida == 1:
            cadastrar_pessoa()
        elif opcao_escolhida == 2:
            ver_pessoas_cadastradas()
        elif opcao_escolhida == 3:
            alterar_estado_pessoa()
        elif opcao_escolhida == 4:
            finalizar_app() #print('Lá no fundo eu sei que você gosta ^_^ ')
        else:
            opcao_invalida()
    except:
        opcao_invalida()



def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main() #função definida com oprincipal