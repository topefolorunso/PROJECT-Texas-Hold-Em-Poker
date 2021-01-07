import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def test_determines_that_there_are_not_five_consecutive_cards_with_same_suit(self):
        cards = [
            Card('3', 'Clubs'), 
            Card('4', 'Clubs'), 
            Card('5', 'Clubs'), 
            Card('6', 'Clubs'), 
            Card('7', 'Diamonds'),
            Card('King', 'Clubs'),
            Card('Ace', 'Diamonds')
        ]

        validator = StraightFlushValidator(cards)

        self.assertEqual(
            validator.is_valid(), 
            False
        )

    def test_determines_that_there_are_five_consecutive_cards_with_same_suit(self):
        cards = [
            Card('3', 'Clubs'), 
            Card('4', 'Clubs'), 
            Card('5', 'Clubs'), 
            Card('6', 'Clubs'), 
            Card('7', 'Clubs'),
            Card('King', 'Clubs'),
            Card('Ace', 'Diamonds')
        ]

        validator = StraightFlushValidator(cards)

        self.assertEqual(
            validator.is_valid(), 
            True
        )

    def test_determines_that_there_are_five_consecutive_cards_with_same_suit(self):
        three = Card('3', 'Clubs')
        four = Card('4', 'Clubs')
        five = Card('5', 'Clubs')
        six = Card('6', 'Clubs')
        seven = Card('7', 'Clubs')
            
        cards = [
            three,
            four,
            five,
            six,
            seven,            
            Card('King', 'Clubs'),
            Card('Ace', 'Diamonds')
        ]

        validator = StraightFlushValidator(cards)

        self.assertEqual(
            validator.valid_cards(), 
            [
                three,
                four,
                five,
                six,
                seven
            ]
        )