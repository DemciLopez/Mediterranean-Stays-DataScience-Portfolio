"""
🎛️ Simulador de Reservas / Booking Simulator
Author: Demci López | Mentorship: ChatGPT
Week 02 – Data Structures & Functions
"""

# 🇪🇸 Objetivo: calcular ingreso y beneficio de varias viviendas con funciones y estructuras de datos
# 🇬🇧 Objective: compute income and profit for several properties using functions and data structures

viviendas = [
    {"nombre": "Villa Los Olivos", "precio_noche": 120, "noches": 18, "gastos": 420},
    {"nombre": "Apartamento Sol", "precio_noche": 95, "noches": 21, "gastos": 380},
    {"nombre": "Casa Marina", "precio_noche": 150, "noches": 12, "gastos": 450},
]

def ingreso(precio, noches):
    return precio * noches

def beneficio(precio, noches, gastos=400):
    return ingreso(precio, noches) - gastos

# 🇪🇸 Calcular KPIs / 🇬🇧 Compute KPIs
for v in viviendas:
    v["ingreso"] = ingreso(v["precio_noche"], v["noches"])
    v["beneficio"] = beneficio(v["precio_noche"], v["noches"], v["gastos"])

# 🇪🇸 Ordenar por beneficio descendente / 🇬🇧 Sort by profit (descending)
ordenadas = sorted(viviendas, key=lambda x: x["beneficio"], reverse=True)

print("\n📊 Ranking por beneficio / Profit ranking")
for v in ordenadas:
    print(f"- {v['nombre']}: ingreso {v['ingreso']} €, beneficio {v['beneficio']} €")
