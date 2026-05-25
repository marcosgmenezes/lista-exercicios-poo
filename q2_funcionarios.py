from abc import ABC, abstractmethod

# 1. Classe abstrata Funcionario
class Funcionario(ABC):
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def mostrar_dados(self):
        print(f"Funcionário: {self.nome} | CPF: {self.cpf}")

    @abstractmethod
    def calcular_pagamento(self) -> float:
        pass

# 2. Subclasse FuncionarioAssalariado
class FuncionarioAssalariado(Funcionario):
    def __init__(self, nome: str, cpf: str, salario_mensal: float):
        super().__init__(nome, cpf)
        self.salario_mensal = salario_mensal

    def calcular_pagamento(self) -> float:
        return self.salario_mensal

# 3. Subclasse FuncionarioHorista
class FuncionarioHorista(Funcionario):
    def __init__(self, nome: str, cpf: str, horas_trabalhadas: float, valor_hora: float):
        super().__init__(nome, cpf)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_pagamento(self) -> float:
        return self.horas_trabalhadas * self.valor_hora

# 4. Subclasse FuncionarioComissionado
class FuncionarioComissionado(Funcionario):
    def __init__(self, nome: str, cpf: str, total_vendas: float, percentual_comissao: float):
        super().__init__(nome, cpf)
        self.total_vendas = total_vendas
        self.percentual_comissao = percentual_comissao  # Ex: 0.10 para 10%

    def calcular_pagamento(self) -> float:
        return self.total_vendas * self.percentual_comissao

# 5. Classe Empresa
class Empresa:
    def __init__(self, nome: str):
        self.nome = nome
        self._funcionarios = []

    def adicionar_funcionario(self, funcionario: Funcionario):
        self._funcionarios.append(funcionario)

    def listar_funcionarios(self):
        print(f"\n--- Quadro de Funcionários da {self.nome} ---")
        for f in self._funcionarios:
            f.mostrar_dados()

    def mostrar_folha_pagamento(self):
        print(f"\n--- Folha de Pagamento: {self.nome} ---")
        total_folha = 0
        for f in self._funcionarios:
            pagamento = f.calcular_pagamento()
            total_folha += pagamento
            print(f"- {f.nome}: R$ {pagamento:.2f}")
        print(f"Total Gasto: R$ {total_folha:.2f}")
