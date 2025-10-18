"""
🏠 Calculadora de Rentabilidad - Mediterranean Stays
Author: Demci López
Mentorship: ChatGPT Personal Tutorship
Week 01 – Python Fundamentals
"""

# 🇪🇸 Solicitar datos al usuario / 🇬🇧 Ask for user input
ingresos = float(input("Introduce los ingresos mensuales (€): "))
gastos = float(input("Introduce los gastos mensuales (€): "))

# 🇪🇸 Calcular beneficio y rentabilidad / 🇬🇧 Calculate profit and ROI
beneficio = ingresos - gastos
rentabilidad = (beneficio / ingresos) * 100

print("\n📊 Resultado:")
print(f"Beneficio: {beneficio:.2f} €")
print(f"Rentabilidad: {rentabilidad:.2f}%")
