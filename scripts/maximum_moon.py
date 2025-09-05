def maximum_moon(df):
    max_moons = df['Number of Moons'].max()

    planet_name = df[df['Number of Moons'] == max_moons]['Planet Name'].tolist()
    if len(planet_name) > 1:
         print('Planets with maximum number of moons are', planet_name, 'with', max_moons, 'moons')
    else:
        print('Planet with maximum number of moons is', planet_name, 'with', max_moons, 'moons')


