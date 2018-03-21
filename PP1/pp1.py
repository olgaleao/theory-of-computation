#!/usr/bin/python
import re

class Fiscalizacao:
    def __init__(self, id_cliente, id_empresa, data_transacao, hora_transacao, preco_transacao, cod_transacao):
        self.id_cliente = id_cliente
        self.id_empresa = id_empresa
        self.cod_transacao = cod_transacao
        self.data_transacao = data_transacao
        self.hora_transacao = hora_transacao
        self.preco_transacao = preco_transacao

    def validarCPF(self, cpf):
        v = [int(x) for x in cpf if x.isdigit()]
        v_comp = v[::-1][2:]
        v1, v2 = 0, 0
        for i in range(len(v_comp)):
            v1 += v_comp[i]*(9 - (i%10))
            v2 += v_comp[i]*(9 - ((i+1)%10))
        v1 = (v1%11)%10
        v2 = ((v2+(v1*9))%11)%10

        return v[-2]==v1 and v[-1]==v2

    def validarCNPJ(self, cnpj):
        a = [int(x) for x in cnpj if x.isdigit()]
        v = a[:-2]
        v1, v2 = 0, 0
        pesos = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        for i in range(len(v)):
            v1 += v[i]*pesos[i]

        v1, resto = v1/11, v1%11
        if resto < 2:
            v1 = 0
        else:
            v1 = 11 - resto

        v.append(v1)
        pesos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
        for i in range(len(v)):
            v2 += v[i]*pesos[i]

        v2, resto = v2/11, v2%11
        if resto < 2:
            v2 = 0
        else:
            v2 = 11 - resto

        return a[-2]==v1 and a[-1]==v2


    def verificarCPF(self, cpf):
        match = re.search(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf)
        return match != None and self.validarCPF(cpf)

    def verificarCNPJ(self, cnpj):
        match = re.search(r'^\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2}$', cnpj)
        return match != None and self.validarCNPJ(cnpj)

    def verificarIdCliente(self):
        return self.verificarCPF(self.id_cliente)

    def verificarIdEmpresa(self):
        if len(self.id_empresa) == 15:
            return self.verificarCPF(self.id_empresa)
        else:
            return self.verificarCNPJ(self.id_empresa)

    def verificarData(self):
        match_data = re.search(r'^(\d{4})\.(0[1-9])|(1[12])\.((0[1-9])|([12]\d)|(3[01]))$', self.data_transacao)
        match_horario = re.search(r'^(([01]\d)|(2[0-3])):([0-5]\d):([0-5]\d)$', self.hora_transacao)

        return match_data != None and match_horario != None

    def verificarPrecos(self):
        match = re.search(r'^\[((\d)+\.\d{2})(,(\d)+\.(\d{2}))*\]$', self.preco_transacao)
        return match != None

    def verificarCodigo(self):
        match = re.search(r'^\d{9}-([0-9a-z])(?!\1)([0-9a-z])(?!\1|\2)([0-9a-z])(?!\1|\2|\3)([0-9a-z])(?!\1|\2|\3|\4)([0-9a-z])-([02468]{3})(-[01]{3})?$', self.cod_transacao)
        return match != None

    def displayIdCliente(self):
        print(self.id_cliente)

    def displayIdEmpresa(self):
        print(self.id_empresa)

    def displayCodigoTransacao(self):
        print(self.cod_transacao)

    def displayDataTransacao(self):
        print(self.data_transacao)

    def displayHoraTransacao(self):
        print(self.hora_transacao)

    def displayPrecoTransacao(self):
        print(self.preco_transacao)

try:
    nota_fiscal = Fiscalizacao(*[x for x in input().split()])
    print(nota_fiscal.verificarIdCliente() and nota_fiscal.verificarIdEmpresa() and nota_fiscal.verificarData() and nota_fiscal.verificarPrecos() and nota_fiscal.verificarCodigo())
except EOFError:
    print(True)
