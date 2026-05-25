from typing import Protocol

# 1. Protocolo Imprimivel (Contrato estrutural)
class Imprimivel(Protocol):
    def imprimir(self) -> None:
        ...

# 2. Classe Boleto (Não herda explicitamente de Imprimivel)
class Boleto:
    def __init__(self, codigo: str, valor: float):
        self.codigo = codigo
        self.valor = valor

    def imprimir(self):
        print(f"Imprimindo Boleto | Código: {self.codigo} | Valor: R$ {self.valor:.2f}")

# 3. Classe Etiqueta
class Etiqueta:
    def __init__(self, destinatario: str, endereco: str):
        self.destinatario = destinatario
        self.endereco = endereco

    def imprimir(self):
        print(f"Imprimindo Etiqueta | Destinatário: {self.destinatario} | Endereço: {self.endereco}")

# 4. Classe RelatorioSimples
class RelatorioSimples:
    def __init__(self, titulo: str):
        self.titulo = titulo

    def imprimir(self):
        print(f"Imprimindo Relatório: {self.titulo}")

# 5. Função processar_impressao
def processar_impressao(item: Imprimivel):
    # Qualquer objeto que possua o método 'imprimir()' é aceito
    item.imprimir()
