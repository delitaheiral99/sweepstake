from scripts.deploy import deploy
from scripts.teams import Team
import os
import json
from datetime import datetime

# File created for integration with the frontend dapp
def calculate_points():
    contract = deploy()

    # Get players
    playerCount = contract.playerCount()
    ranking = {
        "stats": {
            "playerCount": playerCount,
            "betCount": contract.betCount(),
            "totalAmount": contract.balance() * 0.000000000000000001,
        },
        "ranking": []
    }
    for i in range(1, playerCount + 1):
        player = contract.players(i)
        points = contract.points(player)
        ranking['ranking'].append({
            'wallet': player,
            'points': points
        })

    # Write to file
    with open(os.environ['JSON_PATH'] + '/ranking.json', 'w') as outfile:
        json.dump(ranking, outfile, indent=4)


def main():
    calculate_points()
