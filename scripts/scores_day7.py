from scripts.deploy import deploy
from scripts.teams import Team
from scripts.helpers import get_accounts


MATCHES = [
    [25, 0, 1], # [Team.JPN, Team.CRC, "2022-11-27T10:00:00Z"], #25
    [26, 0, 2], # [Team.BEL, Team.MAR, "2022-11-27T13:00:00Z"], #26
    [27, 4, 1], # [Team.CRO, Team.CAN, "2022-11-27T16:00:00Z"], #27
    [28, 1, 1], # [Team.ESP, Team.GER, "2022-11-27T19:00:00Z"], #28
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
