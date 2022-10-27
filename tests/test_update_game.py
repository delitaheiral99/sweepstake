from scripts.deploy import deploy
from scripts.helpers import get_accounts
import datetime
import brownie

def test_update_game():
    contract = deploy(True)
    accounts = get_accounts()
    tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
    timestamp = int(tomorrow.timestamp())
    contract.createGame(10, 20, timestamp, {"from": accounts["main_wallet"]})

    yesterday = datetime.datetime.today() + datetime.timedelta(days=-1)
    timestamp = int(yesterday.timestamp())
    with brownie.reverts():
        contract.updateGame(
            1,
            3,
            4,
            timestamp,
            {
                "from": accounts["main_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
            }
        )

    tomorrow += datetime.timedelta(days=1)
    timestamp = int(tomorrow.timestamp())
    game = contract.games(1)
    print(game)
    with brownie.reverts():
        contract.updateGame(
            1,
            10,
            20,
            timestamp,
            {
                "from": accounts["main_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
            }
        )
    with brownie.reverts():
        contract.updateGame(
            1,
            10,
            0,
            timestamp,
            {
                "from": accounts["main_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
            }
        )
    contract.updateGame(1, 10, 4, timestamp, {"from": accounts["main_wallet"]})
    game = contract.games(1)

    assert game == (0, 0, 10, 4, timestamp)
