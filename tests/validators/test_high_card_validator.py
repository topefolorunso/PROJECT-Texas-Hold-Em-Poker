import unittest

from poker.card import Card
from poker.validators import HighCardValidator

class HighCardValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_a_high_card(self):
        cards = [
            Card('7', 'Clubs'), 
            Card('Ace', 'Diamonds')
        ]

        validator = HighCardValidator(cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_high_card_from_card_collection(self):
        ace_of_diamonds = Card('Ace', 'Diamonds')

        cards = [
            Card('5', 'Spades'),
            Card('8', 'Diamonds'), 
            Card('10', 'Clubs'),
            Card('Queen', 'Spades'),
            ace_of_diamonds
        ]

        validator = HighCardValidator(cards)

        self.assertEqual(
            validator.valid_cards(),
            [ace_of_diamonds]
        )