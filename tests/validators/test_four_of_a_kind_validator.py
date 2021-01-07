import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs = Card('3', 'Clubs')
        self.three_of_diamonds = Card('3', 'Diamonds')
        self.three_of_hearts = Card('3', 'Hearts')
        self.three_of_spades = Card('3', 'Spades')

        self.cards = [
            Card('2', 'Clubs'),
            self.three_of_clubs,
            self.three_of_diamonds,
            self.three_of_hearts,
            self.three_of_spades,
            Card('7', 'Hearts'),
            Card('9', 'Spades')
        ]

    def test_determines_that_four_cards_of_one_rank_are_present(self):
        validator = FourOfAKindValidator(self.cards)

        self.assertEqual(
            validator.is_valid(), 
            True
        )

    def test_returns_the_four_cards_with_the_same_rank(self):
        validator = FourOfAKindValidator(self.cards)

        self.assertEqual(
            validator.valid_cards(), 
            [
                self.three_of_clubs,
                self.three_of_diamonds,
                self.three_of_hearts,
                self.three_of_spades
            ]
        )