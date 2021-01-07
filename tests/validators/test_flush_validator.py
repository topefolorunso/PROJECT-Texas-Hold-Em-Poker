import unittest

from poker.card import Card
from poker.validators import FlushValidator

class FlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.two_of_hearts = Card('2', 'Hearts')
        self.five_of_hearts = Card('5', 'Hearts')
        self.seven_of_hearts = Card('7', 'Hearts')
        self.eight_of_hearts = Card('8', 'Hearts')
        self.ten_of_hearts = Card('10', 'Hearts')
        self.ace_of_hearts = Card('Ace', 'Hearts')

        self.cards = [
            self.two_of_hearts,
            self.five_of_hearts,
            self.seven_of_hearts,
            self.eight_of_hearts,
            self.ten_of_hearts,
            Card('Jack', 'Clubs'),
            self.ace_of_hearts
        ]

    def test_validates_that_five_cards_of_same_suit_exist_in_collection(self):
        validator = FlushValidator(self.cards)

        self.assertEqual(
            validator.is_valid(), 
            True
        )

    def test_returns_the_five_highest_cards_with_the_same_suit(self):
        validator = FlushValidator(self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.five_of_hearts,
                self.seven_of_hearts,
                self.eight_of_hearts,
                self.ten_of_hearts,
                self.ace_of_hearts
            ]
        )