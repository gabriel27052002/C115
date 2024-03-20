from questionario_crud import QuestionarioCRUDDatabase

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, pergunta, function):
        self.commands[pergunta] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")

class questionarioCLI(SimpleCLI):
    def __init__(self, questionario_model):
        super().__init__()
        self.questionario_model = questionario_model
        self.add_command("create_questionario", self.create_questionario)
        self.add_command("read_questionario", self.read_questionario)
        self.add_command("responder_questionario", self.responder_questionario)
        self.add_command("update_questionario", self.update_questionario)
        self.add_command("delete_questionario", self.delete_questionario)

    def create_questionario(self):
        pergunta = input("Crie uma pergunta para o questionario: ")
        alternativaA = input("Crie uma alternativa A para o questionario: ")
        alternativaB = input("Crie uma alternativa B para o questionario: ")
        alternativaC = input("Crie uma alternativa C para o questionario: ")
        alternativaD = input("Crie uma alternativa D para o questionario: ")
        resposta = input("Resposta correta do questionario: ")
        self.questionario_model.create_questionario(pergunta, alternativaA, alternativaB, alternativaC, alternativaD, resposta)
           
    def read_questionario(self):
        id = input("Entre com o id: ")
        questionario = self.questionario_model.read_questionario_by_id(id)
        if questionario:
            print(f"Pergunta do questionario: {questionario['pergunta']}")
            print(f"Alternativa A do questionario: {questionario['alternativaA']}")
            print(f"Alternativa B do questionario: {questionario['alternativaB']}")
            print(f"Alternativa C do questionario: {questionario['alternativaC']}")
            print(f"Alternativa D do questionario: {questionario['alternativaD']}")
            print(f"Resposta do questionario: {questionario['resposta']}")

    def responder_questionario(self):

        respostas_corretas = 0
        respostas_incorretas = 0

        for pergunta_atual in range(1, 4):
            if pergunta_atual == 1:
                id = "64e4f48af0ad2f51ca56002a"
            if pergunta_atual == 2:
                id = "64e51efb777691f01be1bd69"
            if pergunta_atual == 3:
                id = "64e5200e777691f01be1bd6a"
            questionario = self.questionario_model.read_questionario_by_id(id)
            if questionario:
                print(f"Pergunta: {questionario['pergunta']}")
                print(f"A: {questionario['alternativaA']}")
                print(f"B: {questionario['alternativaB']}")
                print(f"C: {questionario['alternativaC']}")
                print(f"D: {questionario['alternativaD']}")
                resposta_dada = input("Escolha uma alternativa do questionario para a resposta correta: ")
                if resposta_dada == questionario['resposta']:
                    print("Acertou!!!")
                    respostas_corretas += 1
                    pergunta_atual = pergunta_atual + 1
                else:
                    print("Resposta incorreta.")
                    print("Resposta correta:", questionario['resposta'])
                    respostas_incorretas += 1
                    pergunta_atual = pergunta_atual + 1
        print("Fim do questionario!")
        print("Numero de acertos:", respostas_corretas)
        print("Numero de erros:", respostas_incorretas)
                    
    def update_questionario(self):
        id = input("Enter the id: ")
        pergunta = input("Crie uma nova pergunta para o questionario: ")
        alternativaA = input("Crie uma nova alternativa A para o questionario: ")
        alternativaB = input("Crie uma nova alternativa B para o questionario: ")
        alternativaC = input("Crie uma nova alternativa C para o questionario: ")
        alternativaD = input("Crie uma nova alternativa D para o questionario: ")
        resposta = input("Atualize a resposta do questionario: ")
        self.questionario_model.update_questionario(id, pergunta, alternativaA, alternativaB, alternativaC, alternativaD, resposta)

    def delete_questionario(self):
        id = input("Entre com o id: ")
        self.questionario_model.delete_questionario(id)

    def run(self):
        print("Welcome to the Questionario CLI!")
        print("Available commands: create_questionario, read_questionario, responder_questionario, update_questionario, delete_questionario, quit")
        super().run()