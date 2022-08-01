import pytest
from brownie import reverts, accounts
from brownie.test import given, strategy
from scripts.helpful_scripts import get_account

def test_mint_loa(token):   
    account = get_account()
    mint_amount = 100**18    

    token.mint(account, mint_amount, {"from": account})     

    assert token.balanceOf(account) == mint_amount

def test_sender_balance_increases(token):
    admin = get_account(index=0)        
    mint_amount = 100**18
    
    token.mint(admin, mint_amount, {"from": admin}) 

    assert token.balanceOf(admin) == mint_amount

    
def test_sender_balance_decreases(token):
    #Arrange
    admin = get_account(index=0)    
    user1 = get_account(index=1)   
    mint_amount = 100**18
    token.mint(admin, mint_amount, {"from": admin}) 
 
    #Act    
    token.approve(user1, mint_amount, {'from': admin})
    token.transferFrom(admin, user1, mint_amount, {'from': user1})

    #Assert
    assert token.balanceOf(admin) == 0
    
def test_total_supply_updated(token):
    #Arrange    
    account = get_account()
    mint_amount = 100**18
    
    #Act
    token.mint(account, mint_amount, {"from": account}) 
    
    #Assert
    assert token.totalSupply() == mint_amount    
    token.burn(mint_amount, {"from": account})     
    assert token.totalSupply() == 0    

def test_transfer_event_fires(token):
    #Arrange  
    user1 = get_account(index=1)       
    user2 = get_account(index=2)
    amount = 100**18
    #Act
    #Assert
    amount = token.balanceOf(user1)

    token.approve(user2, amount, {'from': user1})
    tx = token.transferFrom(user1, user2, amount, {'from': user2})

    assert len(tx.events) == 2
    assert tx.events["Transfer"].values() == [user1, user2, amount]
 
def test_burn_loa(token):   
    #Arrange
    account = get_account()
    amount = 100**18
    
    #Act    
    token.mint(account, amount, {"from": account}) 
    token.burn(amount, {"from": account}) 
    
    #Assert    
    assert token.balanceOf(account) == 0 
    
def test_transfer_without_approval(token):
    #Arrange
    admin = get_account(index=0)    
    user1 = get_account(index=1)       
    user2 = get_account(index=2)
    sender_balance = token.balanceOf(user1)
    receiver_balance = token.balanceOf(user2)
    #Act
    token.transferFrom(user1, user2, 0, {'from': admin})
    
    #Assert   
    assert token.balanceOf(user1) == sender_balance
    assert token.balanceOf(user2) == receiver_balance    
    
def test_mint_permission_loa(token):   
    #Arrange
    admin = get_account(index=0)
    user1 = get_account(index=1)    
    mint_amount = 100**18    

    #Act 
    token.mint(user1, mint_amount, {"from": admin})  
    with reverts():
        token.mint(user1, mint_amount, {"from": user1})  
        
    #Assert    
    assert token.balanceOf(user1) == mint_amount 