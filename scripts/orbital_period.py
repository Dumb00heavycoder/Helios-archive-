def orbital_period(df):
    avg = df['Orbital Period (years)'].mean()
    mini = df['Orbital Period (years)'].min()
    maxi = df ['Orbital Period (years)'].max()
    print (avg, mini, maxi,) 

