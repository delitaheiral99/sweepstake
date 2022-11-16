from scripts.deploy import deploy
from scripts.teams import Team
import os
import json
from datetime import datetime

# File created for integration with the frontend dapp
def write_game_json():
    contract = deploy()

    # Get matches
    gameCount = contract.gameCount()
    games = {"games": []}
    for i in range(1, gameCount + 1):
        game = contract.games(i)
        games['games'].append({
            'id': i,
            'date': datetime.utcfromtimestamp(game[4]).strftime('%a %d %b %H:%M GMT'),
            'team1': Team(game[2]).name,
            'team2': Team(game[3]).name,
        })

    # Write to file
    with open(os.environ['JSON_PATH'] + '/games.json', 'w') as outfile:
        json.dump(games, outfile, indent=4)


def main():
    write_game_json()
