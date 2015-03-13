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
	<li>Run <code>python tournament_test.py</code></li>
	<li>All the tests should be passing</li>
</ol>



