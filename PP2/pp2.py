class Automato:

    def __init__(self, dict):
        self.estados = dict['estados']
        self.estado_inicial = dict['inicial']
        self.estados_finais = sorted(dict['final'])
        self.delta = dict['delta']
        self.delta = self.ordena_delta()
        self.pi, self.eta = [], []
        self.letra_a, self.letra_b = [], []
        self.criar_vetores_coluna()
        self.pi = self.transpor_pi()
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

    def ordena_delta(self):
        m = self.delta
        for i in range(len(self.delta)):
            m[i].sort()
        return m

    def transpor_pi(self):
        m = []
        m.append([self.pi[i][0] for i in range(len(self.pi))])
        return m

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

    def multiplicacao_matrizes(self, f, s):
        n_linha, n_coluna = len(f), len(s[0])
        prod = []
        for i in range(n_linha):
            linha = []
            for j in range(n_coluna):
                ans = 0
                for k in range(len(s)):
                    x = f[i][k]
                    y = s[k][j]
                    ans += x*y
                linha.append(ans)
            prod.append(linha)
        return prod

#lendo a entrada
dict = Automato(eval(input()))
n = int(input())
for i in range(n):
    s = input()
    if s[0] is 'a':
        ans = dict.multiplicacao_matrizes(dict.pi, dict.letra_a)
    elif s[0] is 'b':
        ans = dict.multiplicacao_matrizes(dict.pi, dict.letra_b)

    for j in range(1, len(s)):
        if s[j] is 'a':
            ans = dict.multiplicacao_matrizes(ans, dict.letra_a)
        elif s[j] is 'b':
            ans = dict.multiplicacao_matrizes(ans, dict.letra_b)

    ans = dict.multiplicacao_matrizes(ans, dict.eta)
    if(ans[0][0] == 1):
        print("ACEITA")
    else:
        print("REJEITA")
