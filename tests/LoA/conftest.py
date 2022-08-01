import pytest
from brownie import LoAToken
from scripts.helpful_scripts import get_account

@pytest.fixture
def token(LoAToken):
    LoA = LoAToken.deploy({"from": get_account(index=0)})    
    return LoA

