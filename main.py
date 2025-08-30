import pandas as pd

df = pd.read_csv('Solarsystem_planet_data.csv')

from maximum_moon import maximum_moon

print('Welcome to the Helios Archive! This is an educational passion project I’ve created as a fun way to pass the time. I’ve included a solar system dataset with this project, but feel free to use your own data as well.') 

#will give planet with max moon
maximum_moon(df)

#will give average distance from sum of all planets

'''will give distance between earth and other planets with the help of average distance from sun '''

#will give average, min and max orbital period

#still finding what to do with rp, shape, sg, and esccape velocity






