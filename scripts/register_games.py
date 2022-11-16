from scripts.deploy import deploy
from scripts.helpers import get_accounts
from scripts.teams import Team
import time
import calendar

MATCHES = [
    [Team.QAT, Team.ECU, "2022-11-20T16:00:00Z"],
    [Team.ENG, Team.IRN, "2022-11-21T13:00:00Z"],
    [Team.SEN, Team.NED, "2022-11-21T16:00:00Z"],
    [Team.USA, Team.WAL, "2022-11-21T19:00:00Z"],
    [Team.ARG, Team.KSA, "2022-11-22T10:00:00Z"],
    [Team.DEN, Team.TUN, "2022-11-22T13:00:00Z"],
    [Team.MEX, Team.POL, "2022-11-22T16:00:00Z"],
    [Team.FRA, Team.AUS, "2022-11-22T19:00:00Z"],
    [Team.MAR, Team.CRO, "2022-11-23T10:00:00Z"],
    [Team.GER, Team.JPN, "2022-11-23T13:00:00Z"],
    [Team.ESP, Team.CRC, "2022-11-23T16:00:00Z"],
    [Team.BEL, Team.CAN, "2022-11-23T19:00:00Z"],
    [Team.SUI, Team.CMR, "2022-11-24T10:00:00Z"],
    [Team.URU, Team.KOR, "2022-11-24T13:00:00Z"],
    [Team.POR, Team.GHA, "2022-11-24T16:00:00Z"],
    [Team.BRA, Team.SRB, "2022-11-24T19:00:00Z"],
    [Team.WAL, Team.IRN, "2022-11-25T10:00:00Z"],
    [Team.QAT, Team.SEN, "2022-11-25T13:00:00Z"],
    [Team.NED, Team.ECU, "2022-11-25T16:00:00Z"],
    [Team.ENG, Team.USA, "2022-11-25T19:00:00Z"],
    [Team.TUN, Team.AUS, "2022-11-26T10:00:00Z"],
    [Team.POL, Team.KSA, "2022-11-26T13:00:00Z"],
    [Team.FRA, Team.DEN, "2022-11-26T16:00:00Z"],
    [Team.ARG, Team.MEX, "2022-11-26T19:00:00Z"],
    [Team.JPN, Team.CRC, "2022-11-27T10:00:00Z"],
    [Team.BEL, Team.MAR, "2022-11-27T13:00:00Z"],
    [Team.CRO, Team.CAN, "2022-11-27T16:00:00Z"],
    [Team.ESP, Team.GER, "2022-11-27T19:00:00Z"],
    [Team.CMR, Team.SRB, "2022-11-28T10:00:00Z"],
    [Team.KOR, Team.GHA, "2022-11-28T13:00:00Z"],
    [Team.BRA, Team.SUI, "2022-11-28T16:00:00Z"],
    [Team.POR, Team.URU, "2022-11-28T19:00:00Z"],
    [Team.NED, Team.QAT, "2022-11-29T15:00:00Z"],
    [Team.ECU, Team.SEN, "2022-11-29T15:00:00Z"],
    [Team.WAL, Team.ENG, "2022-11-29T19:00:00Z"],
    [Team.IRN, Team.USA, "2022-11-29T19:00:00Z"],
    [Team.AUS, Team.DEN, "2022-11-30T15:00:00Z"],
    [Team.TUN, Team.FRA, "2022-11-30T15:00:00Z"],
    [Team.POL, Team.ARG, "2022-11-30T19:00:00Z"],
    [Team.KSA, Team.MEX, "2022-11-30T19:00:00Z"],
    [Team.CRO, Team.BEL, "2022-12-01T15:00:00Z"],
    [Team.CAN, Team.MAR, "2022-12-01T15:00:00Z"],
    [Team.JPN, Team.ESP, "2022-12-01T19:00:00Z"],
    [Team.CRC, Team.GER, "2022-12-01T19:00:00Z"],
    [Team.GHA, Team.URU, "2022-12-02T15:00:00Z"],
    [Team.KOR, Team.POR, "2022-12-02T15:00:00Z"],
    [Team.SRB, Team.SUI, "2022-12-02T19:00:00Z"],
    [Team.CMR, Team.BRA, "2022-12-02T19:00:00Z"],
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
