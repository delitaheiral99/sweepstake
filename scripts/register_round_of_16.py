from scripts.deploy import deploy
from scripts.helpers import get_accounts
from scripts.teams import Team
import time
import calendar

MATCHES = [
    [Team.NED, Team.USA, "2022-12-03T15:00:00Z"], #49
    [Team.ARG, Team.AUS, "2022-12-03T19:00:00Z"], #50
    [Team.ENG, Team.SEN, "2022-12-04T15:00:00Z"], #51
    [Team.FRA, Team.POL, "2022-12-04T19:00:00Z"], #52
    [Team.JPN, Team.CRO, "2022-12-05T15:00:00Z"], #53
    [Team.BRA, Team.KOR, "2022-12-05T19:00:00Z"], #54
    [Team.MAR, Team.ESP, "2022-12-06T15:00:00Z"], #55
    [Team.POR, Team.SUI, "2022-12-06T19:00:00Z"], #56
]

def register_games():
    contract = deploy()
    accounts = get_accounts()

    for match in MATCHES:
        timestamp = time.strptime(match[2], "%Y-%m-%dT%H:%M:%SZ")
        unix_timestamp = calendar.timegm(timestamp)
        contract.createGame(
            match[0].value,
            match[1].value,
            unix_timestamp,
            {'from': accounts["main_wallet"]}
        )


def main():
    register_games()
