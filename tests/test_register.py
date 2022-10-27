from scripts.deploy import deploy
from scripts.helpers import get_accounts
import brownie
from web3 import Web3

def test_register():
    contract = deploy(True)
    accounts = get_accounts()

    with brownie.reverts():
        contract.register(
            {
                "from": accounts["player1_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
                "value": Web3.toWei(1, "ether")
            }
        )

    contract.register({
        "from": accounts["player1_wallet"],
        "value": Web3.toWei(0.1, "ether")
    })

    player = contract.players(1)
    assert contract.registeredPlayers(accounts["player1_wallet"]) == 1
    assert player == accounts["player1_wallet"]
    assert contract.balance() == Web3.toWei(0.1, "ether")

    with brownie.reverts():
        contract.register(
            {
                "from": accounts["player1_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
                "value": Web3.toWei(0.1, "ether")
            }
        )

    with brownie.reverts():
        accounts["player2_wallet"].transfer(
            to=contract,
            amount="0.01 ether",
            gas_limit=1000000,
            allow_revert=True
        )

    accounts["player2_wallet"].transfer(contract, "0.1 ether")
    assert contract.balance() == Web3.toWei(0.2, "ether")
    assert contract.playerCount() == 2
    assert contract.players(2) == accounts["player2_wallet"]
