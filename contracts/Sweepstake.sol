// SPDX-License-Identifier: MIT
pragma solidity ^0.8.4;

import "@openzeppelin/contracts/access/Ownable.sol";

contract Sweepstake is Ownable {
    struct Game {
        uint8 team1Score;
        uint8 team2Score;
        uint8 team1; // dapp knows which team is which
        uint8 team2; // dapp knows which team is which
        uint32 startTime;
    }
    uint8 public gameCount;
    uint256[] public gameIds;
    mapping(uint256 => Game) public games;

    struct Bet {
        uint8 gameId;
        uint8 team1Score;
        uint8 team2Score;
        address player;
    }
    uint256 public betCount;
    uint256[] public betIds;
    mapping(uint256 => Bet) public bets;

    uint256 public registrationFee;
    uint256 public betFee;
    uint256 public pointForResult;
    uint256 public pointForScore;
    uint256 public bonusPoints;

    uint256 public playerCount;
    mapping(uint256 => address) public players;
    mapping(address => bool) public registeredPlayers;
    mapping(address => uint256) public points;
    mapping(address => uint256[]) public playerBets;
    mapping(uint256 => uint256[]) public gameBets;
    mapping(address => mapping(uint256 => uint256)) public betByPlayerGame;

    event GameCreated(
        uint8 id,
        uint8 team1,
        uint8 team2,
        uint32 startTime
    );
    event GameUpdated(
        uint8 id,
        uint8 team1,
        uint8 team2,
        uint32 startTime
    );
    event ScoreUpdated(
        uint8 id,
        uint8 team1Score,
        uint8 team2Score
    );
    event BetPlaced(
        uint8 gameId,
        uint8 team1Score,
        uint8 team2Score,
        address player
    );
    event BetUpdated(
        uint8 gameId,
        uint8 team1Score,
        uint8 team2Score,
        address player
    );
    event PlayerRegistered(address player);
    event PointsUpdated(address player, uint256 points);
    event RegistrationFeeUpdated(uint256 registrationFee);
    event BetFeeUpdated(uint256 betFee);
    event PointForResultUpdated(uint256 pointForResult);
    event PointForScoreUpdated(uint256 pointForScore);
    event BonusPointsUpdated(uint256 bonusPoints);
    event Withdraw(address owner, uint256 amount);

    constructor() {
        registrationFee = 0.1 ether;
        betFee = 0.01 ether;
        pointForResult = 4;
        pointForScore = 2;
        bonusPoints = 2;
    }

    function createGame(uint8 team1, uint8 team2, uint32 startTime) external onlyOwner {
        require(team1 != team2, "Teams must be different");
        require(team1 > 0 && team2 > 0, "Teams must be greater than 0");
        require(startTime > block.timestamp, "Start time must be in the future");
        gameCount++;
        gameIds.push(gameCount);
        games[gameCount] = Game(0, 0, team1, team2, startTime);
        emit GameCreated(gameCount, team1, team2, startTime);
    }

    function updateGame(uint8 id, uint8 team1, uint8 team2, uint32 startTime) external onlyOwner {
        require(team1 != team2, "Teams must be different");
        require(team1 > 0 && team2 > 0, "Teams must be greater than 0");
        require(games[id].team1 != team1 || games[id].team2 != team2, "Teams must be different");
        games[id].team1 = team1;
        games[id].team2 = team2;
        games[id].startTime = startTime;
        emit GameUpdated(id, team1, team2, startTime);
    }

    function updateScore(uint8 id, uint8 team1Score, uint8 team2Score) external onlyOwner {
        games[id].team1Score = team1Score;
        games[id].team2Score = team2Score;
        emit ScoreUpdated(id, team1Score, team2Score);
    }

    function register() public payable {
        require(!registeredPlayers[msg.sender], "Player is already registered");
        require(msg.value == registrationFee, "Registration fee is not correct");
        playerCount++;
        registeredPlayers[msg.sender] = true;
        players[playerCount] = msg.sender;
        emit PlayerRegistered(msg.sender);
    }

    function placeBet(uint8 gameId, uint8 team1Score, uint8 team2Score) external payable {
        require(registeredPlayers[msg.sender], "Player is not registered");
        require(msg.value == betFee, "Bet fee is not correct");
        require(games[gameId].team1 > 0, "Game does not exist");
        require(games[gameId].startTime > block.timestamp, "Game has already started");
        require(betByPlayerGame[msg.sender][gameId] == 0, "Player has already placed a bet for this game");
        Bet memory bet = Bet(gameId, team1Score, team2Score, msg.sender);
        betCount++;
        betIds.push(betCount);
        bets[betCount] = bet;
        playerBets[msg.sender].push(betCount);
        gameBets[gameId].push(betCount);
        betByPlayerGame[msg.sender][gameId] = betCount;
        emit BetPlaced(gameId, team1Score, team2Score, msg.sender);
    }

    function updateBet(uint8 gameId, uint8 team1Score, uint8 team2Score) external payable {
        require(msg.value == betFee, "Bet fee is not correct");
        require(betByPlayerGame[msg.sender][gameId] > 0, "Player has not placed a bet for this game");
        uint256 betId = betByPlayerGame[msg.sender][gameId];
        Bet storage bet = bets[betId];
        bet.team1Score = team1Score;
        bet.team2Score = team2Score;
        emit BetUpdated(gameId, team1Score, team2Score, msg.sender);
    }

    function updatePoints(uint8 gameId, uint256[] memory _betIds) external onlyOwner {
        uint256 _points;
        Game memory game = games[gameId];
        for (uint256 i = 0; i < _betIds.length; i++) {
            _points = 0;
            Bet memory bet = bets[_betIds[i]];
            if (bet.gameId == gameId) {
                if (game.team1Score > game.team2Score && bet.team1Score > bet.team2Score) { // team1 win
                    _points += pointForResult;
                } else if (game.team1Score < game.team2Score && bet.team1Score < bet.team2Score) { // team2 win
                    _points += pointForResult;
                } else if (game.team1Score == game.team2Score && bet.team1Score == bet.team2Score) { // draw
                    _points += pointForResult;
                }

                //team1 score
                if (game.team1Score == bet.team1Score) {
                    _points += pointForScore;
                }

                //team2 score
                if (game.team2Score == bet.team2Score) {
                    _points += pointForScore;
                }

                //bonus points
                if (_points == pointForResult + pointForScore * 2) {
                    _points += bonusPoints;
                }

                points[bet.player] += _points;
                emit PointsUpdated(bet.player, _points);
            }
        }
    }

    // dev: adding this function as a fallback to reset the points
    // dev: in case of a manual mistake
    function resetPoints(uint256[] memory _playerIds) external onlyOwner {
        for (uint256 i = 0; i < _playerIds.length; i++) {
            points[players[_playerIds[i]]] = 0;
            emit PointsUpdated(players[_playerIds[i]], 0);
        }
    }

    function setPointsforResult(uint256 _pointForResult) external onlyOwner {
        pointForResult = _pointForResult;
        emit PointForResultUpdated(_pointForResult);
    }

    function setPointsforScore(uint256 _pointForScore) external onlyOwner {
        pointForScore = _pointForScore;
        emit PointForScoreUpdated(_pointForScore);
    }

    function setBonusPoints(uint256 _bonusPoints) external onlyOwner {
        bonusPoints = _bonusPoints;
        emit BonusPointsUpdated(_bonusPoints);
    }

    function setRegistrationFee(uint256 _registrationFee) external onlyOwner {
        registrationFee = _registrationFee;
        emit RegistrationFeeUpdated(_registrationFee);
    }

    function setBetFee(uint256 _betFee) external onlyOwner {
        betFee = _betFee;
        emit BetFeeUpdated(_betFee);
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        emit Withdraw(msg.sender, balance);
        payable(msg.sender).transfer(balance);
    }

    function getGame(uint8 id) external view returns (uint8, uint8, uint8, uint8, uint32) {
        return (
            games[id].team1Score,
            games[id].team2Score,
            games[id].team1,
            games[id].team2,
            games[id].startTime
        );
    }

    function getBet(uint256 id) external view returns (uint8, uint8, uint8, address) {
        return (
            bets[id].gameId,
            bets[id].team1Score,
            bets[id].team2Score,
            bets[id].player
        );
    }

    receive() external payable {
        register();
    }

    fallback() external payable {
        register();
    }
}
