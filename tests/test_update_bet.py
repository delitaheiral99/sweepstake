from scripts.deploy import deploy
from scripts.helpers import get_accounts
import datetime
import brownie
from web3 import Web3

def test_update_bet():
    contract = deploy(True)
    accounts = get_accounts()

    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    timestamp = int(tomorrow.timestamp())

    contract.register({
        "from": accounts["player1_wallet"],
        "value": Web3.toWei(0.1, "ether")
    })

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
    game_bet = contract.gameBets(1, 0)
    player_bet = contract.playerBets(accounts["player1_wallet"], 0)
    assert bet == (1, 2, 1, accounts["player1_wallet"])
    assert contract.bets(game_bet) == bet
    assert contract.bets(player_bet) == bet
    assert contract.betByPlayerGame(accounts["player1_wallet"], 1) == 1

    contract.updateBet(1, 3, 4, {
        "from": accounts["player1_wallet"],
        "value": Web3.toWei(0.01, "ether")
    })

    bet = contract.bets(1)
    game_bet = contract.gameBets(1, 0)
    player_bet = contract.playerBets(accounts["player1_wallet"], 0)
    assert bet == (1, 3, 4, accounts["player1_wallet"])
    assert contract.bets(game_bet) == bet
    assert contract.bets(player_bet) == bet
    assert contract.betByPlayerGame(accounts["player1_wallet"], 1) == 1
    assert contract.balance() == Web3.toWei(0.12, "ether")

    with brownie.reverts():
        contract.updateBet(1, 3, 4, {
            "from": accounts["player2_wallet"],
            "value": Web3.toWei(0.01, "ether"),
            "allow_revert": True,
            "gas_limit": 1000000
        })

