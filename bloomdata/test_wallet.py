from bloomdata.wallet import Wallet
import pytest

@pytest.fixture
def empty_wallet():
    return Wallet()

@pytest.fixture
def wallet_50():
    return Wallet(50)


def test_empty_wallet(empty_wallet):
    assert empty_wallet.balance == 0

def test_wallet_50(wallet_50):
    assert wallet_50.balance == 50
    #assert wallet_50.spend_cash(20) == 'remaining balance : $30'
    #assert wallet_50.spend_cash(60) == 'Not enough money'
    assert wallet_50.spend_cash(50) == 'remaining balance : $0'
    