import ast

entrada = ast.literal_eval(input())
qtd = int(input())

inicial, aceita = entrada['inicial'], entrada['aceita']

for i in range(qtd):
    palavra = list('b' + input() + 'b')

    x, u, ans, j, hadelta = inicial, palavra[0], [], 1, True

    while x != aceita and hadelta:
        hadelta = False
        for d in entrada['delta']:
            if d[0] == x and d[2] == palavra[j]:
                y, v, w = d[1], d[3], d[4]
                palavra[j], x, hadelta = v, y, True
                if w == 'D':
                    j += 1
                elif w == 'E':
                    j -= 1
                break
        if not hadelta:
            break
    palavra = ''.join(palavra[1:len(palavra)-1])
    if x == aceita:
        print(palavra, "ACEITA")
    else:
        print(palavra, "REJEITA")