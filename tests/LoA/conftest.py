import pytest
from brownie import LoAToken , accounts

@pytest.fixture
def token(LoAToken):
    LoA = LoAToken.deploy({"from": accounts[0]})    
    return LoA

