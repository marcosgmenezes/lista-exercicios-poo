from abc import ABC, abstractmethod

# 1. Classe abstrata Notificador
class Notificador(ABC):
    @abstractmethod
    def notificar(self, mensagem: str):
        pass

# 2. Classe NotificadorEmail
class NotificadorEmail(Notificador):
    def notificar(self, mensagem: str):
        print(f"Enviando E-mail: {mensagem}")

# 3. Classe NotificadorSMS
class NotificadorSMS(Notificador):
    def notificar(self, mensagem: str):
        print(f"Enviando SMS: {mensagem}")

# 4. Classe NotificadorApp
class NotificadorApp(Notificador):
    def notificar(self, mensagem: str):
        print(f"📱 Notificação Push no App: {mensagem}")

# 5. Classe CentralNotificacoes
class CentralNotificacoes:
    def __init__(self):
        self._notificadores = []

    def adicionar_notificador(self, notificador: Notificador):
        self._notificadores.append(notificador)
  
    def enviar_para_todos(self, mensagem: str):
        print(f"\n--- Disparando Central de Notificações ---")
        for n in self._notificadores:
            n.notificar(mensagem)
