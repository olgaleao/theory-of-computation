class Automato:

    def __init__(self, dict):
        self.estados = dict['estados']
        self.estado_inicial = dict['inicial']
        self.estados_finais = sorted(dict['final'])
        self.delta = dict['delta']
        self.pi, self.eta = [], []
        self.letra_a, self.letra_b = [], []
        self.criar_vetores_coluna()
        self.criar_alfabeto()

    def criar_vetores_coluna(self):
        for i in range(self.estados):
            pi_temp, eta_temp = [], []
            if(i == self.estado_inicial):
                pi_temp.append(1)
            else:
                pi_temp.append(0)
            if(i in self.estados_finais):
                eta_temp.append(1)
            else:
                eta_temp.append(0)
            self.eta.append(eta_temp)
            self.pi.append(pi_temp)

    def criar_alfabeto(self):
        for i in range(self.estados):
            letraA_temp, letraB_temp = [], []
            for j in range(self.estados):
                letraA_temp.append(0)
                letraB_temp.append(0)
            self.letra_a.append(letraA_temp)
            self.letra_b.append(letraB_temp)

        for i in range(self.estados):
            self.letra_a[i][self.delta[i][0]] = 1
            self.letra_b[i][self.delta[i][1]] = 1


#lendo a entrada
dict = Automato(eval(input()))

n = int(input())
