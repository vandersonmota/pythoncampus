# -*- encoding: iso-8859-1 -*-

# Criacao...: 24/09/2006
# Tecnico...: Marinho Brandão
# Tipos de campos apropriados para a realidade brasileira

import re
from django.db import models
from django import forms
from django.core import validators

PESSOA_SEXO = (('M','Masculino'), ('F','Feminino'), )
CIDADE_ESTADO = (('RS', 'Rio Grande do Sul'), 
                 ('PR', 'Parana'), 
                 ('SC', 'Santa Catarina'),
                 ('SP', 'Sao Paulo'), 
                 ('RJ', 'Rio de Janeiro'), 
                 ('MG', 'Minas Gerais'), 
                 ('ES', 'Espirito Santo'), 
                 ('GO', 'Goias'), 
                 ('MS', 'Mato Grosso do Sul'), 
                 ('MT', 'Mato Grosso'), 
                 ('DF', 'Distrito Federal'), 
                 ('TO', 'Tocantins'), 
                 ('PA', 'Para'), 
                 ('AM', 'Amazonas'), 
                 ('AC', 'Acre'), 
                 ('RO', 'Rondonia'), 
                 ('RR', 'Roraima'), 
                 ('AP', 'Amapa'), 
                 ('BA', 'Bahia'), 
                 ('SE', 'Sergipe'), 
                 ('AL', 'Alagoas'), 
                 ('PE', 'Pernambuco'), 
                 ('PB', 'Paraiba'), 
                 ('RN', 'Rio Grande do Norte'), 
                 ('CE', 'Ceara'), 
                 ('PI', 'Piaui'), 
                 ('MA', 'Maranhao'), )

# Expressoes de validação
expressao_cep = r'^[0-9]{5}[-][0-9]{3}$'
expressao_cpf = r'^[0-9]{3}[.][0-9]{3}[.][0-9]{3}[-][0-9]{2}$'
expressao_cnpj = r'^[0-9]{2}[.][0-9]{3}[.][0-9]{3}[/][0-9]{4}[-][0-9]{2}$'
#expressao_cnpj_re = re.compile(expressao_cnpj, re.IGNORECASE)


# -------------------------------------------------
# http://www.pythonbrasil.com.br/moin.cgi/VerificadorDeCnpj
class CNPJ(object):
    def __init__(self, cnpj):
        """Classe representando um número de CNPJ
        >>> a = CNPJ('11222333000181')
        >>> b = CNPJ('11.222.333/0001-81')
        >>> c = CNPJ([1, 1, 2, 2, 2, 3, 3, 3, 0, 0, 0, 1, 8, 2])
        """
        try:
            basestring
        except:
            basestring = (str, unicode)

        if isinstance(cnpj, basestring):
            if not cnpj.isdigit():
                cnpj = cnpj.replace(".", "")
                cnpj = cnpj.replace("-", "")
                cnpj = cnpj.replace("/", "")

            if not cnpj.isdigit:
                raise ValueError("Valor não segue a forma xx.xxx.xxx/xxxx-xx")

        if len(cnpj) < 14:
            raise ValueError("O número de CNPJ deve ter 14 digítos")
        
        self.cnpj = map(int, cnpj)

    
    def __getitem__(self, index):
        """Retorna o dígito em index como string"""
        return str(self.cnpj[index])
    
    def __repr__(self):
        """Retorna uma representação 'real'"""
        return "CNPJ('%s')" % ''.join([str(x) for x in self.cnpj])
    
    def __eq__(self, other):
        """Provê teste de igualdade para números de CNPJ"""
        if isinstance(other, CNPJ):
            return self.cnpj == other.cnpj
        return False

    def __str__(self):
        """Retorna uma string do CNPJ na forma com pontos e traço"""
        d = ((2, "."), (6, "."), (10, "/"), (15, "-"))
        s = map(str, self.cnpj)
        for i, v in d:
            s.insert(i, v)
        r = ''.join(s)
        return r

    def valido(self):
        """Valida o número de cnpj"""
        cnpj = self.cnpj[:12]
        prod = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

        # pegamos apenas os 9 primeiros dígitos do cpf e geramos os
        # dois dígitos que faltam
        while len(cnpj) < 14:
            r = sum([x*y for (x, y) in zip(cnpj, prod)])%11

            if r > 1: f = 11 - r
            else: f = 0
                
            cnpj.append(f)
            prod.insert(0, 6)

        # se o número com os digítos faltantes coincidir com o número
        # original, então ele é válido
        return bool(cnpj == self.cnpj)
