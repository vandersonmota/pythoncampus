# -*- coding: utf-8 -*-
from django.db import models

TIPO_MINI_EVENTO = (
    ('palestra','Palestra'),
    ('minicurso','Minicurso')
    )

class MiniEvento(models.Model):
    nome = models.CharField('Nome',max_length=100)
    descricao = models.TextField('Descriçao',max_length=500)
    publico_alvo = models.CharField('Publico Alvo',max_length=50)
    ministrante = models.ForeignKey('Ministrante',)
    data = models.DateField('Data')
    horario = models.TimeField('Horario')
    local = models.CharField('Local',max_length=50)
    tipo = models.CharField('Tipo',choices=TIPO_MINI_EVENTO, max_length=10)
    vagas_disponiveis = models.IntegerField('Numero de Vagas',default=0)
    participantes = models.ManyToManyField('Inscrito',blank=True)
    
    def __unicode__(self):
        return self.nome


    def _disponivel(self):
        if self.vagas_disponiveis >= 1:
            return True
        return False

    def registrar_participante(self, participante):
        if self._disponivel():
            self.participantes.add(participante)
            self.vagas_disponiveis -= 1
        else:
            raise Exception('Não há vagas')

class Inscrito(models.Model):
    ESTADOS = (('pendente', 'Pendente'),
              ('confirmado', 'Confirmado'),
              ('espera', 'Espera'))
    
    nome = models.CharField('Nome',max_length=100)
    instituicao = models.CharField('Instituição',max_length=100)
    cpf = models.CharField('CPF',max_length=14,unique=True)
    minicurso = models.ManyToManyField('MiniEvento', limit_choices_to={'tipo':'minicurso'},
                                       blank=True, null=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendente')
    
    def __unicode__(self):
        return self.nome

    def inscrever(self, minicurso):
        minicurso.registrar_participante(self)
        self.minicurso.add(minicurso)
        
        


class Ministrante(models.Model):
    nome = models.CharField('Nome',max_length=100)
    descricao = models.TextField('Quem é',max_length=500)
    site = models.URLField('Site/Blog', blank=True, null=True)
    
    def __unicode__(self):
        return self.nome

