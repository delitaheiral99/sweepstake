from scripts.deploy import deploy
from scripts.helpers import get_accounts
import datetime, time, brownie

def test_update_score():
    contract = deploy(True)
    accounts = get_accounts()
    later = datetime.datetime.today() + datetime.timedelta(seconds=10)
    timestamp = int(later.timestamp())
    contract.createGame(1, 2, timestamp, {"from": accounts["main_wallet"]})
    with brownie.reverts():
        contract.updateScore(
            1,
            3,
            4,
            {
                "from": accounts["main_wallet"],
                "allow_revert": True,
                "gas_limit": 1000000,
            }
        )
    print("Waiting for game to start")
    time.sleep(12)
    print("Game started")
    game = contract.games(1)
    print(game)
    print(time.time())
    contract.updateScore(1, 2, 2, {"from": accounts["main_wallet"]})

    assert game == (0, 0, 10, 4, timestamp)
