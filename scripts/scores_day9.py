from scripts.deploy import deploy
from scripts.teams import Team
from scripts.helpers import get_accounts


MATCHES = [
    [33, 2, 0], # [Team.NED, Team.QAT, "2022-11-29T15:00:00Z"], #33
    [34, 1, 2], # [Team.ECU, Team.SEN, "2022-11-29T15:00:00Z"], #34
    [35, 0, 3], # [Team.WAL, Team.ENG, "2022-11-29T19:00:00Z"], #35
    [36, 0, 1], # [Team.IRN, Team.USA, "2022-11-29T19:00:00Z"], #36
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
