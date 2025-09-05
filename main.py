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
#still finding what to do with rp, shape, sg, and esccape velocity






