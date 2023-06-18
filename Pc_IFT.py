import numpy as np
#Calculate log10 of PCIFT (Pc normalized by measured condition)
def PC_IFT(df,PC,conversion, min, decimal):
    with np.errstate(divide='ignore', invalid='ignore'):
        result2 = np.where(df_clean[PC] > 0, round(np.log10(df_clean[PC]/conversion),decimal), min)
    df_clean['PC_IFT'] = result2
    return df_clean
