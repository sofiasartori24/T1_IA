# Função para verificar o resultado do jogo da velha
def verifica_resultado(tabuleiro):
    # Verifica linhas e colunas
    for i in range(3):
        if tabuleiro[i][0] == tabuleiro[i][1] == tabuleiro[i][2] != 'b':
            return tabuleiro[i][0] + "wins"
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] != 'b':
            return tabuleiro[0][i] + "wins"
    # Verifica diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != 'b':
        return tabuleiro[0][0] + "wins"
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != 'b':
        return tabuleiro[0][2] + "wins"
    # Verifica empate
    if all([pos != 'b' for linha in tabuleiro for pos in linha]):
        return "Draw"
    return "inGame"

# Função para gerar todas as possíveis posições do jogo da velha
def gerar_posicoes():
    posicoes = []
    for p1 in ['x', 'o', 'b']:
        for p2 in ['x', 'o', 'b']:
            for p3 in ['x', 'o', 'b']:
                for p4 in ['x', 'o', 'b']:
                    for p5 in ['x', 'o', 'b']:
                        for p6 in ['x', 'o', 'b']:
                            for p7 in ['x', 'o', 'b']:
                                for p8 in ['x', 'o', 'b']:
                                    for p9 in ['x', 'o', 'b']:
                                        tabuleiro = [[p1, p2, p3], [p4, p5, p6], [p7, p8, p9]]
                                        resultado = verifica_resultado(tabuleiro)
                                        posicao = ','.join([p1, p2, p3, p4, p5, p6, p7, p8, p9]) + ',' + resultado
                                        posicoes.append(posicao)
    return posicoes

# Escrever as posições geradas em um arquivo
def escrever_em_arquivo(posicoes, nome_arquivo):
    with open(nome_arquivo, 'w') as f:
        for posicao in posicoes:
            f.write(posicao + '\n')

# Gerar todas as posições
posicoes = gerar_posicoes()

# Escrever as posições no arquivo 'tic-tac-toe.data'
escrever_em_arquivo(posicoes, 'tic-tac-toe.data')

print("Arquivo 'tic-tac-toe.data' criado com sucesso!")
