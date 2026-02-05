# 📊 Módulo de Visualizaciones NBA - ETLFast

Este módulo genera visualizaciones profesionales de los datos de NBA limpios usando **seaborn** y **matplotlib**.

## 🎯 Visualizaciones Generadas

### 1. **Evolución Temporal de Puntos por Temporada**
- **Archivo**: `evolucion_temporal_puntos.png`
- **Descripción**: Gráfica de línea que muestra la evolución de los puntos promedio por jugador a lo largo de las temporadas NBA
- **Incluye**: Línea de tendencia para visualizar la evolución general

### 2. **Barras Apiladas de Rendimiento por Temporada**
- **Archivo**: `barras_apiladas_rendimiento.png`
- **Descripción**: Gráfica de barras apiladas que muestra la distribución porcentual de jugadores según su rendimiento
- **Categorías**: 
  - Alto Rendimiento (net_rating > 5 y pts > 10)
  - Rendimiento Medio (net_rating > 0 o pts > 8)
  - Bajo Rendimiento (otros casos)

### 3. **Box Plot de Distribución de Puntos por Décadas**
- **Archivo**: `boxplot_puntos_decadas.png`
- **Descripción**: Box plot que muestra la distribución de puntos por jugador agrupados por décadas
- **Incluye**: Medianas marcadas para cada década

## 🚀 Uso

### Opción 1: Script Principal (Recomendado)
```bash
# Desde el directorio raíz del proyecto
python generate_visualizations.py
```

### Opción 2: Módulo Directo
```bash
# Ejecutar el módulo de visualización
python app/Visualization/SMEVisualization.py
```

### Opción 3: Programáticamente
```python
from app.Visualization.SMEVisualization import NBADataVisualizer

# Crear visualizador
viz = NBADataVisualizer()

# Generar todas las gráficas
viz.create_all_visualizations()

# O generar gráficas individuales
viz.create_temporal_points_evolution()
viz.create_stacked_wins_losses_chart()
viz.create_points_distribution_boxplot()
```

## 📁 Estructura de Archivos

```
app/Visualization/
├── __init__.py
├── SMEVisualization.py      # Clase principal de visualización
├── generate_charts.py       # Script auxiliar
└── Charts/                  # 📊 Gráficas generadas
    ├── evolucion_temporal_puntos.png
    ├── barras_apiladas_rendimiento.png
    └── boxplot_puntos_decadas.png
```

## 🔧 Dependencias

- **pandas**: Manipulación de datos
- **numpy**: Operaciones numéricas
- **seaborn**: Visualizaciones estadísticas
- **matplotlib**: Gráficas base
- **sqlite3**: Conexión a base de datos

## 📋 Requisitos

1. **Datos cargados**: La base de datos `app/Extract/Files/etl_data.db` debe contener la tabla `all_seasons_clean`
2. **Entorno Python**: Entorno virtual configurado con las dependencias instaladas
3. **Permisos**: Permisos de escritura en la carpeta `Charts`

## ⚙️ Configuración

La clase `NBADataVisualizer` acepta parámetros de configuración:

```python
visualizer = NBADataVisualizer(
    db_path='ruta/a/base_datos.db',    # Ruta a la base de datos
    charts_dir='ruta/a/graficas'       # Directorio de salida
)
```

## 🎨 Personalización

### Cambiar Estilo de Gráficas
```python
# En SMEVisualization.py, línea ~32
sns.set_style("whitegrid")  # Opciones: whitegrid, darkgrid, white, dark, ticks
```

### Modificar Colores
```python
# Para barras apiladas (línea ~130)
color=['#d62728', '#ff7f0e', '#2ca02c']  # Rojo, Naranja, Verde

# Para box plot (línea ~175)
palette='Set2'  # Opciones: Set1, Set2, Set3, viridis, etc.
```

## 📈 Interpretación de Gráficas

### Evolución Temporal
- **Tendencia ascendente**: Aumento en el promedio de puntos por temporada
- **Puntos atípicos**: Temporadas con cambios significativos (lockouts, reglas)

### Barras Apiladas
- **Verde (Alto)**: Jugadores con excelente rendimiento
- **Naranja (Medio)**: Jugadores con rendimiento promedio
- **Rojo (Bajo)**: Jugadores con bajo rendimiento

### Box Plot por Décadas
- **Caja**: Rango intercuartílico (Q1 a Q3)
- **Línea central**: Mediana
- **Bigotes**: Valores mín/máx dentro de 1.5 * IQR
- **Puntos**: Valores atípicos

## 🐛 Solución de Problemas

### Error: "unable to open database file"
```bash
# Verificar que la base de datos existe
ls -la app/Extract/Files/etl_data.db

# Ejecutar desde el directorio correcto
cd /path/to/ETLFast
python generate_visualizations.py
```

### Error: "No module named 'seaborn'"
```bash
# Activar entorno virtual e instalar dependencias
pip install seaborn matplotlib pandas
```

### Gráficas no se guardan
```bash
# Verificar permisos de escritura
chmod 755 app/Visualization/Charts/
```

## 📊 Salida Esperada

Al ejecutar exitosamente, verás:
```
🏀 ETLFast - Generador de Visualizaciones NBA
=======================================================
Datos cargados exitosamente: 12844 registros

1. Creando gráfica de evolución temporal de puntos...
Gráfica guardada en: app/Visualization/Charts/evolucion_temporal_puntos.png

2. Creando gráfica de barras apiladas de rendimiento...
Gráfica guardada en: app/Visualization/Charts/barras_apiladas_rendimiento.png

3. Creando box plot de distribución de puntos por décadas...
Gráfica guardada en: app/Visualization/Charts/boxplot_puntos_decadas.png

✅ ¡Todas las visualizaciones se generaron exitosamente!
```