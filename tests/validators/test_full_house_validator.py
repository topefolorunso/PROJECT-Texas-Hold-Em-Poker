import unittest

from poker.card import Card
from poker.validators import FullHouseValidator

class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs = Card('3', 'Clubs')
        self.three_of_hearts = Card('3', 'Hearts')
        self.three_of_spades = Card('3', 'Spades')
        self.nine_of_diamonds = Card('9', 'Diamonds')
        self.nine_of_spades = Card('9', 'Spades')

        self.cards = [
            self.three_of_clubs,
            self.three_of_hearts,
            self.three_of_spades,
            Card('5', 'Diamonds'),
            self.nine_of_diamonds,
            self.nine_of_spades,
            Card('Queen', 'Clubs')
        ]

    def test_validates_that_cards_have_two_of_the_same_rank_and_three_of_another_rank(self):
        validator = FullHouseValidator(self.cards)

        self.assertEqual(
            validator.is_valid(), 
            True
        )

    def test_returns_collection_of_two_cards_of_the_same_rank_and_three_cards_of_the_same_rank(self):
        validator = FullHouseValidator(self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_clubs,
                self.three_of_hearts,
                self.three_of_spades,
                self.nine_of_diamonds,
                self.nine_of_spades
            ]
        )