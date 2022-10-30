# test09.py
#  L. Lee (LJL2), S. Marschner (SRM2), and W. White (WMW2)
# September 28, 2013
"""Unit test for module blackjack"""
import cornelltest
import lab09
import card


def test_init():
    """Test initializer of blackjack objects"""
    c1 = card.Card(0, 12)
    c2 = card.Card(1, 10)
    c3 = card.Card(2, 9)
    c4 = card.Card(0, 1)
    
    # Initialize deck and start game.
    deck = [c1, c2, c3, c4]
    game = lab09.Blackjack(deck)
    
    cornelltest.assert_equals([c1, c2], game.playerHand)
    cornelltest.assert_equals([c3], game.dealerHand)
    cornelltest.assert_equals([c4], deck)  # check that cards were removed
    
    deck = card.full_deck()  # non-shuffled deck
    game = lab09.Blackjack(deck)
    c1 = card.Card(0, 1)
    c2 = card.Card(0, 2)
    c3 = card.Card(0, 3)
    c4 = card.Card(0, 4)
    
    cornelltest.assert_equals([c1, c2], game.playerHand)
    cornelltest.assert_equals([c3], game.dealerHand)
    
    # check that right cards were removed
    cornelltest.assert_equals(card.full_deck()[3:], deck)
    
    print 'Test of testinit passed'


def test_str():
    """Test __str__ function for Blackjack objects"""
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = lab09.Blackjack(deck)
    cornelltest.assert_equals('player: 20; dealer: 9', str(game))
    
    game.playerHand=[]
    cornelltest.assert_equals('player: 0; dealer: 9', str(game))
    game.dealerHand.append(card.Card(2,1))
    cornelltest.assert_equals('player: 0; dealer: 20', str(game))
    game.dealerHand.append(card.Card(2,5))
    cornelltest.assert_equals('player: 0; dealer: 25', str(game))
    
    print 'Tests of __str__ passed'


def test_score():
    """Test _score function"""
    # need a dummy game object to call its _score function (and test it)
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = lab09.Blackjack(deck)
    
    cornelltest.assert_equals(13,
                game._score([card.Card(2, 2), card.Card(3, 1)]))
    cornelltest.assert_equals(13,
                game._score([card.Card(1, 13), card.Card(0, 3)]))
    cornelltest.assert_equals(22,
                game._score([card.Card(1, 1), card.Card(0, 1)]))
    cornelltest.assert_equals(9,
                game._score([card.Card(1, 2),
                             card.Card(0, 3),
                             card.Card(3, 4)]))
    cornelltest.assert_equals(0, game._score([]))
    
    print 'Tests of _score passed'


def test_dealerScore():
    """Test dealerScore function"""
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = lab09.Blackjack(deck)
    
    cornelltest.assert_equals(9, game.dealerScore())
    game.dealerHand = [card.Card(2, 2), card.Card(3, 1)]
    game.playerHand = [card.Card(1, 13), card.Card(0, 3)]
    cornelltest.assert_equals(13, game.dealerScore())
    
    print 'Tests of dealerScore passed'


def test_playerScore():
    """Test playerScore function"""
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = lab09.Blackjack(deck)
    
    cornelltest.assert_equals(20, game.playerScore())
    game.playerHand = [card.Card(2, 2), card.Card(3, 1)]
    game.dealerHand = [card.Card(1, 13), card.Card(0, 3)]
    cornelltest.assert_equals(13, game.playerScore())
    
    print 'Tests of playerScore passed'


def test_playerBust():
    """Test playerBust function"""
    
    # get dummy deck
    deck = [card.Card(0, 12), card.Card(1, 10), card.Card(2, 9)]
    game = lab09.Blackjack(deck)
    
    cornelltest.assert_true(not game.playerBust())
    game.playerHand = [card.Card(0, 1), card.Card(1, 10)]
    cornelltest.assert_true(not game.playerBust())
    game.playerHand = [card.Card(0, 1), card.Card(1, 10), card.Card(0, 2)]
    cornelltest.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 1)]
    cornelltest.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1)]
    cornelltest.assert_true(game.playerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1), card.Card(1,1)]
    cornelltest.assert_true(game.playerBust())
    
    print 'Tests of playerBust passed'


def test_dealerBust():
    """Test dealerBust function"""
    # get dummy deck
    deck = [card.Card(0, 12),  card.Card(2, 9), card.Card(1, 10),]
    game = lab09.Blackjack(deck)
    
    cornelltest.assert_true(not game.dealerBust())
    game.dealerHand = [card.Card(0, 1), card.Card(1, 10)]
    cornelltest.assert_true(not game.dealerBust())
    game.dealerHand = [card.Card(0, 1), card.Card(1, 10), card.Card(0, 2)]
    cornelltest.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 10), card.Card(1, 10), card.Card(0, 1)]
    cornelltest.assert_true(game.dealerBust())
    game.dealerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1)]
    cornelltest.assert_true(game.dealerBust())
    game.playerHand = [card.Card(0, 11), card.Card(1, 10), card.Card(0, 1), card.Card(1,1)]
    cornelltest.assert_true(game.playerBust())
    
    print 'tests of playerBust passed'


# Script code
if __name__ == '__main__':
    test_init()
    test_score()
    test_dealerScore()
    test_playerScore()
    test_dealerBust()
    test_playerBust()
    test_str()

    print "All tests for lab 9 passed"
