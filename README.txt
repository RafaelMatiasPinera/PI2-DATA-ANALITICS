# PROYECTO INDIVIDUAL 2 DATA ANALISIS

alumno: Rafael Piñera

Contexto: 
En Argentina, cada año mueren cerca de 4.000 personas en siniestros viales.   
Aunque muchas jurisdicciones han logrado disminuir la cantidad de accidentes de tránsito,   
esta sigue siendo la principal causa de muertes violentas en el país.     

Objeto:
La Secretaría de Transporte del Gobierno de la Ciudad Autónoma de Buenos Aires  
del Observatorio de Movilidad y Seguridad Vial (OMSV) requiere un análisis para generar información y 
evaluar medidas con el fin de disminuir la cantidad de víctimas fatales en siniestros viales.

Recursos:   
#dataset - homicidios - siniestros viales - en CABA ((2016-2021)).  
"""dataset - formato xlsx - dos hojas llamadas: hechos y víctimas"""  
#dos hojas de diccionarios de guía.

Nota:
Los pasos seguidos en este trabajo se exponen cronológicamente en el JupiterNotebook denominado "PI2.ipynb".
A su vez en el mencionado archivo se observan gráficos, como también mapas interactivos.
Respecto de los KPIS, se pueden visualizar en DASHBOARD.PY (Dashboard generado con la librería DE PYTHON Dash).
Dadas las limítaciones de la librería, se optó a su vez por presentar un DashBoard en Google Sheets.
(Se optó por usar estas tecnologías, antes que Tableau, o Power BI, debido a que utilizo el sistema operativo UBUNTU linux y no encontré forma de correr dichos programas)

Pasos:
PRIMERO:
Se procede al modelado de los datos. Se eliminan columnas innecesarias, se fucionan las tablas correspondientes.
Esto derivó en que se consiguiera tener dos archivos formato csv:
(HECHOS_FATALES) Y (HECHOS_LESIONES)

SEGUNDO:
Se procede a analizar gráficamente los datos. Y se deja asentado los patrones y analisis que se observaron en los datos.

TERCERO:
Se definieron los KPIS, se analizó si se cumplieron las expectativas correspondientes en los últimos períodos de tiempo registrados.
Asimismo se crearon los Dashboards (.py) y Google Sheets.

CUARTO:
En base a la información recolectada, sobre todo teniendo en cuenta los gráficos y analisis de la segunda seccion se definieron políticas publicas /medidas aplicables para disminuir las víctimas fatales en CABA.

