# -*- coding:utf-8 -*-
from pyhistorian import *
from windmill.authoring import WindmillTestClient

class HistoriaInscricao(Historia):
    """Como um visitante
    Eu quero me inscrever nos minicursos
    Para que eu possa aprender mais"""


class CenarioVisitanteSeInscreve(Cenario):

    @DadoQue('Estou na paǵina de inscrições')
    def abrir_pagina_principal(self):
        self.navegador = WindmillTestClient(__name__)
        self.navegador.open(url='/inscricoes/')

    @Quando("eu clico em 'Quero me inscrever'")
    def clicar_em_quero_me_inscrever(self):
        self.navegador.click(id='inscrever')

    @Quando("eu entro com todos os meus dados")
    def entrar_dados(self):
        pass

    @Quando("eu clico em 'Salvar'")
    def clicar_em_salvar(self):
        pass

    @Entao("a mensagem 'Participante inserido com sucesso' deverá aparecer")
    def mensagem_sucesso(self):
        pass

