from pybaseball import  playerid_lookup
from pybaseball import  statcast_batter

player_id = playerid_lookup('chisholm', 'jazz')

#   name_last  name_first  key_mlbam  key_retro  key_bbref  key_fangraphs  mlb_played_first  mlb_played_last
#   chisholm   jazz        665862     chisj001   chishja01  20454          2020.0            2024.0

data = statcast_batter('2020-01-01', '2024-10-30', 665862)

home_runs = data[data['events'] == 'home_run']

home_runs[['game_year', 'game_date', 'game_type', 'home_team', 'away_team', 
           'pitcher', 'pitch_type', 'pitch_name', 'launch_speed', 'launch_angle', 
           'hit_distance_sc', 'hc_x', 'hc_y']].to_csv('jazz_home_runs.csv', index=False)