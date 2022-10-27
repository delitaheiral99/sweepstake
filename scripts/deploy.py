from brownie import Sweepstake
from scripts.helpers import get_accounts


def deploy(force=False):
    accounts = get_accounts()
    if force == True or len(Sweepstake) < 1:
        contract = Sweepstake.deploy({"from": accounts["main_wallet"]})
        print(f"Sweepstake contract deployed to {contract.address}")
    else:
        contract = Sweepstake[-1]
        print(f"Sweepstake contract already deployed to {contract.address}")
    return contract


def main():
    deploy()
