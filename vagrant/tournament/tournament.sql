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
	name TEXT ,
	id SERIAL PRIMARY KEY
);

CREATE TABLE Matches (
	id SERIAL PRIMARY KEY,
	p1 TEXT,
	p2 TEXT,
	winner INTEGER REFERENCES Players(id)
);

INSERT INTO Players (name) VALUES ('Stevo'), ('Bojana'), ('Lana'), ('Dukara');

INSERT INTO Matches (p1, p2, winner) 
VALUES	('Stevo', 'Bojana', 2), 
		('Lana', 'Dukara', 3),
		('Bojana', 'Lana', 3),
		('Stevo', 'Dukara', 4);

CREATE VIEW getMatches_byPlayer AS
SELECT players.id, players.name,
(select count(*) from matches where players.name in (p1, p2)) as matches_played
FROM players
ORDER BY players.id;

CREATE VIEW getAllWins_byPlayer AS
SELECT players.id, players.name,
(select count(*) from matches where matches.winner = players.id) as matches_won
FROM players
ORDER BY matches_won DESC;

-- get leaderboard :) finally
create view leaderboard as
select players.id, players.name, v2.matches_won, v1.matches_played from players 
left join (select * from getMatches_byPlayer) as v1 on players.id = v1.id 
left join (select * from getAllWins_byPlayer) as v2 on players.id = v2.id
order by v2.matches_won desc;


