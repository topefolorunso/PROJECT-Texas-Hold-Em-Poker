from poker.validators import ThreeOfAKindValidator, PairValidator

class FullHouseValidator():
    def __init__(self, cards):
        self.cards = cards
        self.name = 'Full House'

    def is_valid(self):
        return ThreeOfAKindValidator(self.cards).is_valid() and PairValidator(self.cards).is_valid()

    def valid_cards(self):
        three_of_a_kind_cards = ThreeOfAKindValidator(self.cards).valid_cards()
        pair_cards = PairValidator(self.cards).valid_cards()
        all_cards = three_of_a_kind_cards + pair_cards
        all_cards.sort()
        return all_cards