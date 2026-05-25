from abc import ABC, abstractmethod
from typing import Protocol

# === PARTE A - Contrato Rígido usando ABC ===
class Armazenador(ABC):
    @abstractmethod
    def salvar(self, dado: str):
        pass

class ArmazenadorArquivo(Armazenador):
    def salvar(self, dado: str):
        print(f"Salvando '{dado}' em arquivo local.")

class ArmazenadorBanco(Armazenador):
    def salvar(self, dado: str):
        print(f"Inserindo '{dado}' no banco de dados.")


# === PARTE B - Contrato Flexível usando Protocol ===
class Salvavel(Protocol):
    def salvar(self, dado: str) -> None:
        ...

# Não herda de 'Armazenador', mas possui a estrutura (método salvar)
class ArmazenadorNuvem:
    def salvar(self, dado: str):
        print(f"Fazendo upload de '{dado}' para a nuvem.")


# === PARTE C - Funções de Execução ===
def executar_salvamento_formal(armazenador: Armazenador, dado: str):
    # Só aceita quem é explicitamente herdeiro de Armazenador
    armazenador.salvando = True # Exemplo de controle interno da hierarquia
    armazenador.salvar(dado)

def executar_salvamento_flexivel(objeto: Salvavel, dado: str):
    # Aceita QUALQUER objeto que tenha o método salvar(dado)
    objeto.salvar(dado)
