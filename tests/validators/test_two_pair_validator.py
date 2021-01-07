import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.five_of_clubs = Card('5', 'Clubs')
        self.king_of_diamonds = Card('King', 'Diamonds')
        self.king_of_hearts = Card('King', 'Hearts')
        self.ace_of_clubs = Card('Ace', 'Clubs')
        self.ace_of_spades = Card('Ace', 'Spades')

        self.cards = [
            self.five_of_clubs,
            self.king_of_diamonds, 
            self.king_of_hearts, 
            self.ace_of_clubs, 
            self.ace_of_spades
        ]

    def test_validates_that_cards_have_at_least_two_pairs_of_same_rank(self):
        validator = TwoPairValidator(self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_collection_of_cards_that_have_pairs(self):
        validator = TwoPairValidator(self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_diamonds,
                self.king_of_hearts,
                self.ace_of_clubs,
                self.ace_of_spades
            ]
        )