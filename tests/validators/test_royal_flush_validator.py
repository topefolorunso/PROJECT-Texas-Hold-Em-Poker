import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def test_validates_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card('9', 'Clubs'),
            Card('10', 'Clubs'), 
            Card('Jack', 'Clubs'), 
            Card('Queen', 'Clubs'), 
            Card('King', 'Clubs'), 
            Card('Ace', 'Diamonds'), 
        ]

        validator = RoyalFlushValidator(cards)

        self.assertEqual(
            validator.is_valid(), 
            False
        )

    def test_validates_that_cards_do_not_have_straight_flush_ending_in_ace(self):
        cards = [
            Card('2', 'Spades'),
            Card('10', 'Clubs'), 
            Card('Jack', 'Clubs'), 
            Card('Queen', 'Clubs'), 
            Card('King', 'Clubs'), 
            Card('Ace', 'Clubs'),
            Card('Ace', 'Diamonds')
        ]

        validator = RoyalFlushValidator(cards)

        self.assertEqual(
            validator.is_valid(), 
            True
        )

    def test_returns_five_straight_cards_with_same_rank_ending_in_ace(self):
        ten = Card('10', 'Clubs')
        jack = Card('Jack', 'Clubs')
        queen = Card('Queen', 'Clubs')
        king = Card('King', 'Clubs')
        ace = Card('Ace', 'Clubs')
        
        cards = [
            Card('2', 'Spades'),
            ten,
            jack,
            queen,
            king,
            ace,
            Card('Ace', 'Diamonds')
        ]

        validator = RoyalFlushValidator(cards)

        self.assertEqual(
            validator.valid_cards(), 
            [
                ten,
                jack,
                queen,
                king,
                ace
            ]
        )