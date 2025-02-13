class GerenciadorTarefas: 
    def __init__(self):
        self.tarefas = []  # Lista para armazenar as tarefas

    def adicionar_tarefa(self, descricao, prioridade="Média"):
        tarefa = {
            "id": len(self.tarefas) + 1,
            "descricao": descricao,
            "prioridade": prioridade,
            "concluida": False
        }
        self.tarefas.append(tarefa)
        print(f"Tarefa adicionada: {descricao}")

    def listar_tarefas(self): # Sem parâmetros 
        if not self.tarefas:
            print("Nenhuma tarefa pendente.") #Se não houver tarefas, imprime "nenhuma tarefa pendente e sai da função (return)C
            return
        print("\nTarefas pendentes:")
        for tarefa in self.tarefas:
            status = "✔ Concluída" if tarefa["concluida"] else "❌ Pendente"
            print(f"[{tarefa['id']}] {tarefa['descricao']} - Prioridade: {tarefa['prioridade']} - {status}")

    def concluir_tarefa(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                tarefa["concluida"] = True
                print(f"Tarefa {id_tarefa} concluída!")
                return
        print(f"Tarefa {id_tarefa} não encontrada.")

    def remover_tarefa(self, id_tarefa):
        for tarefa in self.tarefas:
            if tarefa["id"] == id_tarefa:
                self.tarefas.remove(tarefa)
                print(f"Tarefa {id_tarefa} removida!")
                return
        print(f"Tarefa {id_tarefa} não encontrada.")

# Exemplo de uso:
gerenciador = GerenciadorTarefas()
gerenciador.adicionar_tarefa("Estudar Estrutura de Dados", "Alta")
gerenciador.adicionar_tarefa("Treinar na academia", "Média")
gerenciador.adicionar_tarefa("Estudar python", "Média")
gerenciador.listar_tarefas() #Não precisa passar nada 
gerenciador.concluir_tarefa(1)
gerenciador.concluir_tarefa(3)
gerenciador.listar_tarefas()
gerenciador.remover_tarefa(2)
gerenciador.listar_tarefas()
