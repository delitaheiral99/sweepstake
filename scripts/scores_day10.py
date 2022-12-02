from scripts.deploy import deploy
from scripts.teams import Team
from scripts.helpers import get_accounts


MATCHES = [
    [37, 1, 0], # [Team.AUS, Team.DEN, "2022-11-30T15:00:00Z"], #37
    [38, 1, 0], # [Team.TUN, Team.FRA, "2022-11-30T15:00:00Z"], #38
    [39, 0, 2], # [Team.POL, Team.ARG, "2022-11-30T19:00:00Z"], #39
    [40, 1, 2], # [Team.KSA, Team.MEX, "2022-11-30T19:00:00Z"], #40
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
