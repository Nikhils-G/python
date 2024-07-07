import pandas as pd

#create DataFrame
df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'points': [18, 22, 29, 25, 14, 11, 10, 15]})

#create boxplot of points, grouped by team
df.boxplot(column=['points'], by='team', grid=False, color='black')
