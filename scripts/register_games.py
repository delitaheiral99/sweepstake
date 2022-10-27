from scripts.deploy import deploy
from scripts.helpers import get_accounts
from enum import Enum
import time
import calendar

class Team(Enum):
    QATAR=1
    ECUADOR=2
    SENEGAL=3
    NETHERLANDS=4
    ENGLAND=5
    IRAN=6
    USA=7
    WALES=8
    ARGENTINA=9
    SAUDI_ARABIA=10
    MEXICO=11
    POLAND=12
    FRANCE=13
    AUSTRALIA=14
    DENMARK=15
    TUNISIA=16
    SPAIN=17
    COSTA_RICA=18
    GERMANY=19
    JAPAN=20
    BELGIUM=21
    CANADA=22
    MOROCCO=23
    CROATIA=24
    BRAZIL=25
    SERBIA=26
    SWITZERLAND=27
    CAMEROON=28
    PORTUGAL=29
    GHANA=30
    URUGUAY=31
    KOREA_REPUBLIC=32

MATCHES = [
    [Team.QATAR, Team.ECUADOR, "2022-11-20T16:00:00Z"],
    [Team.ENGLAND, Team.IRAN, "2022-11-21T13:00:00Z"],
    [Team.SENEGAL, Team.NETHERLANDS, "2022-11-21T16:00:00Z"],
    [Team.USA, Team.WALES, "2022-11-21T19:00:00Z"],
    [Team.ARGENTINA, Team.SAUDI_ARABIA, "2022-11-22T10:00:00Z"],
    [Team.DENMARK, Team.TUNISIA, "2022-11-22T13:00:00Z"],
    [Team.MEXICO, Team.POLAND, "2022-11-22T16:00:00Z"],
    [Team.FRANCE, Team.AUSTRALIA, "2022-11-22T19:00:00Z"],
    [Team.MOROCCO, Team.CROATIA, "2022-11-23T10:00:00Z"],
    [Team.GERMANY, Team.JAPAN, "2022-11-23T13:00:00Z"],
    [Team.SPAIN, Team.COSTA_RICA, "2022-11-23T16:00:00Z"],
    [Team.BELGIUM, Team.CANADA, "2022-11-23T19:00:00Z"],
    [Team.SWITZERLAND, Team.CAMEROON, "2022-11-24T10:00:00Z"],
    [Team.URUGUAY, Team.KOREA_REPUBLIC, "2022-11-24T13:00:00Z"],
    [Team.PORTUGAL, Team.GHANA, "2022-11-24T16:00:00Z"],
    [Team.BRAZIL, Team.SERBIA, "2022-11-24T19:00:00Z"],
    [Team.WALES, Team.IRAN, "2022-11-25T10:00:00Z"],
    [Team.QATAR, Team.SENEGAL, "2022-11-25T13:00:00Z"],
    [Team.NETHERLANDS, Team.ECUADOR, "2022-11-25T16:00:00Z"],
    [Team.ENGLAND, Team.USA, "2022-11-25T19:00:00Z"],
    [Team.TUNISIA, Team.AUSTRALIA, "2022-11-26T10:00:00Z"],
    [Team.POLAND, Team.SAUDI_ARABIA, "2022-11-26T13:00:00Z"],
    [Team.FRANCE, Team.DENMARK, "2022-11-26T16:00:00Z"],
    [Team.ARGENTINA, Team.MEXICO, "2022-11-26T19:00:00Z"],
    [Team.JAPAN, Team.COSTA_RICA, "2022-11-27T10:00:00Z"],
    [Team.BELGIUM, Team.MOROCCO, "2022-11-27T13:00:00Z"],
    [Team.CROATIA, Team.CANADA, "2022-11-27T16:00:00Z"],
    [Team.SPAIN, Team.GERMANY, "2022-11-27T19:00:00Z"],
    [Team.CAMEROON, Team.SERBIA, "2022-11-28T10:00:00Z"],
    [Team.KOREA_REPUBLIC, Team.GHANA, "2022-11-28T13:00:00Z"],
    [Team.BRAZIL, Team.SWITZERLAND, "2022-11-28T16:00:00Z"],
    [Team.PORTUGAL, Team.URUGUAY, "2022-11-28T19:00:00Z"],
    [Team.NETHERLANDS, Team.QATAR, "2022-11-29T15:00:00Z"],
    [Team.ECUADOR, Team.SENEGAL, "2022-11-29T15:00:00Z"],
    [Team.WALES, Team.ENGLAND, "2022-11-29T19:00:00Z"],
    [Team.IRAN, Team.USA, "2022-11-29T19:00:00Z"],
    [Team.AUSTRALIA, Team.DENMARK, "2022-11-30T15:00:00Z"],
    [Team.TUNISIA, Team.FRANCE, "2022-11-30T15:00:00Z"],
    [Team.POLAND, Team.ARGENTINA, "2022-11-30T19:00:00Z"],
    [Team.SAUDI_ARABIA, Team.MEXICO, "2022-11-30T19:00:00Z"],
    [Team.CROATIA, Team.BELGIUM, "2022-12-01T15:00:00Z"],
    [Team.CANADA, Team.MOROCCO, "2022-12-01T15:00:00Z"],
    [Team.JAPAN, Team.SPAIN, "2022-12-01T19:00:00Z"],
    [Team.COSTA_RICA, Team.GERMANY, "2022-12-01T19:00:00Z"],
    [Team.GHANA, Team.URUGUAY, "2022-12-02T15:00:00Z"],
    [Team.KOREA_REPUBLIC, Team.PORTUGAL, "2022-12-02T15:00:00Z"],
    [Team.SERBIA, Team.SWITZERLAND, "2022-12-02T19:00:00Z"],
    [Team.CAMEROON, Team.BRAZIL, "2022-12-02T19:00:00Z"],
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
