from scripts.deploy import deploy
from scripts.teams import Team
from scripts.helpers import get_accounts


MATCHES = [
    [29, 3, 3], # [Team.CMR, Team.SRB, "2022-11-28T10:00:00Z"], #29
    [30, 2, 3], # [Team.KOR, Team.GHA, "2022-11-28T13:00:00Z"], #30
    [31, 1, 0], # [Team.BRA, Team.SUI, "2022-11-28T16:00:00Z"], #31
    [32, 2, 0], # [Team.POR, Team.URU, "2022-11-28T19:00:00Z"], #32
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
