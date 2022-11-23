from scripts.deploy import deploy
from scripts.helpers import get_accounts
from scripts.teams import Team
import time
import calendar

MATCHES = [
    [Team.QAT, Team.ECU, "2022-11-20T16:00:00Z"], #1
    [Team.ENG, Team.IRN, "2022-11-21T13:00:00Z"], #2
    [Team.SEN, Team.NED, "2022-11-21T16:00:00Z"], #3
    [Team.USA, Team.WAL, "2022-11-21T19:00:00Z"], #4
    [Team.ARG, Team.KSA, "2022-11-22T10:00:00Z"], #5
    [Team.DEN, Team.TUN, "2022-11-22T13:00:00Z"], #6
    [Team.MEX, Team.POL, "2022-11-22T16:00:00Z"], #7
    [Team.FRA, Team.AUS, "2022-11-22T19:00:00Z"], #8
    [Team.MAR, Team.CRO, "2022-11-23T10:00:00Z"], #9
    [Team.GER, Team.JPN, "2022-11-23T13:00:00Z"], #10
    [Team.ESP, Team.CRC, "2022-11-23T16:00:00Z"], #11
    [Team.BEL, Team.CAN, "2022-11-23T19:00:00Z"], #12
    [Team.SUI, Team.CMR, "2022-11-24T10:00:00Z"], #13
    [Team.URU, Team.KOR, "2022-11-24T13:00:00Z"], #14
    [Team.POR, Team.GHA, "2022-11-24T16:00:00Z"], #15
    [Team.BRA, Team.SRB, "2022-11-24T19:00:00Z"], #16
    [Team.WAL, Team.IRN, "2022-11-25T10:00:00Z"], #17
    [Team.QAT, Team.SEN, "2022-11-25T13:00:00Z"], #18
    [Team.NED, Team.ECU, "2022-11-25T16:00:00Z"], #19
    [Team.ENG, Team.USA, "2022-11-25T19:00:00Z"], #20
    [Team.TUN, Team.AUS, "2022-11-26T10:00:00Z"], #21
    [Team.POL, Team.KSA, "2022-11-26T13:00:00Z"], #22
    [Team.FRA, Team.DEN, "2022-11-26T16:00:00Z"], #23
    [Team.ARG, Team.MEX, "2022-11-26T19:00:00Z"], #24
    [Team.JPN, Team.CRC, "2022-11-27T10:00:00Z"], #25
    [Team.BEL, Team.MAR, "2022-11-27T13:00:00Z"], #26
    [Team.CRO, Team.CAN, "2022-11-27T16:00:00Z"], #27
    [Team.ESP, Team.GER, "2022-11-27T19:00:00Z"], #28
    [Team.CMR, Team.SRB, "2022-11-28T10:00:00Z"], #29
    [Team.KOR, Team.GHA, "2022-11-28T13:00:00Z"], #30
    [Team.BRA, Team.SUI, "2022-11-28T16:00:00Z"], #31
    [Team.POR, Team.URU, "2022-11-28T19:00:00Z"], #32
    [Team.NED, Team.QAT, "2022-11-29T15:00:00Z"], #33
    [Team.ECU, Team.SEN, "2022-11-29T15:00:00Z"], #34
    [Team.WAL, Team.ENG, "2022-11-29T19:00:00Z"], #35
    [Team.IRN, Team.USA, "2022-11-29T19:00:00Z"], #36
    [Team.AUS, Team.DEN, "2022-11-30T15:00:00Z"], #37
    [Team.TUN, Team.FRA, "2022-11-30T15:00:00Z"], #38
    [Team.POL, Team.ARG, "2022-11-30T19:00:00Z"], #39
    [Team.KSA, Team.MEX, "2022-11-30T19:00:00Z"], #40
    [Team.CRO, Team.BEL, "2022-12-01T15:00:00Z"], #41
    [Team.CAN, Team.MAR, "2022-12-01T15:00:00Z"], #42
    [Team.JPN, Team.ESP, "2022-12-01T19:00:00Z"], #43
    [Team.CRC, Team.GER, "2022-12-01T19:00:00Z"], #44
    [Team.GHA, Team.URU, "2022-12-02T15:00:00Z"], #45
    [Team.KOR, Team.POR, "2022-12-02T15:00:00Z"], #46
    [Team.SRB, Team.SUI, "2022-12-02T19:00:00Z"], #47
    [Team.CMR, Team.BRA, "2022-12-02T19:00:00Z"], #48
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
