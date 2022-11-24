from scripts.deploy import deploy
from scripts.teams import Team
from scripts.helpers import get_accounts


MATCHES = [
    [9, 0, 0], # [Team.MAR, Team.CRO, "2022-11-23T10:00:00Z"]
    [10, 1, 2], # [Team.GER, Team.JPN, "2022-11-23T13:00:00Z"]
    [11, 7, 0], # [Team.ESP, Team.CRC, "2022-11-23T16:00:00Z"]
    [12, 1, 0], # [Team.BEL, Team.CAN, "2022-11-23T19:00:00Z"]
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
