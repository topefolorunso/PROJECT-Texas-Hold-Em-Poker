import unittest
from poker.card import Card
from poker.hand import Hand
from poker.validators import PairValidator

class HandTest(unittest.TestCase):
    def test_starts_out_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_cards_in_technical_representation(self):
        cards = [
            Card('Ace', 'Diamonds'),
            Card('7', 'Clubs')
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            repr(hand),
            '7 of Clubs, Ace of Diamonds'
        )

    def test_receives_and_stores_cards(self):
        ace_of_spades = Card('Ace', 'Spades')
        six_of_clubs = Card('6', 'Clubs')
        
        cards = [
            ace_of_spades, 
            six_of_clubs
        ]

        hand = Hand()
        hand.add_cards(cards)

        self.assertEqual(
            hand.cards,
            [
                six_of_clubs,
                ace_of_spades
            ]
        )

    def test_interacts_with_validator_to_get_winning_hand(self):
        class HandWithOneValidator(Hand):
            VALIDATORS = (PairValidator,)

        ace_of_hearts = Card('Ace', 'Hearts')
        ace_of_spades = Card('Ace', 'Spades')
        cards = [ace_of_hearts, ace_of_spades]

        hand = HandWithOneValidator()
        hand.add_cards(cards)

        self.assertEqual(
            hand.best_rank(),
            (0, 'Pair', cards)
        )