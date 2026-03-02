class Livro:
    def __init__(self):
        #Variáveis
        self.titulo = [] #Título do livro
        self.autor = [] #Autor do livro
        self.disp = bool() #Disponibilidade

    
    ###Métodos
    #Emprestar livro
    def emprestar(self):
        print('Versão protótipo (sem resultado)')

    #Devolver livro
    def devolver(self):
        print('Versão protótipo (sem resultado)')

    #str
    def __str__(self):
        return f'Título = {self.titulo}\nAutor = {self.autor}\nDisponibilidade = {self.disp}'


class Usuario:
    def __init__(self):
        #Variáveis
        self.ra = [] #ID do aluno
        self.nome = [] #Nome do aluno
        self.lista_de_livros_emprestados = [] #Livros que já estão emprestados para ele
    

    ###Métodos
    #Emprestar livro para esse usuário
    def emprestar_livro(self, livro):
        print('Versão protótipo (sem resultado)')

    #Devolver livro desse usuário
    def devolver_livro(self, livro):
        print('Versão protótipo (sem resultado)')

    #Listar os livros desse usuário
    def listar_livros(self):
        print('Versão protótipo (sem resultado)')



class Biblioteca:
    def __init__(self):
        #Variáveis
        self.lista_de_livros = [] #Lista com os livros cadastrados
        self.lista_de_usuarios = [] #Lista com os usuários cadastrados

    
    ###Métodos
    #Cadastro de livro (Terminado) + Objeto
    def cadastrar_livro(self, livro):
        #Verificar se o livro já existe
        loc = 0
        for livro_lista in self.lista_de_livros: #Procurando pelos livros da biblioteca
            if(str(livro_lista.titulo) == str(livro.titulo)): #Verificando por outro livro com esse título
                loc = 1 #Já tem o nome na biblioteca
        if(loc == 0):
            livro.disp = bool(True) #Tornando o livro disponível para empréstimo
            self.lista_de_livros.append(livro) #Adicionando o livro a biblioteca
        else:
            print('Esse livro já está na biblioteca')
        
    #Cadastro de usuário (Terminado) + Objeto
    def cadastrar_usuario(self, usuario):
        #Verificar se o usuário já existe
        loc = 0
        for usuario_lista in self.lista_de_usuarios: #Procurando pelos alunos já cadastrados
            if(str(usuario_lista.ra) == str(usuario.ra)): #Procurando outro aluno com o mesmo ra
                loc = 1 #Já tem o ra na biblioteca
        if(loc == 0):
            self.lista_de_usuarios.append(usuario) #Adicionando usuário na biblioteca
        else:
            print('Esse ra já está sendo utilizado')

    #Realizar empréstimo (Terminado)
    def realizar_emprestimo(self, ra, titulo_livro):
        #Verificar se o livro existe
        for livro_lista in self.lista_de_livros: #Procurando pelos livros da biblioteca
            if(str(livro_lista.titulo) == str(titulo_livro)): #Verificando por outro livro com esse título
                #Verificar se o aluno existe
                for usuario_lista in self.lista_de_usuarios: #Procurando pelos alunos já cadastrados
                    if(str(usuario_lista.ra) == str(ra)): #Procurando outro aluno com o mesmo ra
                        #Verificando se o livro está disponível para empréstimo
                        if(livro_lista.disp == bool(True)):
                        #Realizar o empréstimo
                            usuario_lista.lista_de_livros_emprestados.append(livro_lista) #Emprestando o livro
                            livro_lista.disp = bool(False)
                        else: print('O livro já está emprestado para alguém')

    #Devolver o livro (Terminado)
    def realizar_devolucao(self, ra, titulo_livro):
        #Verificar se o livro existe
        for livro_lista in self.lista_de_livros: #Procurando pelos livros da biblioteca
            if(str(livro_lista.titulo) == str(titulo_livro)): #Verificando por outro livro com esse título
                #Verificar se o aluno existe
                for usuario_lista in self.lista_de_usuarios: #Procurando pelos alunos já cadastrados
                    if(str(usuario_lista.ra) == str(ra)): #Procurando outro aluno com o mesmo ra
                        #Verificando se ele tem o livro para devolver
                        for livro_emprestado_usuario in usuario_lista:
                            if(livro_emprestado_usuario.titulo == titulo_livro): #Achando o livro na lista do aluno
                                usuario_lista.pop(usuario_lista.index(livro_emprestado_usuario.titulo)) #Removendo o livro da lista do aluno
                                livro_lista.disp = bool(True) #Disponibilizando o livro para empréstimo

    #Listar todos os livros disponíveis (Terminado)
    def listar_livros_disponiveis(self):
        #Verificando a lista de livros e imprimindo
        for livro in self.lista_de_livros:
            if(livro.disp == bool(True)):
                print(livro)

    #Listar todos os livros emprestados para esse usuário (Terminado)
    def listar_livros_emprestados_usuario(self, ra):
        #Verificar se o aluno existe
        for usuario_lista in self.lista_de_usuarios: #Procurando pelos alunos já cadastrados
            if(str(usuario_lista.ra) == str(ra)): #Procurando outro aluno com o mesmo ra
                print('O aluno referido foi encontrado')
                #Listando os livros emprestados para determinado aluno
                for livro in usuario_lista.lista_de_livros_emprestados:
                    print(f'Os livros emprestados para o usuário {usuario_lista.nome[usuario_lista.ra]} foram {livro}')




class Main:
    def __init__(self):
        self.base = Biblioteca()        

    def Indexing():
        #Verificando o que o usuário quer fazer
        indexer = input('Que operação você deseja realizar? (Insira apenas o número da operação)\n1. Cadastrar livro\n2. Cadastrar usuário\n3. Realizar empréstimo\n4. Realizar devolução\n5. Listar livros disponíveis\n6. Listar livros emprestados ao usuário\n7. Finalizar')

        match indexer:
            case 1: #Cadastrar livro
                novolivro = Livro()
                nome = input('Qual o nome do livro?')
                autor = input('Qual o autor do livro?')
                novolivro.nome = nome
                novolivro.autor = autor
                base.cadastrar_livro(novolivro)
            case 2: #Cadastrar usuário
                novousuario = Usuario()
                nome = input('Qual o nome do aluno?')
                ra = input('Qual o ra do aluno?')
                novousuario.ra = ra
                novousuario.nome = nome
                base.cadastrar_usuario(novousuario)
            case 3:
                ra = input('Qual o ra do aluno?')
                titulo = input('Qual o titulo do livro?')
                base.realizar_emprestimo(ra, titulo)
            case 4:
                ra = input('Qual o ra do aluno?')
                titulo = input('Qual o titulo do livro?')
                realizar_devolucao(ra, titulo)
            case 5:
                base.listar_livros_disponiveis()
            case 6:
                ra = input('Qual o ra do aluno?')
                base.listar_livros_emprestados_usuario(ra)



#Teste do Código
