from scripts.deploy import deploy
from scripts.teams import Team


MATCHES = [
    [1, 0, 2], # [Team.QAT, Team.ECU, "2022-11-20T16:00:00Z"]
    [2, 6, 2], # [Team.ENG, Team.IRN, "2022-11-21T13:00:00Z"]
    [3, 0, 2], # [Team.SEN, Team.NED, "2022-11-21T16:00:00Z"]
    [4, 1, 1], # [Team.USA, Team.WAL, "2022-11-21T19:00:00Z"]
]

# File created for integration with the frontend dapp
def add_scores():
    contract = deploy()

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
        contract.updateScore(match[0], match[1], match[2])

        #update player points
        contract.updatePoints(match[0], bets)


def main():
    add_scores()
