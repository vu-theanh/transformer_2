import numpy as np

#Calculate normalized water saturation
def Swn(df,Sw,Swir,Swn): #dataframe name, sw, swir, swn column names
    df_clean = df.copy()
    with np.errstate(divide='ignore', invalid='ignore'):
        result = (df_clean[Sw]  - df_clean[Swir] ) / (1 - df_clean[Swir] )
        result = np.where(result> 0, round(np.log10(result),5), 0.00001)

    df_clean[Swn] = result
    return df_clean
