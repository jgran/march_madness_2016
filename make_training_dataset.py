import pandas as pd
import numpy as np

season_df = pd.read_csv('input/RegularSeasonDetailedResults.csv')
tourney_df = pd.read_csv('input/TourneyCompactResults.csv')
teams_df = pd.read_csv('input/Teams.csv')
seeds_df = pd.read_csv('input/TourneySeeds.csv')
avg_df = pd.read_csv('season_avg.csv')

def seed_str_to_num(seed):
    return int(float(''.join(i for i in seed if i.isdigit())))


print '\n'
print 'making training dataset'

#training dataset from available years prior to 2016 tournament
tourney_df = tourney_df.loc[(tourney_df.Season >= 2003) & (tourney_df.Season <= 2015), ['Season','Wteam','Lteam']]

train_df = pd.DataFrame({
    'Season':[0],
    'LowTeam':[0],
    'HighTeam':[0],
    'LowWin':[0],
    'diff_seed':[0],
    'diff_score':[0],
    'diff_fgm':[0],
    'diff_fga':[0],
    'diff_fgm3':[0],
    'diff_fga3':[0],
    'diff_ftm':[0],
    'diff_fta':[0],
    'diff_or':[0],
    'diff_dr':[0],
    'diff_ast':[0],
    'diff_to':[0],
    'diff_stl':[0],
    'diff_blk':[0],
    'diff_pf':[0]
})


for index, row in tourney_df.iterrows():

    #figure out if the team with the lowest team ID won the game
    #this makes the notion of win or lose unambiguous
    low_team = 0
    high_team = 0
    low_win = 0
    if row['Wteam'] < row['Lteam']:
        low_team = row['Wteam']
        high_team = row['Lteam']
        low_win = 1
    else:
        low_team = row['Lteam']
        high_team = row['Wteam']
        low_win = 0

    #year this game took place
    rs = row['Season'] 

    #now calculate differences in season avg stats and store in dataframe
    try:
      s1 = seed_str_to_num(seeds_df[(seeds_df.Season == rs) & (seeds_df.Team == low_team)].iloc[0].Seed)
      s2 = seed_str_to_num(seeds_df[(seeds_df.Season == rs) & (seeds_df.Team == high_team)].iloc[0].Seed)
      diff_seed = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].score
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].score
      diff_score = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].fgm
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].fgm
      diff_fgm = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].fga
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].fga
      diff_fga = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].fgm3
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].fgm3
      diff_fgm3 = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].fga3
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].fga3
      diff_fga3 = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].ftm
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].ftm
      diff_ftm = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].fta
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].fta
      diff_fta = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0]['or']
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0]['or']
      diff_or = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].dr
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].dr
      diff_dr = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].ast
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].ast
      diff_ast = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].to
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].to
      diff_to = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].stl
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].stl
      diff_stl = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].blk
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].blk
      diff_blk = s1 - s2

      s1 = avg_df[(avg_df.Season == rs) & (avg_df.Team == low_team)].iloc[0].pf
      s2 = avg_df[(avg_df.Season == rs) & (avg_df.Team == high_team)].iloc[0].pf
      diff_pf = s1 - s2

      temp_df = pd.DataFrame({
          'Season':row['Season'],
          'LowTeam':[low_team],
          'HighTeam':[high_team],
          'LowWin':[low_win],
          'diff_seed':[diff_seed],
          'diff_score':[diff_score],
          'diff_fgm':[diff_fgm],
          'diff_fga':[diff_fga],
          'diff_fgm3':[diff_fgm3],
          'diff_fga3':[diff_fga3],
          'diff_ftm':[diff_ftm],
          'diff_fta':[diff_fta],
          'diff_or':[diff_or],
          'diff_dr':[diff_dr],
          'diff_ast':[diff_ast],
          'diff_to':[diff_to],
          'diff_stl':[diff_stl],
          'diff_blk':[diff_blk],
          'diff_pf':[diff_pf]
      })

      train_df = train_df.append(temp_df)
    except: 
      print 'found an exception'
      continue


train_df = train_df[1:]
#print train_df.head(5)

train_df.to_csv('train.csv', index=False)