# -------------------------------------------------

# http://www.pythonbrasil.com.br/moin.cgi/VerificadorDeCpf
class CPF(object):
    def __init__(self, cpf):
        """Classe representando um número de CPF"""
        try:
            basestring
        except:
            basestring = (str, unicode)

        if isinstance(cpf, basestring):
            cpf = cpf.replace(".", "")
            cpf = cpf.replace("-", "")
            if not cpf.isdigit():
                raise ValueError("Valor não segue a forma xxx.xxx.xxx-xx")

        if len(cpf) < 11:
            raise ValueError("O número de CPF deve ter 11 digítos")

        self.cpf = map(int, cpf)


    def __getitem__(self, index):
        """Retorna o dígito em index como string"""
        return str(self.cpf[index])

    def __repr__(self):
        """Retorna uma representação 'real', ou seja:"""
        return "CPF('%s')" % ''.join([str(x) for x in self.cpf])

    def __eq__(self, other):
        """Provê teste de igualdade para números de CPF"""
        if isinstance(other, CPF):
            return self.cpf == other.cpf
        return False

    def __str__(self):
        """Retorna uma string do CPF na forma com pontos e traço"""
        d = ((3, "."), (7, "."), (11, "-"))
        s = map(str, self.cpf)
        for i, v in d:
            s.insert(i, v)
        r = ''.join(s)
        return r

    def valido(self):
        """Valida o número de cpf"""
        cpf = self.cpf[:9]
        # pegamos apenas os 9 primeiros dígitos do cpf e geramos os
        # dois dígitos que faltam
        while len(cpf) < 11:

            r = sum(map(lambda(i,v):(len(cpf)+1-i)*v,enumerate(cpf))) % 11

            if r > 1:
                f = 11 - r
            else:
                f = 0
            cpf.append(f)

        # se o número com os digítos faltantes coincidir com o número
        # original, então ele é válido
        return bool(cpf == self.cpf)

    def __nonzero__(self):
        """Valida o número de cpf"""

        return self.valido()
# -------------------------------------------------


class Manipulador_CepField(forms.TextField):
    def __init__(self, field_name, is_required=False, validator_list=None, maxlength=9):
        if validator_list is None: validator_list = []
        validator_list = [self.formatoValido] + validator_list
        forms.TextField.__init__(self, field_name, length=9, maxlength=maxlength,
            is_required=is_required, validator_list=validator_list)

    def formatoValido(self, field_data, all_data):
        exp = re.compile(expressao_cep, re.IGNORECASE)
        if not len(exp.findall(field_data)):
            raise validators.ValidationError(u"CEP tem formato inválido. O correto é (99999-999)")

