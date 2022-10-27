from scripts.deploy import deploy
from scripts.helpers import get_accounts
import datetime
import brownie

def test_create_game():
    contract = deploy(True)
    accounts = get_accounts()

    # game in the past
    yesterday = datetime.datetime.today() + datetime.timedelta(days=-1)
    timestamp = int(yesterday.timestamp())
    with brownie.reverts():
        contract.createGame(
            1,
            2,
            timestamp,
            {
                "from": accounts["main_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
            }
        )

    # same team
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    timestamp = int(tomorrow.timestamp())
    with brownie.reverts():
        contract.createGame(
            1,
            1,
            timestamp,
            {
                "from": accounts["main_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
            }
        )

    contract.createGame(1, 2, timestamp, {"from": accounts["main_wallet"]})
    game = contract.games(1)
    assert game == (0, 0, 1, 2, timestamp)
