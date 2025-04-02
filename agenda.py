from pymongo import MongoClient
from bson.objectid import ObjectId

class ContatoTelefonico:
    def __init__(self):
        # Conexão com o MongoDB (altere a string de conexão conforme necessário)
        self.client = MongoClient('mongodb+srv://carlossoaresads:X1c6Z96B3t9D3gNI@cluster0.fmshe.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
        
        self.db = self.client['agenda_telefonica']
        self.contatos = self.db['contatos']
    
    def adicionar_contato(self):
        print("\n--- Adicionar Novo Contato ---")
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email (opcional): ") or None
        categoria = input("Categoria (ex: família, trabalho, amigos) (opcional): ") or None
        
        contato = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "categoria": categoria
        }
        
        resultado = self.contatos.insert_one(contato)
        print(f"\nContato adicionado com ID: {resultado.inserted_id}")
    
    def listar_contatos(self):
        print("\n--- Lista de Contatos ---")
        for contato in self.contatos.find():
            print(f"\nID: {contato['_id']}")
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            if contato.get('email'):
                print(f"Email: {contato['email']}")
            if contato.get('categoria'):
                print(f"Categoria: {contato['categoria']}")
        print("\n")
    
    def atualizar_contato(self):
        self.listar_contatos()
        contato_id = input("\nDigite o ID do contato que deseja atualizar: ")
        
        try:
            objeto_id = ObjectId(contato_id)
        except:
            print("ID inválido!")
            return
        
        contato = self.contatos.find_one({"_id": objeto_id})
        if not contato:
            print("Contato não encontrado!")
            return
        
        print("\nDeixe em branco para manter o valor atual")
        nome = input(f"Nome [{contato['nome']}]: ") or contato['nome']
        telefone = input(f"Telefone [{contato['telefone']}]: ") or contato['telefone']
        email = input(f"Email [{contato.get('email', '')}]: ") or contato.get('email')
        categoria = input(f"Categoria [{contato.get('categoria', '')}]: ") or contato.get('categoria')
        
        atualizacao = {
            "$set": {
                "nome": nome,
                "telefone": telefone,
                "email": email,
                "categoria": categoria
            }
        }
        
        self.contatos.update_one({"_id": objeto_id}, atualizacao)
        print("\nContato atualizado com sucesso!")
    
    def remover_contato(self):
        self.listar_contatos()
        contato_id = input("\nDigite o ID do contato que deseja remover: ")
        
        try:
            objeto_id = ObjectId(contato_id)
        except:
            print("ID inválido!")
            return
        
        resultado = self.contatos.delete_one({"_id": objeto_id})
        if resultado.deleted_count > 0:
            print("\nContato removido com sucesso!")
        else:
            print("\nContato não encontrado!")
    
    def pesquisar_contato(self):
        termo = input("\nDigite o nome ou telefone para pesquisar: ")
        
        query = {
            "$or": [
                {"nome": {"$regex": termo, "$options": "i"}},
                {"telefone": {"$regex": termo}}
            ]
        }
        
        print("\n--- Resultados da Pesquisa ---")
        encontrados = False
        for contato in self.contatos.find(query):
            encontrados = True
            print(f"\nID: {contato['_id']}")
            print(f"Nome: {contato['nome']}")
            print(f"Telefone: {contato['telefone']}")
            if contato.get('email'):
                print(f"Email: {contato['email']}")
            if contato.get('categoria'):
                print(f"Categoria: {contato['categoria']}")
        
        if not encontrados:
            print("Nenhum contato encontrado.")
        print("\n")
    
    def menu(self):
        while True:
            print("\n--- Agenda Telefônica ---")
            print("1. Adicionar Contato")
            print("2. Listar Contatos")
            print("3. Atualizar Contato")
            print("4. Remover Contato")
            print("5. Pesquisar Contato")
            print("6. Sair")
            
            opcao = input("\nEscolha uma opção: ")
            
            if opcao == "1":
                self.adicionar_contato()
            elif opcao == "2":
                self.listar_contatos()
            elif opcao == "3":
                self.atualizar_contato()
            elif opcao == "4":
                self.remover_contato()
            elif opcao == "5":
                self.pesquisar_contato()
            elif opcao == "6":
                print("\nSaindo do sistema...")
                self.client.close()
                break
            else:
                print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    app = ContatoTelefonico()
    app.menu()