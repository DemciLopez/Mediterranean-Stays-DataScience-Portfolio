# 📈 Week 04 – Tourism Trends Visualizer (Matplotlib & Seaborn)
# 🇪🇸 Visualizador de tendencias | 🇬🇧 Trends visualizer

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------------------------------------
# 1) Cargar datos de Week 03 / Load Week 03 data
# -----------------------------------------------------------
csv_path = "../Week_03_NumPy_Pandas/reservas_mediterranean.csv"
df = pd.read_csv(csv_path)

# KPIs calculados de nuevo por claridad / Recompute KPIs for clarity
df["ingreso_mensual"] = df["precio_noche"] * df["noches_ocupadas"]
df["ocupacion_pct"] = (df["noches_ocupadas"] / 30.0) * 100

os.makedirs("outputs", exist_ok=True)

# -----------------------------------------------------------
# 2) Línea: ocupación media por ciudad
#    Line: avg occupancy by city
# -----------------------------------------------------------
plt.figure()
(df.groupby("ciudad")["ocupacion_pct"].mean()
   .sort_values(ascending=False)
   .plot(kind="line", marker="o"))
plt.title("Avg Occupancy by City / Ocupación media por ciudad")
plt.ylabel("%")
plt.tight_layout()
plt.savefig("outputs/occupancy_by_city.png", dpi=150)

# -----------------------------------------------------------
# 3) Barras: ingreso medio por ciudad
#    Bars: avg revenue by city
# -----------------------------------------------------------
plt.figure()
(df.groupby("ciudad")["ingreso_mensual"].mean()
   .sort_values(ascending=False)
   .plot(kind="bar"))
plt.title("Avg Revenue by City / Ingreso medio por ciudad")
plt.ylabel("€")
plt.tight_layout()
plt.savefig("outputs/revenue_by_city.png", dpi=150)

# -----------------------------------------------------------
# 4) Dispersión: precio vs valoración
#    Scatter: price vs rating
# -----------------------------------------------------------
plt.figure()
sns.scatterplot(data=df, x="precio_noche", y="valoracion", hue="ciudad")
plt.title("Price vs Rating / Precio vs Valoración")
plt.tight_layout()
plt.savefig("outputs/price_vs_rating.png", dpi=150)

print("✅ Charts exported to Week_04_Visualization/outputs")
