## Project 2 - Swiss Tournament Planner

This is a Python module that uses the PostgreSQL database to keep track
of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in 
each round: players are not eliminated, and each player should be paired 
with another player with the same number of wins, or as close as possible.


## Requirements
<ul>
	<li>Vagrant VM</li>
	<li>Python 2.7.9 or later</li>
</ul>


## Installation and running
<ol>
	<li>Clone this repository and cd into it.</li>
	<li>Run <code>vagrant up</code> to start the VM</li>
	<li>Log into the VM using <code>vagrant ssh</code></li>
	<li>Change your directory to /vagrant/tournament/</li>
	<li>Start a psql prompt with <code>psql</code></li>
	<li>You should be connected to the vagrant database</li>
	<li>Install the tournament database with <code>\i tournament.sql</code><br/>
		This should be your output:<br/>
		<code width="400px">
			vagrant=> \i tournament.sql<br/><br/>
			CREATE DATABASE<br/>
			You are now connected to database "tournament" as user "vagrant".<br/>
			CREATE TABLE<br/>
			CREATE TABLE<br/>
			CREATE VIEW<br/>
			CREATE VIEW<br/>
			CREATE VIEW<br/>
			tournament=><br/>
		</code>
	</li>
	<li>Quit the psql prompt with <code>\q</code></li>
	<li>Run <code>python tournament_test.py</code></li>
	<li>All the tests should be passing</li>
</ol>



