from q1_midias import Plataforma, Video, Podcast, TextoNarrado
from q2_funcionarios import Empresa, FuncionarioAssalariado, FuncionarioHorista, FuncionarioComissionado
from q3_notificacoes import CentralNotificacoes, NotificadorEmail, NotificadorSMS, NotificadorApp
from q4_impressao import Boleto, Etiqueta, RelatorioSimples, processar_impressao
from q5_armazenamento import (
    ArmazenadorArquivo, ArmazenadorBanco, ArmazenadorNuvem,
    executar_salvamento_formal, executar_salvamento_flexivel
)

def testar_q1():
    print("\n========== QUESTÃO 1 ==========")
    streaming = Plataforma("UfamPlay")
    
    vid = Video("Aula de POO", 120, "1080p")
    pod = Podcast("Tech Cast", 45, "Marcos Eduardo")
    txt = TextoNarrado("Resumo Sistemas", 15, "PT-BR")
    
    streaming.adicionar_midia(vid)
    streaming.adicionar_midia(pod)
    streaming.adicionar_midia(txt)
    
    streaming.listar_midias()
    streaming.reproduzir_todas()

def testar_q2():
    print("\n========== QUESTÃO 2 ==========")
    empresa = Empresa("Inova Tech")
    
    f1 = FuncionarioAssalariado("Marcos", "123.456.789-00", 3500.00)
    f2 = FuncionarioHorista("Aline", "987.654.321-11", 40, 50.00)
    f3 = FuncionarioComissionado("Bruno", "456.123.789-22", 50000.00, 0.05)
    
    empresa.adicionar_funcionario(f1)
    empresa.adicionar_funcionario(f2)
    empresa.adicionar_funcionario(f3)
    
    empresa.listar_funcionarios()
    empresa.mostrar_folha_pagamento()

def testar_q3():
    print("\n========== QUESTÃO 3 ==========")
    central = CentralNotificacoes()
    central.adicionar_notificador(NotificadorEmail())
    central.adicionar_notificador(NotificadorSMS())
    central.adicionar_notificador(NotificadorApp())
    
    central.enviar_para_todos("O prazo final da lista é hoje às 16:00!")

def testar_q4():
    print("\n========== QUESTÃO 4 ==========")
    boleto = Boleto("00192.37482", 250.50)
    etiqueta = Etiqueta("Agnes", "Av. Principal, 123")
    relatorio = RelatorioSimples("Desempenho Semestral")
    
    processar_impressao(boleto)
    processar_impressao(etiqueta)
    processar_impressao(relatorio)

def testar_q5():
    print("\n========== QUESTÃO 5 ==========")
    arq = ArmazenadorArquivo()
    banco = ArmazenadorBanco()
    nuvem = ArmazenadorNuvem()
    
    dado = "Dados_Do_Sistema"
    
    # Testando o salvamento formal (Exige ABC)
    executar_salvamento_formal(arq, dado)
    executar_salvamento_formal(banco, dado)
    # executar_salvamento_formal(nuvem, dado)  <- Erro de tipo estático (Não herda de Armazenador)
    
    # Testando o salvamento flexível (Exige apenas a assinatura/Protocol)
    print("\n--- Teste Flexível (Protocol) ---")
    executar_salvamento_flexivel(arq, dado)
    executar_salvamento_flexivel(banco, dado)
    executar_salvamento_flexivel(nuvem, dado) # Funciona perfeitamente!

if __name__ == "__main__":
    testar_q1()
    testar_q2()
    testar_q3()
    testar_q4()
    testar_q5()