class CepField(models.CharField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        models.CharField.__init__(self, verbose_name, name, maxlength=9, **kwargs)

    def get_internal_type(self):
        return 'CharField'

    def get_manipulator_field_objs(self):
        return [Manipulador_CepField]

# -------------------------------------------------

class EstadoBrasileiroField(models.CharField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        models.CharField.__init__(self, verbose_name, name, maxlength = 2, choices=CIDADE_ESTADO, **kwargs)

    def get_internal_type(self):
        return 'CharField'

# -------------------------------------------------

class SexoField(models.CharField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        models.CharField.__init__(self, verbose_name, name, maxlength = 1, choices=PESSOA_SEXO, **kwargs)

    def get_internal_type(self):
        return 'CharField'

# -------------------------------------------------

class Manipulador_CpfField(forms.TextField):
    def __init__(self, field_name, is_required=False, validator_list=None, maxlength=14):
        if validator_list is None: validator_list = []
        validator_list = [self.formatoValido, self.cpfValido] + validator_list
        forms.TextField.__init__(self, field_name, length=9, maxlength=maxlength,
            is_required=is_required, validator_list=validator_list)

    def formatoValido(self, field_data, all_data):
        exp = re.compile(expressao_cpf, re.IGNORECASE)
        if not len(exp.findall(field_data)):
            raise validators.ValidationError(u"CPF tem formato inválido. O correto é (999.999.999-99)")

    def cpfValido(self, field_data, all_data):
        try:
            cpf = CPF(field_data)
            if not cpf.valido():
                raise validators.ValidationError(u"CPF inválido.")
        except:
            raise validators.ValidationError(sys.exc_info()[0])

class CpfField(models.CharField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        models.CharField.__init__(self, verbose_name, name, maxlength = 14, **kwargs)

    def get_internal_type(self):
        return 'CharField'

    def get_manipulator_field_objs(self):
        return [Manipulador_CpfField]

# -------------------------------------------------

class Manipulador_CnpjField(forms.TextField):
    def __init__(self, field_name, is_required=False, validator_list=None, maxlength=18):
        if validator_list is None: validator_list = []
        validator_list = [self.formatoValido, self.cnpjValido] + validator_list
        forms.TextField.__init__(self, field_name, length=18, maxlength=maxlength,
            is_required=is_required, validator_list=validator_list)

    def formatoValido(self, field_data, all_data):
        exp = re.compile(expressao_cnpj, re.IGNORECASE)
        if not len(exp.findall(field_data)):
            raise validators.ValidationError(u"CNPJ tem formato inválido. O correto é (99.999.999/9999-99)")

    def cnpjValido(self, field_data, all_data):
        try:
            cnpj = CNPJ(field_data)
            if not cnpj.valido():
                raise validators.ValidationError(u"CNPJ inválido.")
        except:
            raise validators.ValidationError(sys.exc_info()[0])

class CnpjField(models.CharField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        models.CharField.__init__(self, verbose_name, name, maxlength = 18, **kwargs)

    def get_internal_type(self):
        return 'CharField'

    def get_manipulator_field_objs(self):
        return [Manipulador_CnpjField]

# -------------------------------------------------

class Manipulador_CnpjCpfField(forms.TextField):
    def __init__(self, field_name, is_required=False, validator_list=None, maxlength=18):
        if validator_list is None: validator_list = []
        validator_list = [self.formatoValido, self.cnpjCpfValido] + validator_list
        forms.TextField.__init__(self, field_name, length=18, maxlength=maxlength,
            is_required=is_required, validator_list=validator_list)

    def formatoValido(self, field_data, all_data):
        exp_cnpj = re.compile(expressao_cnpj, re.IGNORECASE)
        exp_cpf = re.compile(expressao_cpf, re.IGNORECASE)

        if not len(exp_cnpj.findall(field_data)) and not len(exp_cpf.findall(field_data)):
            raise validators.ValidationError(u"CNPJ ou CPF tem formato inválido. O correto é (999.999.999-99) ou (99.999.999/9999-99)")

    def cnpjValido(self, field_data, all_data):
        try:
            cnpj = CNPJ(field_data)
            return cnpj.valido()
        except:
            return False

    def cpfValido(self, field_data, all_data):
        try:
            cpf = CPF(field_data)
            return cpf.valido()
        except:
            return False

    def cnpjCpfValido(self, field_data, all_data):
        if not self.cnpjValido(field_data, all_data) and not self.cpfValido(field_data, all_data):
            raise validators.ValidationError(u"CNPJ ou CPF inválido.")

class CnpjCpfField(models.CharField):
    def __init__(self, verbose_name=None, name=None, **kwargs):
        models.CharField.__init__(self, verbose_name, name, maxlength = 18, **kwargs)

    def get_internal_type(self):
        return 'CharField'

    def get_manipulator_field_objs(self):
        return [Manipulador_CnpjCpfField]

