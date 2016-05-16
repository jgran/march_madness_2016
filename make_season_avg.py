import pandas as pd
import numpy as np

print '\n'
print 'calculating season averages for each team for each season'

#read in stats for regular season games and team ID numbers
season_df = pd.read_csv('input/RegularSeasonDetailedResults.csv')
teams_df = pd.read_csv('input/Teams.csv')

#split game stats into two data frames to faciliate calculating season averages for each team
win_df = season_df[['Season','Wteam','Wscore','Wfgm','Wfga','Wfgm3','Wfga3','Wftm','Wfta','Wor','Wdr','Wast','Wto','Wstl','Wblk','Wpf']]
lose_df = season_df[['Season','Lteam','Lscore','Lfgm','Lfga','Lfgm3','Lfga3','Lftm','Lfta','Lor','Ldr','Last','Lto','Lstl','Lblk','Lpf']]

win_df.columns = ['Season','Team','score','fgm','fga','fgm3','fga3','ftm','fta','or','dr','ast','to','stl','blk','pf']
lose_df.columns = ['Season','Team','score','fgm','fga','fgm3','fga3','ftm','fta','or','dr','ast','to','stl','blk','pf']

#combine win and lose data frames, then each row has stats for a single team
season_df = pd.concat([win_df, lose_df])

#create dataframe to hold season avg stats and fill for each team and season
seasons = pd.unique(season_df.Season.ravel())
teams = pd.unique(teams_df.Team_Id.ravel())
avg_df = pd.DataFrame({
    'Season':[0],
    'Team':[0],
    'score':[0],
    'fgm':[0],
    'fga':[0],
    'fgm3':[0],
    'fga3':[0],
    'ftm':[0],
    'fta':[0],
    'or':[0],
    'dr':[0],
    'ast':[0],
    'to':[0],
    'stl':[0],
    'blk':[0],
    'pf':[0]
})
for i in seasons:
    for j in teams:
        df = season_df.loc[(season_df.Season == i) & (season_df.Team == j), ['Season','Team','score','fgm','fga','fgm3','fga3','ftm','fta','or','dr','ast','to','stl','blk','pf']]
        temp_data = pd.DataFrame({'Season':[i],
                             'Team':[j],
                             'score':[df["score"].mean()],
                             'fgm':[df["fgm"].mean()],
                             'fga':[df["fga"].mean()],
                             'fgm3':[df["fgm3"].mean()],
                             'fga3':[df["fga3"].mean()],
                             'ftm':[df["ftm"].mean()],
                             'fta':[df["fta"].mean()],
                             'or':[df["or"].mean()],
                             'dr':[df["dr"].mean()],
                             'ast':[df["ast"].mean()],
                             'to':[df["to"].mean()],
                             'stl':[df["stl"].mean()],
                             'blk':[df["blk"].mean()],
                             'pf':[df["pf"].mean()]})
        avg_df = avg_df.append(temp_data)

avg_df = avg_df[1:]
avg_df.to_csv('season_avg.csv', index=False)
