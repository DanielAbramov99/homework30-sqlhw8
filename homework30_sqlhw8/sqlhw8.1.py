# CREATE TABLE IF NOT EXISTS competition_by_year(
# competition_year INTEGER PRIMARY KEY,
# hosting_country TEXT NOT NULL
# );
#
# CREATE TABLE IF NOT EXISTS countries(
# name TEXT PRIMARY KEY ,
# language TEXT NOT NULL,
# capital, TEXT NOT NULL
# );
#
# CREATE TABLE IF NOT EXISTS songs(
# name TEXT PRIMARY KEY,
# language TEXT NOT NULL,
# singer TEXT NOT NULL,
# country_won TEXT NOT NULL,
# FOREIGN KEY (country_won) REFERENCES countries(name)
# );

# INSERT OR IGNORE INTO competition_by_year VALUES('2012','Azerbaijan');
# INSERT OR IGNORE INTO competition_by_year VALUES('2013','Sweden');
# INSERT OR IGNORE INTO competition_by_year VALUES('2014','Denmark');
# INSERT OR IGNORE INTO competition_by_year VALUES('2015','Austria');
# INSERT OR IGNORE INTO competition_by_year VALUES('2016','Sweden');
# INSERT OR IGNORE INTO competition_by_year VALUES('2017','Ukraine');
# INSERT OR IGNORE INTO competition_by_year VALUES('2018','Portugal');
# INSERT OR IGNORE INTO competition_by_year VALUES('2019','Israel');
# INSERT OR IGNORE INTO competition_by_year VALUES('2021','Netherlands');
# INSERT OR IGNORE INTO competition_by_year VALUES('2022','Italy');
# INSERT OR IGNORE INTO competition_by_year VALUES('2023','United Kingdom');
# INSERT OR IGNORE INTO competition_by_year VALUES('2024','Sweden');

# INSERT OR IGNORE INTO countries VALUES('Azerbaijan','Azerbaijani','Baku');
# INSERT OR IGNORE INTO countries VALUES('Sweden','Swedish','Stockholm');
# INSERT OR IGNORE INTO countries VALUES('Denmark','Danish','Copenhagen');
# INSERT OR IGNORE INTO countries VALUES('Austria','German','Vienna');
# INSERT OR IGNORE INTO countries VALUES('Ukraine','Ukrainian','Kyiv');
# INSERT OR IGNORE INTO countries VALUES('Portugal','Portuguese','Lisbon');
# INSERT OR IGNORE INTO countries VALUES('Israel','Hebrew','Jerusalem');
# INSERT OR IGNORE INTO countries VALUES('Netherlands','Dutch','Amsterdam');
# INSERT OR IGNORE INTO countries VALUES('Italy','Italian','Rome');
# INSERT OR IGNORE INTO countries VALUES('United Kingdom','English','London');
# INSERT OR IGNORE INTO countries VALUES('Switzerland','German','Bern');

# INSERT OR IGNORE INTO songs VALUES ('The Code', 'English', 'Nemo', 'Switzerland');
# INSERT OR IGNORE INTO songs VALUES ('Tattoo', 'English', 'Loreen', 'Sweden');
# INSERT OR IGNORE INTO songs VALUES ('Stefania', 'Ukrainian', 'Kalush Orchestra', 'Ukraine');
# INSERT OR IGNORE INTO songs VALUES ('Zitti e buoni', 'Italian', 'Måneskin', 'Italy');
# INSERT OR IGNORE INTO songs VALUES ('Arcade', 'English', 'Duncan Laurence', 'Netherlands');
# INSERT OR IGNORE INTO songs VALUES ('Toy', 'English', 'Netta', 'Israel');
# INSERT OR IGNORE INTO songs VALUES ('Amar pelos dois', 'Portuguese', 'Salvador Sobral', 'Portugal');
# INSERT OR IGNORE INTO songs VALUES ('1944', 'English/Ukrainian', 'Jamala', 'Ukraine');
# INSERT OR IGNORE INTO songs VALUES ('Heroes', 'English', 'Måns Zelmerlöw', 'Sweden');
# INSERT OR IGNORE INTO songs VALUES ('Rise Like a Phoenix', 'English', 'Conchita Wurst', 'Austria');
# INSERT OR IGNORE INTO songs VALUES ('Only Teardrops', 'English', 'Emmelie de Forest', 'Denmark');
# INSERT OR IGNORE INTO songs VALUES ('Euphoria', 'English', 'Loreen', 'Sweden');

# this query shows only each song that one and his complete information
# SELECT s.name AS song_name, s.language AS song_language, s.singer,
#        c.name AS country_name, c.language AS country_language, c.capital AS country_capital
# FROM songs s
# JOIN countries c ON s.country_won = c.name;

# this query shows each competition year as well complete information about hosting country
# SELECT *
# FROM competition_by_year comp
# LEFT JOIN countries c ON comp.hosting_country = c.name;