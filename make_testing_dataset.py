import pandas as pd
import numpy as np
import itertools as iter

def seed_str_to_num(seed):
    return int(float(''.join(i for i in seed if i.isdigit())))

print '\n'
print 'making test dataset'

avg_df = pd.read_csv('season_avg.csv')
seeds_df = pd.read_csv('input/TourneySeeds.csv')

avg_df = avg_df.loc[(avg_df.Season == 2016), ['Season','Team','score','fgm','fga','fgm3','fga3','ftm','fta','or','dr','ast','to','stl','blk','pf']]
seeds_df = seeds_df.loc[(seeds_df.Season == 2016), ['Season','Team','Seed']]
test_df = pd.DataFrame([[0,1]], columns=['LowTeam','HighTeam'])
year_df = seeds_df.loc[(seeds_df.Season == 2016), ['Team']]

#get all possible combinations of teams since we don't know apriori which teams will play each other
df =[year_df.transpose()[list(pair)] for pair in list(iter.combinations(year_df.transpose().columns, 2))]
for j in df:
    j['Season'] = 2016
    j.columns = ['LowTeam', 'HighTeam','Season']
    test_df = test_df.append(j)

test_df = test_df[1:]
test_df = test_df[['Season', 'LowTeam', 'HighTeam']]

out_df = pd.DataFrame({
    'Season':[0],
    'LowTeam':[0],
    'HighTeam':[0],
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

#for each possible game in the tournament, add row to dataframe with differences in season avg stats
for index, row in test_df.iterrows():

    low_team = row['LowTeam']
    high_team = row['HighTeam']
    rs = row['Season'] 
    
    if row['LowTeam'] < row['HighTeam']:
        low_team = row['LowTeam']
        high_team = row['HighTeam']
    else:
        low_team = row['HighTeam']
        high_team = row['LowTeam']

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

    out_df = out_df.append(temp_df)

out_df = out_df[1:]
#print out_df.head(5)

out_df.to_csv('test.csv')
