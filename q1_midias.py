from abc import ABC, abstractmethod

# 1. Classe abstrata Midia
class Midia(ABC):
    def __init__(self, titulo: str, duracao: int):
        self.titulo = titulo
        self.duracao = duracao  # em minutos

    def mostrar_info(self):
        print(f"Mídia: {self.titulo} | Duração: {self.duracao} min")

    @abstractmethod
    def reproduzir(self):
        pass

# 2. Subclasse Video
class Video(Midia):
    def __init__(self, titulo: str, duracao: int, resolucao: str):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def reproduzir(self):
        print(f"Reproduzindo Vídeo: '{self.titulo}' em {self.resolucao}...")

# 3. Subclasse Podcast
class Podcast(Midia):
    def __init__(self, titulo: str, duracao: int, apresentador: str):
        super().__init__(titulo, duracao)
        self.apresentador = apresentador

    def reproduzir(self):
        print(f"Reproduzindo Podcast: '{self.titulo}' com {self.apresentador}...")

# 4. Subclasse TextoNarrado
class TextoNarrado(Midia):
    def __init__(self, titulo: str, duracao: int, idioma: str):
        super().__init__(titulo, duracao)
        self.idioma = idioma

    def reproduzir(self):
        print(f"Reproduzindo Texto Narrado: '{self.titulo}' em [{self.idioma}]...")

# 5. Classe Plataforma
class Plataforma:
    def __init__(self, nome: str):
        self.nome = nome
        self._midias = []

    def adicionar_midia(self, midia: Midia):
        self._midias.append(midia)

    def listar_midias(self):
        print(f"\n--- Mídias disponíveis na {self.nome} ---")
        for m in self._midias:
            m.mostrar_info()

    def reproduzir_todas(self):
        print(f"\n--- Iniciando a reprodução automática na {self.nome} ---")
        for m in self._midias:
            m.reproduzir()  # Polimorfismo em ação
