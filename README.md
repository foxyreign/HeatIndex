# Heat Index Calculator

This is a simple interactive **web application** built with **Streamlit** that calculates the **Heat Index** (also known as the "feels like" temperature) based on user-input **temperature in Celsius** and **relative humidity**.

The app also visualizes the relationship between heat index, temperature, and humidity using an interactive line chart.

---

## What is the Heat Index?

The **Heat Index (HI)** is an estimate of how hot it feels to the human body when humidity is factored in with the actual air temperature. It reflects the combined effects of **air temperature** and **relative humidity** on human discomfort and heat stress.

> When the humidity is high, sweat evaporates more slowly, making it feel hotter than the actual air temperature.

---

## Formula (U.S. National Weather Service)

The formula is originally defined in Fahrenheit:

\[
\text{HI} = -42.379 + 2.04901523T + 10.14333127R - 0.22475541TR - 0.00683783T^2 - 0.05481717R^2 + 0.00122874T^2R + 0.00085282TR^2 - 0.00000199T^2R^2
\]

Where:
- \( T \) = Air temperature in **°F**
- \( R \) = Relative Humidity in **%**

This app converts Celsius input to Fahrenheit for the formula and converts the result back to **°C**.

> The formula is most accurate when:
> - Temperature ≥ 26.7°C (80°F)  
> - Humidity ≥ 40%

---

## Features

- User input for temperature (°C) and humidity (%)
- Line chart showing how heat index changes with humidity
- Validates input range to avoid extrapolation
- Simple, responsive Streamlit interface

---

## Requirements

- Python 3.7+
- `streamlit`
- `matplotlib`
- `numpy`

Install dependencies with:

```bash
pip install streamlit matplotlib numpy
