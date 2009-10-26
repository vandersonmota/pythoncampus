# -*- coding: utf-8 -*-

from django.test import TestCase
from models import Inscrito, DadosMiniEvento, Ministrante, MiniCurso

from os import path
from django.test.client import Client
from windmill.authoring import djangotest

      
    

class InscricaoEmMinicurso(TestCase):

    def setUp(self):
        ministrante_grok = Ministrante.objects.create(nome='Gustavo Rezende', descricao='Mó patinho no DOTA',
                                                           site = 'http://nsigustavo.blogspot.com')

        dados_minievento = DadosMiniEvento.objects.create(nome='Aprendendo Grok', descricao='Um curso fácil de grok',
                                                        publico_alvo='Masoquistas', data='2012-12-12',
                                                        horario='16:00:00', local='Laboratório 01',)
        
        self.minicurso_grok = MiniCurso.objects.create(minievento = dados_minievento, ministrante=ministrante_grok,
                                                       vagas_disponiveis=1)

        self.jim_fulton = Inscrito.objects.create(nome='Jim Fulton', instituicao='Zope Corporation',cpf='12345678910')

    def test_cadastrar_1_no_minicurso(self):
        self.jim_fulton.inscrever(self.minicurso_grok)
        self.assertEquals(0, self.minicurso_grok.vagas_disponiveis)
        
    def test_cadastrar_2_no_minicurso(self):
        martin_aspeli = Inscrito.objects.create(nome='Martin Aspeli', instituicao='Plone Foundation',cpf='12345678911')

        self.jim_fulton.inscrever(self.minicurso_grok)
        martin_aspeli.inscrever(self.minicurso_grok)        
        
        self.assertEquals('espera', martin_aspeli.estado)

