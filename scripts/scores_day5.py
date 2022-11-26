from scripts.deploy import deploy
from scripts.teams import Team
from scripts.helpers import get_accounts


MATCHES = [
    [17, 0, 2], # [Team.WAL, Team.IRN, "2022-11-25T10:00:00Z"], #17
    [18, 1, 3], # [Team.QAT, Team.SEN, "2022-11-25T13:00:00Z"], #18
    [19, 1, 1], # [Team.NED, Team.ECU, "2022-11-25T16:00:00Z"], #19
    [20, 0, 0], # [Team.ENG, Team.USA, "2022-11-25T19:00:00Z"], #20
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
