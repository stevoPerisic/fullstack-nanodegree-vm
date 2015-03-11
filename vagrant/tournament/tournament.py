#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import random
import tournamentdb as db

# Tournament classes
def deleteMatches():
    """Remove all the match records from the database."""
    db.deleteAll("matches")

def deletePlayers():
    """Remove all the player records from the database."""
    db.deleteAll("players")

def countPlayers():
    """Returns the number of players currently registered."""
    players = db.fetchAll("players")
    return len(players)

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db.insertRecord('players', ['name'], (name, ))

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    playerStandings = db.fetchAll("leaderboard")
    return playerStandings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    p1 = db.getById("players", winner)
    p2 = db.getById("players", loser)
    db.insertRecord('matches', ['p1', 'p2', 'winner'], (p1[0], p2[0], winner,))
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

    standings = playerStandings()
    i = 0
    matches = []

    for p in standings:
        player1 = standings[i]
        player2 = standings[i+1]
        matches.insert(i, (player1[0], player1[1], player2[0], player2[1]))
        standings.pop(i)
        i = i+1

    return matches



