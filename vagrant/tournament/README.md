## Project 2 - Swiss Tournament Planner

This project has two parts:

1) Defining the database schema (SQL table definitions)

The database schema is defined in the tournament.sql file. I will name the database tournament and it will have two simple tables named players and matches. The players table will store information about the players, namely id and name. I will declare the id to be a unique id using the SERIAL data type and declaring it a primary key. Name will be of type text. The matches table will also have a unique id along with p1, p2 and winner columns to hold the first and second players names and winner's id as a foreign key respectively. 

Next I will create several views which will store some of our more complex select statements that I will use regularly. First view will get all matches played by a single player, next view will get all matches won by a player and third I want a leaderboard to list all players, their ids, number of matches played and number of games won.

This database schema will allow me to access and modify the data in the way that suits the requirements of this project.

2) Writing the code that will use it.

I will use the tests written in the tournament_test.py file as a guide on how to write the classes defined in the tournament.py module. 


-------------------------

This is a Python module that uses the PostgreSQL database to keep track
of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in 
each round: players are not eliminated, and each player should be paired with another player with teh samenumber of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.

-------------------------

## Requirements

<ol>
	<li>Clone this repository and cd into it.</li>
	<li>Run <code>vagrant up</code> to start the VM</li>
	<li>log into the VM using <code>vagrant ssh</code></li>
	<li>to do</li>
</ol>

## Installation and running



