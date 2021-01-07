from poker.card import Card
from poker.deck import Deck
from poker.game_round import GameRound
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player('Tope', hand1)
player2 = Player('Layo', hand2)
players = [player1, player2]

game_round = GameRound(deck, players)
game_round.play()

for player in players:
    print(f'{player.name} recieves a {player.hand}.')
    index, hand_name, hand_cards = player.best_hand()
    hand_card_strings = [str(card) for card in hand_cards]
    hand_card_strings = ' and '.join(hand_card_strings)
    print(f'{player.name} has a {hand_name} with a {hand_card_strings}.')

winning_player = max(players)

print(f'The winner is {winning_player.name}.')