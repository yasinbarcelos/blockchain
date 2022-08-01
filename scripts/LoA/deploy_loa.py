#!/usr/bin/python3
from brownie import LoAToken
from scripts.helpful_scripts import get_account

def deploy_loa(account= get_account()):
    LoA =  LoAToken.deploy({"from": account})
    print(LoA.signatures)
    return LoA
    
def main():    
    deploy_loa()    