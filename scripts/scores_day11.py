from scripts.deploy import deploy
from scripts.teams import Team
from scripts.helpers import get_accounts


MATCHES = [
    [41, 0, 0], # [Team.CRO, Team.BEL, "2022-12-01T15:00:00Z"], #41
    [42, 1, 2], # [Team.CAN, Team.MAR, "2022-12-01T15:00:00Z"], #42
    [43, 2, 1], # [Team.JPN, Team.ESP, "2022-12-01T19:00:00Z"], #43
    [44, 2, 4], # [Team.CRC, Team.GER, "2022-12-01T19:00:00Z"], #44
]

# File created for integration with the frontend dapp
def add_scores():
    contract = deploy()
    accounts = get_accounts()
    playerCount = contract.playerCount()

    #update matches scores
    for match in MATCHES:
        bets = []

        #get all bets for the match
        for i in range(1, playerCount + 1):
            player = contract.players(i)
            bet = contract.betByPlayerGame(player, match[0])
            if (bet > 0):
                bets.append(bet)

        #update match score
        contract.updateScore(
            match[0],
            match[1],
            match[2],
            {'from': accounts['main_wallet']}
        )

        #update player points
        contract.updatePoints(match[0], bets, {'from': accounts['main_wallet']})


def main():
    add_scores()
