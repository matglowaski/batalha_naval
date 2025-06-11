import random


def criar_tabuleiro():
    return [["🌊" for _ in range(10)] for _ in range(5)
]

def mostrar_tab(tabuleiro):
    for linha in tabuleiro:
        print(" ".join(linha))
    print()


def posicionar_barcos(tabuleiro, qtd=4):
    barcos = []
    while len(barcos) < qtd:
        numerobarco = len(barcos)
        print(f"Posicione o {numerobarco + 1}º barco:")

        while True:
            try:
                linha = int(input(f"Digite a linha do barco {numerobarco + 1} (0 a 4): "))
                coluna = int(input(f"Digite a coluna do barco {numerobarco + 1} (0 a 9): "))
                if 0 <= linha <= 4 and 0 <= coluna <= 9:
                    break
                else:
                    print("Coordenada inválida, digite outra.")
            except ValueError:
                print("Coordenada inválida, tente novamente.")

        if [linha, coluna] not in barcos:
            barcos.append([linha, coluna])
            tabuleiro[linha][coluna] = "🚢"
        else:
            print("Você já colocou um barco nessa posição.")
    return barcos


def posicionar_barcos_pc(qtd):
    barcos = []
    while len(barcos) < qtd:
        linha = random.randint(0, 4)
        coluna = random.randint(0, 9)
        if [linha, coluna] not in barcos:
            barcos.append([linha, coluna])
    return barcos


def jogar():
    jogador_tab = criar_tabuleiro()
    pc_tab_mostrar = criar_tabuleiro()
    pc_barcos_tab = criar_tabuleiro()

    print("--- POSICIONE SEUS BARCOS ---")
    jogador_barcos = posicionar_barcos(jogador_tab, 5)
    pc_barcos = posicionar_barcos_pc(5)

    for linha, coluna in pc_barcos:
        pc_barcos_tab[linha][coluna] = "🚢"

    jogador_pontuacao = 5
    pc_pontuacao = 5

    ataques_jogador = []

    while jogador_pontuacao > 0 and pc_pontuacao > 0:
        print("--- SEU TABULEIRO ---")
        mostrar_tab(jogador_tab)

        print("--- TABULEIRO DO PC ---")
        mostrar_tab(pc_tab_mostrar)

        print("Sua vez de atacar!")
        while True:
            try:
                linha = int(input("Linha (0 a 4): "))
                coluna = int(input("Coluna (0 a 9): "))
                if not (0 <= linha <= 4 and 0 <= coluna <= 9):
                    print("Coordenada inválida, digite outra.")
                    continue
                if [linha, coluna] in ataques_jogador:
                    print("Você já atacou essa posição. Tente novamente.")
                    continue
                break
            except ValueError:
                print("Coordenada inválida, tente novamente.")

        ataques_jogador.append([linha, coluna])

        if [linha, coluna] in pc_barcos:
            print("🔥 BOOOM! Você acertou um navio!")
            pc_tab_mostrar[linha][coluna] = "🔥"
            pc_barcos.remove([linha, coluna])
            pc_pontuacao -= 1
        else:
            print("❌ Água... nada ali.")
            pc_tab_mostrar[linha][coluna] = "❌"

        if pc_pontuacao == 0:
            print("\n💥 Você venceu! Afundou todos os navios do PC!")
            break

        print("--- VEZ DO COMPUTADOR ---")
        while True:
            linha = random.randint(0, 4)
            coluna = random.randint(0, 9)
            if jogador_tab[linha][coluna] not in ["🔥", "❌"]:
                break
        print(f"O computador atacou ({linha}, {coluna})")

        if [linha, coluna] in jogador_barcos:
            print("🔥 O computador acertou um navio seu!")
            jogador_tab[linha][coluna] = "🔥"
            jogador_barcos.remove([linha, coluna])
            jogador_pontuacao -= 1
        else:
            print("❌ O computador errou!")
            if jogador_tab[linha][coluna] == "🌊":
                jogador_tab[linha][coluna] = "❌"

        if jogador_pontuacao == 0:
            print("💀 Você perdeu! Seus navios foram todos afundados.")
            break

    print("Obrigado por jogar nossa versão de Batalha Naval.")
    print("Desenvolvido por Julio Cezar e Matheus Glowaski")



jogar()