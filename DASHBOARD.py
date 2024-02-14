import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Leer los datos de accidentes fatales y accidentes con lesiones
df_fatales = pd.read_csv('HECHOS_FATALES.csv')
df_lesiones = pd.read_csv('HECHOS_LESIONES.csv')

# Convertir la columna 'FECHA' a tipo datetime con múltiples formatos
df_fatales['FECHA'] = pd.to_datetime(df_fatales['FECHA'], errors='coerce')
df_lesiones['FECHA'] = pd.to_datetime(df_lesiones['FECHA'], errors='coerce')

# Definir las fechas de inicio y fin de los semestres
inicio_primer_semestre = pd.to_datetime('2021-01-01')  # Inicio del primer semestre (primer día de enero)
fin_primer_semestre = pd.to_datetime('2021-06-30')  # Fin del primer semestre (último día de junio)
inicio_segundo_semestre = pd.to_datetime('2021-07-01')  # Inicio del segundo semestre (primer día de julio)
fin_segundo_semestre = pd.to_datetime('2021-12-31')  # Fin del segundo semestre (último día de diciembre)

# Filtrar los registros por el período de los semestres
df_fatales_primer_semestre = df_fatales[(df_fatales['FECHA'] >= inicio_primer_semestre) & (df_fatales['FECHA'] <= fin_primer_semestre)]
df_lesiones_primer_semestre = df_lesiones[(df_lesiones['FECHA'] >= inicio_primer_semestre) & (df_lesiones['FECHA'] <= fin_primer_semestre)]
df_fatales_segundo_semestre = df_fatales[(df_fatales['FECHA'] >= inicio_segundo_semestre) & (df_fatales['FECHA'] <= fin_segundo_semestre)]
df_lesiones_segundo_semestre = df_lesiones[(df_lesiones['FECHA'] >= inicio_segundo_semestre) & (df_lesiones['FECHA'] <= fin_segundo_semestre)]

# Calcular el número total de accidentes fatales y con lesiones para cada semestre
total_accidentes_primer_semestre = len(df_fatales_primer_semestre) + len(df_lesiones_primer_semestre)
total_accidentes_segundo_semestre = len(df_fatales_segundo_semestre) + len(df_lesiones_segundo_semestre)

# Calcular la cantidad de hechos fatales para cada semestre
hechos_fatales_primer_semestre = len(df_fatales_primer_semestre)
hechos_fatales_segundo_semestre = len(df_fatales_segundo_semestre)

# Calcular la tasa de homicidios en siniestros viales para cada semestre
tasa_homicidios_primer_semestre = (hechos_fatales_primer_semestre / total_accidentes_primer_semestre) * 100 if total_accidentes_primer_semestre > 0 else 0
tasa_homicidios_segundo_semestre = (hechos_fatales_segundo_semestre / total_accidentes_segundo_semestre) * 100 if total_accidentes_segundo_semestre > 0 else 0

# Calcular la reducción de la tasa entre semestres
reduccion_tasa = abs(tasa_homicidios_segundo_semestre - tasa_homicidios_primer_semestre) / tasa_homicidios_primer_semestre * 100

# Inicializar la aplicación Dash
app = dash.Dash(__name__)

# Layout del dashboard
app.layout = html.Div([
    html.H1("Dashboard de Accidentes Viales"),
    html.Div([
        dcc.Dropdown(
            id='year-dropdown',
            options=[
                {'label': '2020', 'value': '2020'},
                {'label': '2021', 'value': '2021'}
            ],
            value='2020'
        )
    ]),
    html.Div(id='accidentes-graph'),
    dcc.Graph(id='motociclistas-graph')
])

# Callback para actualizar el gráfico de motociclistas según el año seleccionado
@app.callback(
    Output('motociclistas-graph', 'figure'),
    [Input('year-dropdown', 'value')]
)
def update_motociclistas_graph(year):
    if year == '2020':
        df_year = df_fatales[df_fatales['AAAA'] == 2020]
    else:
        df_year = df_fatales[df_fatales['AAAA'] == 2021]

    # Filtrar para considerar solo accidentes fatales con víctima en moto
    df_motociclistas = df_year[df_year['VICTIMA'] == 'MOTO']

    # Calcular la cantidad de accidentes fatales con víctima en moto
    hechos_fatales_motociclistas = len(df_motociclistas)

    # Crear el gráfico de barras
    fig = go.Figure(data=[go.Bar(x=['Accidentes Fatales'], y=[hechos_fatales_motociclistas])])
    fig.update_layout(
        title=f'Accidentes Fatales con Motociclistas en el Año {year}',
        xaxis_title='Tipo de Accidente',
        yaxis_title='Cantidad de Accidentes Fatales',
        height=500,
        width=700
    )
    return fig

# Callback para mostrar la leyenda de reducción de tasa
@app.callback(
    Output('accidentes-graph', 'children'),
    [Input('year-dropdown', 'value')]
)
def update_accidentes_graph(year):
    if year == '2020':
        labels = ['Total Accidentes', 'Accidentes Fatales']
        values = [total_accidentes_primer_semestre, hechos_fatales_primer_semestre]
    else:
        labels = ['Total Accidentes', 'Accidentes Fatales']
        values = [total_accidentes_segundo_semestre, hechos_fatales_segundo_semestre]
    
    fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    fig.update_layout(
        title=f'Distribución de Accidentes Totales vs Fatales en el Año {year}',
        margin=dict(l=20, r=20, t=30, b=20),
        height=500,
        width=700
    )
    return dcc.Graph(figure=fig)

# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True, port=8052)
