def maximum_moon(df):
    max_moons = df['Number of Moons'].max()

    planets_name = df[df['Number of Moons'] == max_moons]['Planet Name'].tolist()
    planet_name = df[df['Number of Moons'] == max_moons]['Planet Name'].iloc[0]
    if len(planets_name) > 1:
         print(f"Planets with maximum number of moons are {planets_name} with {max_moons} moons")
    else:
        print(f"Planet with maximum number of moons is {planet_name} with {max_moons} moons")


