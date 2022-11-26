from scripts.deploy import deploy
from scripts.teams import Team
from scripts.helpers import get_accounts


MATCHES = [
    [17, 0, 1], # [Team.TUN, Team.AUS, "2022-11-26T10:00:00Z"], #21
    [18, 2, 0], # [Team.POL, Team.KSA, "2022-11-26T13:00:00Z"], #22
    [19, 2, 1], # [Team.FRA, Team.DEN, "2022-11-26T16:00:00Z"], #23
    [20, 2, 0], # [Team.ARG, Team.MEX, "2022-11-26T19:00:00Z"], #24
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
