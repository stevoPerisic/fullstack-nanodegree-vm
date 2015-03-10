#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#


# import psycopg2 library
import psycopg2

import random


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("""DELETE FROM matches *""")
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()
    c.execute("""DELETE FROM players *""")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    c = db.cursor()
    c.execute("""SELECT * FROM players""")
    players = c.fetchall()
    db.close()
    return len(players)


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    c.execute('INSERT INTO players (name) VALUES (%s)', (name,))
    db.commit()
    db.close()


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
    db = connect()
    c = db.cursor()
    query = """SELECT * FROM leaderboard"""
    c.execute(query)
    playerStandings = c.fetchall()
    return playerStandings
    db.close()

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()
    c.execute('SELECT players.name FROM players WHERE players.id = %s', (winner,))
    p1 = c.fetchall()
    c.execute('SELECT players.name FROM players WHERE players.id = %s', (loser,))
    p2 = c.fetchall()
    c.execute('INSERT INTO matches (p1, p2, winner) VALUES (%s, %s, %s)',  (p1[0], p2[0], winner,))
    db.commit()
    db.close()
 
 
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
    # [id1, id2, id3, id4] = [row[0] for row in standings]
    # swissPairings()
    # print standings[0]
    i = 0
    matches = []
    for p in standings:
        player1 = standings[i]
        player2 = standings[i+1]

        print ("--Match--(%s)"%(i+1))
        print player1
        print player2
        print ("---------")
        matches.insert(i, (player1[0], player1[1], player2[0], player2[1]))
        standings.pop(i)

        i = i+1

    return matches



