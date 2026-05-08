import pandas as pd
import json

df = pd.read_csv("union.csv")

# convertir a formato diccionario por speciesCode
resultado = {}

for _, row in df.iterrows():
    if pd.notna(row["speciesCode"]):
        resultado[row["speciesCode"]] = {
            "es": row["Nombre_CL"],
            "en": row["comName_en"],
            "sci": row["sciName"]
        }

with open("species.json", "w", encoding="utf-8") as f:
    json.dump(resultado, f, ensure_ascii=False, indent=2)
