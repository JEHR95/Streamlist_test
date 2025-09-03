#importación de librerías
import streamlit as st
import scipy.stats
import time

# Agrega un encabezado a la página
st.header('Lanzar una moneda')

chart = st.line_chart([0.5])

#función que emula el lanzamiento de una moneda 
def toss_coin(n):

    trial_outcomes = scipy.stats.bernoulli.rvs(p=0.5, size=n)

    mean = None
    outcome_no = 0
    outcome_1_count = 0

    for r in trial_outcomes:
        outcome_no +=1
        if r == 1:
            outcome_1_count +=1
        mean = outcome_1_count / outcome_no
        chart.add_rows([mean])
        time.sleep(0.05)

    return mean

# Genera un slider para determinar el número de lanzamientos de la moneda
number_of_trials = st.slider('¿Número de intentos?', 1, 1000, 10)
# Crea un botón de ejecución
start_button = st.button('Ejecutar')

if start_button:
    st.write(f'Experimento con {number_of_trials} intentos en curso.')

st.write ('Esta aplicación aún no es funcional. En construcción.')