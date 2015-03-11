-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players (
	name TEXT ,
	id SERIAL PRIMARY KEY
);

CREATE TABLE matches (
	id SERIAL PRIMARY KEY,
	p1 TEXT,
	p2 TEXT,
	winner INTEGER REFERENCES players(id)
);


CREATE VIEW matchesPlayed AS
SELECT players.id, players.name,
(select count(*) from matches where players.name in (p1, p2)) as matches_played
FROM players
ORDER BY players.id;

CREATE VIEW matchesWon AS
SELECT players.id, players.name,
(select count(*) from matches where matches.winner = players.id) as matches_won
FROM players
ORDER BY matches_won DESC;

-- get leaderboard :) finally
create view leaderboard as
select players.id, players.name, v2.matches_won, v1.matches_played from players 
left join (select * from matchesPlayed) as v1 on players.id = v1.id 
left join (select * from matchesWon) as v2 on players.id = v2.id
order by v2.matches_won desc;


