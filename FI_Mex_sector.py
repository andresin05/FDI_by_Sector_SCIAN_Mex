# FDI Mex Sector SCIAN
# Parra Caporal José Andrés
# 14/03/23

# Pandas Modules
import os
import pandas as pd
import numpy as np
import bar_chart_race as bcr


# Directory
os.chdir("C:\\Users\\parra\\OneDrive\\Documents\\Python\\Data")

# Data
fdi_sector = pd.read_excel("flujosportipodeinversion.xlsx",
                           sheet_name = "Por sector",
                           header = None,
                           skiprows = 3,
                           nrows = 392,
                           usecols = "A,F,K,P,U,Z,AE,AJ,AO,AT,AY,BD,BI,BN,BS,BX,CC,CH,CM,CR,CW,DB,DG,DL,DQ")
    # Rename the columns
years = list(range(1999,2023))
years = [str(i) for i in years]
years.insert(0, "Sector, subsector, rama")

fdi_sector.columns = years
del years

# Select only the sectors
fdi_sector = fdi_sector[fdi_sector["Sector, subsector, rama"].isin(["11 Agricultura, cría y explotación de animales, aprovechamiento forestal, pesca y caza",
                                                                    "21 Minería",
                                                                    "22 Generación, transmisión y distribución de energía eléctrica, suministro de agua y de gas por ductos al consumidor final",
                                                                    "23 Construcción",
                                                                    "31-33 Industrias manufactureras",
                                                                    "43 y 46 Comercio",
                                                                    "48 y 49 Transportes, correos y almacenamiento",
                                                                    "51 Información en medios masivos",
                                                                    "52 Servicios financieros y de seguros",
                                                                    "53 Servicios inmobiliarios y de alquiler de bienes muebles e intangibles",
                                                                    "54 Servicios profesionales, científicos y técnicos",
                                                                    "56 Servicios de apoyo a los negocios y manejo de residuos y desechos, y servicios de remediación",
                                                                    "61 Servicios educativos",
                                                                    "62 Servicios de salud y de asistencia social",
                                                                    "71 Servicios de esparcimiento culturales y deportivos, y otros servicios recreativos",
                                                                    "72 Servicios de alojamiento temporal y de preparación de alimentos y bebidas",
                                                                    "81 Otros servicios excepto actividades gubernamentales",
                                                                    "93 Actividades legislativas, gubernamentales, de impartición de justicia y de organismos internacionales y extraterritoriales"])]

fdi_sector = fdi_sector.replace({"11 Agricultura, cría y explotación de animales, aprovechamiento forestal, pesca y caza":" Agricultura, animales, forestal (11)",
                                 "21 Minería":"Minería (21)",
                                 "22 Generación, transmisión y distribución de energía eléctrica, suministro de agua y de gas por ductos al consumidor final":"Energía eléctrica (22)",
                                 "23 Construcción":"Construcción (23)",
                                 "31-33 Industrias manufactureras":"Manufactura (31-33)",
                                 "43 y 46 Comercio":"Comercio (43 y 46)",
                                 "48 y 49 Transportes, correos y almacenamiento": "Transportes (48 y 49)",
                                 "51 Información en medios masivos":"Medios Masivos (51)",
                                 "52 Servicios financieros y de seguros":" S. Financieros (52)",
                                 "53 Servicios inmobiliarios y de alquiler de bienes muebles e intangibles":"Inmuebles (53)",
                                 "54 Servicios profesionales, científicos y técnicos":"S. profesionales (54)",
                                 "56 Servicios de apoyo a los negocios y manejo de residuos y desechos, y servicios de remediación":"S. Apoyo (56)",
                                 "61 Servicios educativos":"S. Educativos (61)",
                                 "62 Servicios de salud y de asistencia social":"S. Salud (62)",
                                 "71 Servicios de esparcimiento culturales y deportivos, y otros servicios recreativos":"S. Esparcimiento (71)",
                                 "72 Servicios de alojamiento temporal y de preparación de alimentos y bebidas":"S. Alojamiento (72)",
                                 "81 Otros servicios excepto actividades gubernamentales":"S. Otros (81)",
                                 "93 Actividades legislativas, gubernamentales, de impartición de justicia y de organismos internacionales y extraterritoriales":"Actividades Legislativas (93)"})

fdi_sector = fdi_sector.set_index("Sector, subsector, rama", drop = True)
fdi_sector = fdi_sector.replace('C', np.nan , regex=True)
fdi_sector.reset_index(inplace=True)

# Create a barchart race with the bar_chart race module
    # Each row is a year
    # Each column is a sector
fdi_sector_t = fdi_sector.copy()
fdi_sector_t = fdi_sector_t.set_index("Sector, subsector, rama", drop = True)
fdi_sector_t = fdi_sector_t.T

os.chdir("C:\\Users\\parra\\OneDrive\\Documents\\Python\\Figures\\Foering_inv_sector")

def summary(values, ranks):
    total_fi = int(round(values.sum(), -2))
    s = f'Total FDI - {total_fi:,.0f}' + "\nSource: Secretaría de Economía, México."
    return {'x': .99, 'y': .05, 's': s, 'ha': 'right', 'size': 8}

bcr.bar_chart_race(df = fdi_sector_t,
                   filename = "fi_mex_sector.gif",
                   orientation = "h",
                   sort = "desc",
                   n_bars = 10,
                   steps_per_period = 30,
                   perpendicular_bar_func= 'mean',
                   period_summary_func = summary,
                   cmap='dark12',
                   title = "Foreing Direct Investment by Sector SCIAN, Mexico (Millon USD)")













