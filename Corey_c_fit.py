# Calculate the intercept and slope for each unique combination of sample name and location
import numpy as np
import pandas as pd
def Corey_v_fit(df,groupby, Sw, PC): #groupby column list ["column1","column2"], df is pandas data frame
    df_clean = df.copy()
    df_clean['Intercept'] = np.nan
    df_clean['Slope'] = np.nan

    for _, group in df_clean.groupby(groupby):
        if len(group) > 1:
            x = group[Sw].astype(float)
            y = group[PC].astype(float)
            slope, intercept = np.polyfit(x, y, 1)  # Fit a linear regression line
            df_clean.loc[group.index, 'Intercept'] = round(intercept,5)
            df_clean.loc[group.index, 'Slope'] = round(slope,5)

    # Sort the dataframe by 'Sample' and 'Location' for QC
    df_clean = df_clean.sort_values(by= groupby)

    # Reset the index of the sorted dataframe
    df_clean = df_clean.reset_index(drop=True)
    return df_clean
