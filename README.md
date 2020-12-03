### Project Summary
This is an etl in python that feeds a star schema with data from JSON files in series format.
The data is from a music streaming app, and contains info such as but not limited to:
songs: song_id, title, artist_id, year, duration
users of the app: user_id, first_name, last_name, gender, level
artists: artist_id, name, location, latitude, longitude
song plays: start_time , user_id , level, song_id, artist_id, session_id, location, user_agent

### how to run the Python scripts
run etl.py with no params
### and an explanation of the files in the repository. 
#### create_tables.py
As its name suggests creates posgres tables to fill with data.
#### sql_queries.py
Keeps the SQL queries out of the main file for readabilty and separation of concern
#### etl.py
is the main file , it first calls the create tables to prepare the environnement, then it iterates over all the Json files from the directory.
It applies the process_song function to song files one by one. and does process_log to the log files.
process_song consists into filling song_data and artist_data
process_logs deals with time, users song_plays as these are present in the log files.