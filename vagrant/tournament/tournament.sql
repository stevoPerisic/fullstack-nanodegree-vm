-- Table definitions for the tournament project.

-- Create the tournamnet database
CREATE DATABASE tournament;

-- Connect to the database using the psql \c command
\c tournament;

-- table players
-- example:
--        name       | id 
-- ------------------+----
--  Twilight Sparkle | 12
--  Fluttershy       | 13
--  Applejack        | 14
--  Pinkie Pie       | 15
CREATE TABLE players (
	name TEXT ,
	id SERIAL PRIMARY KEY
);

-- table matches
-- example:
-- id |      p1      |      p2      | winner 
-- ----+--------------+--------------+--------
--   1 | Bruno Walton | Boots O'Neal |      8
--   2 | Cathy Burton | Diane Grant  |     10
CREATE TABLE matches (
	id SERIAL PRIMARY KEY,
	p1 TEXT,
	p2 TEXT,
	winner INTEGER REFERENCES players(id)
);

-- view that gives us all the matches played by players, sorted by player.id
-- example:
-- id |     name     | matches_played 
-- ----+--------------+----------------
--   8 | Bruno Walton |              1
--   9 | Boots O'Neal |              1
--  10 | Cathy Burton |              1
--  11 | Diane Grant  |              1
CREATE VIEW matchesPlayed AS
SELECT players.id, players.name,
(select count(*) from matches where players.name in (p1, p2)) as matches_played
FROM players
ORDER BY players.id;

-- view that gices us all the matches won by players, sorted by most wins
-- example:
--  id |     name     | matches_won 
-- ----+--------------+-------------
--   8 | Bruno Walton |           1
--  10 | Cathy Burton |           1
--   9 | Boots O'Neal |           0
--  11 | Diane Grant  |           0
CREATE VIEW matchesWon AS
SELECT players.id, players.name,
(select count(*) from matches where matches.winner = players.id) as matches_won
FROM players
ORDER BY matches_won DESC;

-- view that gives us the leaderboard
-- example:
--  id |     name     | matches_won | matches_played 
-- ----+--------------+-------------+----------------
--   8 | Bruno Walton |           1 |              1
--  10 | Cathy Burton |           1 |              1
--   9 | Boots O'Neal |           0 |              1
--  11 | Diane Grant  |           0 |              1
create view leaderboard as
select players.id, players.name, v2.matches_won, v1.matches_played from players 
left join (select * from matchesPlayed) as v1 on players.id = v1.id 
left join (select * from matchesWon) as v2 on players.id = v2.id
order by v2.matches_won desc;


