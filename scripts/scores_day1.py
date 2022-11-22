from scripts.deploy import deploy
from scripts.teams import Team

MATCHES = [
    [1, 0, 2],
    [2, 6, 2],
    [3, 0, 2],
    [4, 1, 1],
]

# File created for integration with the frontend dapp
def add_scores():
    contract = deploy()

    playerCount = contract.playerCount()
    bets = []

    #update matches scores
    for match in MATCHES:
        #contract.updateScore(match[0], match[1], match[2])
        for i in range(1, playerCount + 1):
            player = a.players(i)
            bet = contract.betByPlayerGame(player, match[0])
            bets.append(bet)

        #update players scores
        print(bets)
        #contract.updatePoints(match[0], bets)


def main():
    add_scores()
