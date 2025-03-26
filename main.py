from pybaseball import  playerid_lookup, statcast_batter, playerid_reverse_lookup

player_id = playerid_lookup('chisholm', 'jazz')

#   name_last  name_first  key_mlbam  key_retro  key_bbref  key_fangraphs  mlb_played_first  mlb_played_last
#   chisholm   jazz        665862     chisj001   chishja01  20454          2020.0            2024.0

data = statcast_batter('2020-01-01', '2025-12-12', 665862)

home_runs = data[data['events'] == 'home_run'].copy()

def get_pitcher_name(pitcher_id):
    try:
        lookup = playerid_reverse_lookup([pitcher_id], key_type='mlbam')
        if not lookup.empty:
            first_name = lookup.iloc[0]['name_first']
            last_name = lookup.iloc[0]['name_last']
            return f"{first_name} {last_name}"
        return None
    except Exception:
        return None

home_runs.loc[:, 'pitcher_name'] = home_runs['pitcher'].apply(get_pitcher_name)

home_runs[['game_year', 'game_date', 'game_type', 'home_team', 'away_team', 
           'pitcher', 'pitcher_name', 'pitch_type', 'pitch_name', 'launch_speed', 'launch_angle', 
           'hit_distance_sc', 'hc_x', 'hc_y']].to_csv('jazz_home_runs.csv', index=False, encoding='utf-8-sig')