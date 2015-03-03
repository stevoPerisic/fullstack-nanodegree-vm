-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;

\c tournament;

CREATE TABLE Players (
	id SERIAL PRIMARY KEY,
	name varchar(40)  
);

CREATE TABLE Matches (
	id SERIAL PRIMARY KEY,
	p1 varchar(40),
	p2 varchar(40),
	winner integer REFERENCES Players(id)
);

INSERT INTO Players (name) VALUES ('Stevo'), ('Bojana');

INSERT INTO Matches (p1, p2, winner) 
VALUES ('Stevo', 'Bojana', 2), ('Bojana', 'Stevo', 1),('Stevo', 'Bojana', 1);

CREATE VIEW getAllMatches_byPlayer AS
	SELECT name, count(*) as matches_played
	FROM Players
	LEFT JOIN Matches 
	ON Players.name = Matches.p1 OR Players.name = Matches.p2
	GROUP BY Players.name;

CREATE VIEW getAllWins_byPlayer AS
	SELECT name, count(*) as wins
	FROM Players
	LEFT JOIN Matches 
	ON Players.id = Matches.winner
	GROUP BY Players.name;

CREATE VIEW getStandings AS
	SELECT name, count(*) as wins
	FROM Players
	LEFT JOIN Matches 
	ON Players.id = Matches.winner
	GROUP BY Players.name
	ORDER BY wins DESC;

