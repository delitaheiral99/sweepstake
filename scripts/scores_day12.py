from scripts.deploy import deploy
from scripts.teams import Team
from scripts.helpers import get_accounts


MATCHES = [
    [45, 0, 2], # [Team.GHA, Team.URU, "2022-12-02T15:00:00Z"], #45
    [46, 2, 1], # [Team.KOR, Team.POR, "2022-12-02T15:00:00Z"], #46
    [47, 2, 3], # [Team.SRB, Team.SUI, "2022-12-02T19:00:00Z"], #47
    [48, 1, 0], # [Team.CMR, Team.BRA, "2022-12-02T19:00:00Z"], #48
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
