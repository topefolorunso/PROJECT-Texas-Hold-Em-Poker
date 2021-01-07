import unittest

from poker.card import Card
from poker.validators import StraightValidator

class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
        two = Card('2', 'Spades')
        six = Card('6', 'Hearts')
        self.seven = Card('7', 'Diamonds')
        self.eight = Card('8', 'Spades')
        self.nine = Card('9', 'Clubs')
        self.ten = Card('10', 'Clubs')
        self.jack = Card('Jack', 'Hearts')
            
        self.cards = [
            two,
            six,
            self.seven,
            self.eight,
            self.nine,
            self.ten,
            self.jack
        ]

    def test_determines_if_there_are_five_cards_in_a_row(self):
        validator = StraightValidator(self.cards)

        self.assertEqual(
            validator.is_valid(), 
            True
        )

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card('6', 'Hearts'), 
            Card('7', 'Diamonds')
        ]

        validator = StraightValidator(cards)

        self.assertEqual(
            validator.is_valid(), 
            False
        )

    def test_returns_five_highest_cards_in_a_row(self):
        validator = StraightValidator(self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.seven,
                self.eight,
                self.nine,
                self.ten,
                self.jack
            ]
        )