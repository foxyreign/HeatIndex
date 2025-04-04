import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Conversion Functions
# -------------------------------
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

# -------------------------------
# Heat Index Formula (Fahrenheit)
# -------------------------------
def heat_index_fahrenheit(T, R):
    return (
        -42.379 + 2.04901523 * T + 10.14333127 * R
        - 0.22475541 * T * R - 6.83783e-3 * T**2
        - 5.481717e-2 * R**2 + 1.22874e-3 * T**2 * R
        + 8.5282e-4 * T * R**2 - 1.99e-6 * T**2 * R**2
    )

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("🌡️ Heat Index Calculator (Feels Like Temperature)")
st.markdown("Enter the **temperature in °C** and **relative humidity in %** below.")

temp_c = st.number_input("Temperature (°C)", min_value=0.0, max_value=60.0, value=32.0)
rh = st.number_input("Relative Humidity (%)", min_value=0.0, max_value=100.0, value=70.0)

if temp_c < 26.7 or rh < 40:
    st.warning("⚠️ Formula is only accurate for T ≥ 26.7°C and RH ≥ 40%.")
else:
    temp_f = c_to_f(temp_c)
    hi_f = heat_index_fahrenheit(temp_f, rh)
    hi_c = f_to_c(hi_f)
    st.success(f"**Heat Index (Feels Like): {hi_c:.1f}°C**")

# -------------------------------
# Plotting Heat Index vs Temperature
# -------------------------------
st.markdown("### 📈 Heat Index Curve by Humidity")

temps_c = np.arange(25, 45, 1)
humidity_levels = [40, 50, 60, 70, 80, 90]

fig, ax = plt.subplots(figsize=(8, 6))
for rh_plot in humidity_levels:
    temps_f = c_to_f(temps_c)
    hi_f = heat_index_fahrenheit(temps_f, rh_plot)
    hi_c = f_to_c(hi_f)
    ax.plot(temps_c, hi_c, label=f"{rh_plot}% RH")

ax.set_title("Heat Index vs Temperature")
ax.set_xlabel("Temperature (°C)")
ax.set_ylabel("Heat Index (°C)")
ax.legend(title="Relative Humidity")
ax.grid(True)
st.pyplot(fig)
