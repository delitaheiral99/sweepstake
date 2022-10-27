from scripts.deploy import deploy
from scripts.helpers import get_accounts
import datetime
import brownie
from web3 import Web3

def test_place_bet():
    contract = deploy(True)
    accounts = get_accounts()

    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    timestamp = int(tomorrow.timestamp())

    with brownie.reverts():
        contract.placeBet(
            1,
            1,
            1,
            {
                "from": accounts["player1_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
                "value": Web3.toWei(0.01, "ether")
            }
        )

    contract.register({
        "from": accounts["player1_wallet"],
        "value": Web3.toWei(0.1, "ether")
    })

    with brownie.reverts():
        contract.placeBet(
            1,
            1,
            1,
            {
                "from": accounts["player1_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
                "value": Web3.toWei(0.1, "ether")
            }
        )

    with brownie.reverts():
        contract.placeBet(
            1,
            1,
            1,
            {
                "from": accounts["player1_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
                "value": Web3.toWei(0.01, "ether")
            }
        )

    contract.createGame(1, 2, timestamp, {"from": accounts["main_wallet"]})

    contract.placeBet(
        1,
        2,
        1,
        {
            "from": accounts["player1_wallet"],
            "value": Web3.toWei(0.01, "ether")
        }
    )

    bet = contract.bets(1)

    assert bet == (1, 2, 1, accounts["player1_wallet"])
    assert contract.allGameBets(1, 0) == bet
    assert contract.betByPlayerGame(accounts["player1_wallet"], 1) == 1
    assert contract.balance() == Web3.toWei(0.11, "ether")

    with brownie.reverts():
        contract.placeBet(
            1,
            1,
            1,
            {
                "from": accounts["player1_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
                "value": Web3.toWei(0.01, "ether")
            }
        )


