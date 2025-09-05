import pandas as pd

df = pd.read_csv('Solarsystem_planet_data.csv')

from maximum_moon import maximum_moon
from average_distance_from_star import average_distance
from orbital_period import orbital_period

#will give planet with max moon
maximum_moon(df)

#will give average distance from sum of all planetis
average_distance(df)

#will give average, min and max orbital period
orbital_period(df)

#still finding what to do with rp, shape, sg, and esccape velocity






