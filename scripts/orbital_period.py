def orbital_period(df):
    avg = df['Orbital Period (years)'].mean()


    mini = df['Orbital Period (years)'].min()
    mini_planets = df[df['Orbital Period (years)'] == mini]['Planet Name'].tolist()
    mini_planet = df[df['Orbital Period (years)'] == mini]['Planet Name'].iloc[0]


    maxi = df ['Orbital Period (years)'].max()
    max_planets = df[df['Orbital Period (years)'] == maxi]['Planet Name'].tolist()
    max_planet = df[df['Orbital Period (years)'] == maxi]['Planet Name'].iloc[0]

    print (f"The average orbital period of all the planets is: {avg} years")


    if len(mini_planets) > 1:
        print (f"The Planets with least Orbital period are {mini_planets} with period being:{mini} years")
    else:
        print(f"The Planet with Least Orbital period is {mini_planet} with period being: {mini} years")


    if len(max_planets) > 1:
        print(f"The Planets with most Orbital period are {max_planets} with period being: {maxi} years")
    else:
        print(f"The Planet with most Orbital period is { max_planet} with period being {maxi} years")



