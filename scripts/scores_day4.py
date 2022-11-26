from scripts.deploy import deploy
from scripts.teams import Team
from scripts.helpers import get_accounts


MATCHES = [
    [13, 1, 0], # [Team.SUI, Team.CMR, "2022-11-24T10:00:00Z"], #13
    [14, 0, 0], # [Team.URU, Team.KOR, "2022-11-24T13:00:00Z"], #14
    [15, 3, 2], # [Team.POR, Team.GHA, "2022-11-24T16:00:00Z"], #15
    [16, 2, 0], # [Team.BRA, Team.SRB, "2022-11-24T19:00:00Z"], #16
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
