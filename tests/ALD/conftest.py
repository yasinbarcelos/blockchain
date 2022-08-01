import pytest
from brownie import ALDToken
from scripts.helpful_scripts import get_account

@pytest.fixture
def token(ALDToken):
    ALD = ALDToken.deploy({"from": get_account(index=0)})    
    return ALD