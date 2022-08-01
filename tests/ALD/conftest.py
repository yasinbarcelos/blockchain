import pytest
from brownie import ALDToken
from scripts.helpful_scripts import get_account

@pytest.fixture
def token(ALDToken):
    ALD = ALDToken.deploy({"from": accounts[0]})    
    return ALD
