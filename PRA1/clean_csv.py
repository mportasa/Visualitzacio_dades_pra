import pandas as pd


fitxer = "Accidents_de_tr_nsit_amb_morts_o_ferits_greus_a_Catalunya.csv"
df = pd.read_csv(fitxer)

#print(df.head())

columnes = ['nomCom', 'Any', 'F_MORTS']
df = df[columnes]
#print(df.head())
morts_any_comarca = df.groupby(['Any', 'nomCom']).sum().reset_index()
print (morts_any_comarca.head())


#aqui s'obte un llistat amb el nom de les comarques, que hi ha que modificar-les per tal de concordin amb el geojson
#comarques_llistat = df['nomCom'].drop_duplicates().reset_index(drop=True)

#he tingut problemes en llegir el segon fitxer
llistat_comarques = "comarques.csv"
try:
    llistat = pd.read_csv(llistat_comarques, encoding='utf-8')
except UnicodeDecodeError:
    try:
        llistat = pd.read_csv(llistat_comarques, encoding='ISO-8859-1')
    except UnicodeDecodeError:
        llistat = pd.read_csv(llistat_comarques, encoding='cp1252')
#print(llistat.head())

#arreglar el nom de les columnes
df_bona = pd.merge(morts_any_comarca, llistat, how='left', left_on='nomCom', right_on='mal')
#print(df_bona.head())
df_bona['nomCom'] = df_bona['be']
df_bona = df_bona.drop(columns=['be','mal'])
print(df_bona.head())
