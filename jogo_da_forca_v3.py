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
              Status do jogo (também mostrar desenho) F
4 -> Pegar uma palavra aleatorica do banco de palavras F
5 -> Criar o objeto da classe jogoDaForca dentro de uma função main() F
    Função main - Pedir uma letra ao usuário F
                  Mostrar o status do jogo
                  Mostrar se perdeu ou ganhou
6 -> Executar o main() F

Extra: Criar níveis (fácil e difícil)
"""

# Importar o random para palavra aleatória
import random

print('>>>>>Seja bem-vindo<<<<<')

# Desenhos do jogo fácil
desenhos_easy = ['''
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

# Desenhos do jogo difícil
desenhos_hard = ['''
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
/|\  |
     |
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

    # Verificar fim de jogo fácil
    def game_over_easy(self):
        return self.player_win() or (len(self.wrong_letters) == 6)

    # Verificar fim de jogo difícil
    # Palavras mais difíceis e 4 chances
    def game_over_hard(self):
        return self.player_win() or (len(self.wrong_letters) == 4)

    # Verificar se jogador ganhou
    def player_win(self):
        if '_' not in self.show_letter():
            return True
        return False

    # Status do jogo fácil
    def game_status_easy(self):
        print('-=-=-=-=-=-=-=-=-=-')
        print(desenhos_easy[len(self.wrong_letters)])
        print('\nA palavra é: ' + self.show_letter())
        print('\nLetras erradas: ', )
        for letter in self.wrong_letters:
            print(letter,)
        print('-=-=-=-=-=-=-=-=-=-')

    # Status do jogo difícil
    def game_status_hard(self):
        print('-=-=-=-=-=-=-=-=-=-')
        print(desenhos_hard[len(self.wrong_letters)])
        print('\nA palavra é: ' + self.show_letter())
        print('\nLetras erradas: ', )
        for letter in self.wrong_letters:
            print(letter, )
        print('-=-=-=-=-=-=-=-=-=-')


# Função para ler uma palavra de forma aleatória do banco de palavras fáceis
def random_word_easy():
    with open("palavras_easy.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Função para ler uma palavra de forma aleatória do banco de palavras fáceis
def random_word_hard():
    with open("palavras_hard.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()


# Criar objetivo dentro de uma função main
def main():
    # Objeto criado
    hangman_easy = HangmanGame(random_word_easy())
    hangman_hard = HangmanGame(random_word_hard())

    difficulty = int(input('1 -> Fácil'
                           '\n2 -> Difícil'
                           '\nEscolha: '))

    # Condição de dificuldade
    if difficulty == 1:
        print('Você selecionou o modo FÁCIL.')
        # Solicitar letra e mostrar status para o jogador
        while not hangman_easy.game_over_easy():
            hangman_easy.game_status_easy()
            letter = input('Digite uma letra: ')
            hangman_easy.add_letters(letter)

        # Verifica status do jogo e define se ganhou ou perdeu
        hangman_easy.game_status_easy()

        if hangman_easy.player_win():
            print('\nParabéns, você venceu no fácil! Tente jogar o modo mais difícil.')
        else:
            print(f'\nVocê perdeu! A palavra era {hangman_easy.word.upper()}.')

    elif difficulty == 2:
        print('Você selecionou o modo DIFÍCIL.')
        # Solicitar letra e mostrar status para o jogador
        while not hangman_hard.game_over_hard():
            hangman_hard.game_status_hard()
            letter = input('Digite uma letra:')
            hangman_hard.add_letters(letter)

        # Verificar satus do jogo e definir se ganhou ou perde
        hangman_hard.game_status_hard()

        if hangman_hard.player_win():
            print('\nParabéns, você venceu no modo mais difícil!')
        else:
            print(f'\nVocê perdeu! A palavra era {hangman_hard.word.upper()}.')

    else:
        print('\nOpção inválida. Tente novamente.')


# Executa a função main
if __name__ == "__main__":
    main()
