import pandas as pd

df = pd.read_csv('Solarsystem_planet_data.csv')

from scripts.maximum_moon import maximum_moon
from scripts.average_distance_from_star import average_distance
from scripts.orbital_period import orbital_period

#will give planet with max moon
maximum_moon(df)
print('\n')
#will give average distance from sum of all planetis
average_distance(df)
print('\n')
#will give average, min and max orbital period
orbital_period(df)
print('\n')
#will give heaviest and lighest planet with which is hardest to escape and easiest to escape

#will give travel time for sunlight, which takes max which takes least and what is average

#shape comparison. which is most perfect and which is least perfect  

#communication delay by computing light travel time using distance and speed of light. 

#calculate orbital speed of all planets

#



