# -*- coding: utf-8 -*-

from django.test import TestCase
from models import Inscrito, MiniEvento, Ministrante

from os import path
from django.test.client import Client
from windmill.authoring import djangotest

#This is only to have pyhistorian integration
class WindmillStoryRunner(djangotest.WindmillDjangoUnitTest):
    test_dir = path.join(path.dirname(path.abspath(__file__)),"stories")
    browser = "firefox"


class InscricaoEmMinicurso(TestCase):

    def setUp(self):
        ministrante_grok = Ministrante.objects.create(nome='Gustavo Rezende', descricao='Mó patinho no DOTA',
                                                           site = 'http://nsigustavo.blogspot.com')

        self.minicurso_grok = MiniEvento.objects.create(nome='Aprendendo Grok', descricao='Um curso fácil de grok',
                                                        publico_alvo='Masoquistas', ministrante=ministrante_grok,
                                                        data='2012-12-12', horario='16:00:00',
                                                        local='Laboratório 01', tipo='minicurso', vagas_disponiveis=1)

        self.jim_fulton = Inscrito.objects.create(nome='Jim Fulton', instituicao='Zope Corporation',cpf='12345678910')

    def test_cadastrar_1_no_minicurso(self):
        self.jim_fulton.inscrever(self.minicurso_grok)
        self.assertEquals(0, self.minicurso_grok.vagas_disponiveis)

    def test_cadastrar_2_no_minicurso(self):
        martin_aspeli = Inscrito.objects.create(nome='Martin Aspeli', instituicao='Plone Foundation',cpf='12345678911')

        self.jim_fulton.inscrever(self.minicurso_grok)
        try:
            martin_aspeli.inscrever(self.minicurso_grok)
            self.fail('Limite de vagas do minicurso não respeitado')
        except:
            pass

        self.assertEquals(0, len(martin_aspeli.minicurso.all()))

