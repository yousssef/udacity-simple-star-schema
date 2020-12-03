# DROP TABLES 

songplay_table_drop = "DROP TABLE  IF EXISTS  songplays"
user_table_drop = "DROP TABLE  IF EXISTS users "
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS  artists"
time_table_drop = "DROP TABLE IF EXISTS time "

# CREATE TABLE IF NOT EXISTSS

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays 
(songplay_id SERIAL PRIMARY KEY, start_time float8, user_id VARCHAR(50), level VARCHAR(10), song_id  VARCHAR(50), artist_id text, session_id int, location text, user_agent text)""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (user_id VARCHAR(50), first_name  VARCHAR(100), last_name  VARCHAR(100), gender char(1), level VARCHAR(10))""")
#ok
song_table_create = ("CREATE TABLE IF NOT EXISTS songs (song_id text, title text, artist_id text, year INT, duration float8 )")

artist_table_create = ("CREATE TABLE IF NOT EXISTS artists (artist_id text, name VARCHAR(100), location VARCHAR(100), latitude FLOAT8, longitude FLOAT8)")
#ok
time_table_create = ("CREATE TABLE IF NOT EXISTS time (start_time time, hour INT, day INT, week INT, month INT, year INT, weekday INT )")
#ok
# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays
( start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES (%s, %s,%s, %s, %s,%s, %s, %s)
""")

user_table_insert = ("""INSERT INTO users
(user_id, first_name, last_name, gender, level) 
VALUES (%s, %s, %s, %s, %s)
""")

song_table_insert = ("""INSERT INTO songs
(song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""INSERT INTO artists
(artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
""")


time_table_insert = ("""INSERT INTO time
(start_time, hour, day, week, month, year, weekday)
VALUES (%s, %s, %s, %s, %s, %s, %s)
""")

# FIND SONGS , song_id and artist_id from the inner join of songs and artists

song_select = ("""select song_id, songs.artist_id from songs inner join artists on artists.artist_id=songs.artist_id where title like %s and artists.name like %s and duration=%s""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]