"""
1 -> Criar arquivo txt que será o banco de palavras. F
2 -> Criar a lista (desenho/tabuleiro). F
3 -> Criar uma classe jogoDaForca com os atributos e métodos.
    Atributos - palavra, letras erradas, letras certas F
    Métodos - Adicionar letras erradas e certas na lista F
              Mostrar a letra no tabuleiro F
              Verificar se o jogo terminou (6 erros ou Jogador venceu) F
                    Game over
                    Player win
              Status do jogo (também mostrar desenho)
4 -> Pegar uma palavra aleatorica do banco de palavras
5 -> Criar o objeto da classe jogoDaForca dentro de uma função main()
    Função main - Pedir uma letra ao usuário
                  Mostrar o status do jogo
                  Mostrar se perdeu ou ganhou
6 -> Executar o main()
"""

# Importar o random para palavra aleatória
import random

print('>>>>>Seja bem-vindo<<<<<')

# Desenhos do jogo
desenhos = ['''
+---+
|   |
    |
    |
    |
    |
=========''', '''
+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe do jogo
class HangmanGame:
    # Atributos (constructor)
    def __init__(self, word):
        self.word = word
        self.wrong_letters = []
        self.correct_letters = []

    # Adicionar palavras em suas respectivas listas
    def add_letters(self, letter):
        if letter in self.word and letter not in self.correct_letters:
            self.correct_letters.append(letter)
        elif letter not in self.word and letter not in self.wrong_letters:
            self.wrong_letters.append(letter)
        else:
            return False
        return True

    # Mostrar letra no tabuleiro
    def show_letter(self):
        hidden_letter = ''
        for letter in self.word:
            if letter not in self.correct_letters:
                hidden_letter += '_'
            else:
                hidden_letter += letter
        return hidden_letter

    # Verificar fim de jogo
    def game_over(self):
        return self.player_win() or (len(self.wrong_letters) == 6)

    # Verificar se jogador ganhou
    def player_win(self):
        if '_' not in self.show_letter():
            return True
        return False

    # Status do jogo
    def game_status(self):
        print('-=-=-=-=-=-=-=-=-=-')
        print(desenhos[len(self.wrong_letters)])
        print('\nA palavra é: ' + self.show_letter())
        print('\nLetras erradas: ', )
        for letter in self.wrong_letters:
            print(letter,)
        print('-=-=-=-=-=-=-=-=-=-')


# Função para ler uma palavra de forma aleatória do banco de palavras
def random_word():
    with open("palavras_easy.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Criar objetivo dentro de uma função main
def main():
    # Objeto criado
    hangman = HangmanGame(random_word())

    # Solicitar letra e mostrar status para o jogador
    while not hangman.game_over():
        hangman.game_status()
        letter = input('Digite uma letra: ')
        hangman.add_letters(letter)

    # Verifica status do jogo e define se ganhou ou perdeu
    hangman.game_status()

    if hangman.player_win():
        print('\nParabéns, você venceu!')
    else:
        print(f'\nVocê perdeu! A palavra era {hangman.word.upper()}')


# Executa a função main
if __name__ == "__main__":
    main()
