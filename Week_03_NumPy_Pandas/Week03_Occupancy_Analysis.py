# 📊 Week 03 – NumPy & Pandas: Occupancy & Revenue Analysis
# 🇪🇸 Análisis de ocupación e ingresos | 🇬🇧 Occupancy & revenue analysis

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# 1) Cargar datos / Load data
# Si no existe el CSV, generamos uno pequeño de ejemplo
# If CSV doesn't exist, we create a tiny sample dataset
# -----------------------------------------------------------
import os
csv_path = "reservas_mediterranean.csv"

if not os.path.exists(csv_path):
    df = pd.DataFrame({
        "nombre": ["Villa Olivos","Apto Sol","Casa Marina","Apto Centro","Loft Blue","Casa Mar"],
        "ciudad": ["Alicante","Alicante","Calpe","Benidorm","Denia","Alicante"],
        "precio_noche": [120,95,150,110,85,130],
        "noches_ocupadas": [18,21,12,20,16,22],
        "valoracion": [4.8,4.6,4.3,4.5,4.1,4.9],
        "mes": ["Ene","Ene","Ene","Ene","Ene","Ene"]
    })
    df.to_csv(csv_path, index=False)
else:
    df = pd.read_csv(csv_path)

# -----------------------------------------------------------
# 2) Métricas básicas / Basic metrics
# -----------------------------------------------------------
df["ingreso_mensual"] = df["precio_noche"] * df["noches_ocupadas"]
df["ocupacion_pct"] = (df["noches_ocupadas"] / 30.0) * 100

print("🇪🇸 Ingreso medio por ciudad / 🇬🇧 Avg monthly revenue by city")
print(df.groupby("ciudad")["ingreso_mensual"].mean().round(2), "\n")

top_prop = df.loc[df["ingreso_mensual"].idxmax(), ["nombre","ingreso_mensual"]]
print(f"🏆 Top propiedad / Top property: {top_prop['nombre']} -> {top_prop['ingreso_mensual']:.2f} €")

# -----------------------------------------------------------
# 3) Visual rápido / Quick viz
# -----------------------------------------------------------
# Ingreso medio por ciudad (barras) / Avg revenue by city (bar)
avg_rev = df.groupby("ciudad")["ingreso_mensual"].mean().sort_values(ascending=False)
plt.figure()
avg_rev.plot(kind="bar")
plt.title("Avg revenue by city / Ingreso medio por ciudad")
plt.ylabel("€")
plt.tight_layout()
os.makedirs("outputs", exist_ok=True)
plt.savefig("outputs/revenue_by_city.png", dpi=150)

# Ocupación por propiedad (línea) / Occupancy per property (line)
plt.figure()
plt.plot(df["nombre"], df["ocupacion_pct"], marker="o")
plt.title("Occupancy (%) by property / Ocupación (%) por propiedad")
plt.xticks(rotation=25)
plt.ylabel("%")
plt.tight_layout()
plt.savefig("outputs/occupancy_by_property.png", dpi=150)

print("✅ Saved charts in /outputs")
