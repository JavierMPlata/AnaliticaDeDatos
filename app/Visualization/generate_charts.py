"""
Script para generar visualizaciones de datos NBA limpios.

Este script ejecuta las visualizaciones principales del proyecto ETLFast:
1. Evolución temporal de puntos por temporada
2. Barras apiladas de rendimiento de jugadores
3. Box plot de distribución de puntos por décadas

Las gráficas se guardan automáticamente en app/Visualization/Charts/
"""

from SMEVisualization import NBADataVisualizer

def generate_charts():
    """Función principal para generar todas las gráficas."""
    print("🏀 Generador de Visualizaciones NBA - ETLFast")
    print("=" * 50)
    
    # Crear instancia del visualizador
    visualizer = NBADataVisualizer()
    
    # Generar todas las visualizaciones
    visualizer.create_all_visualizations()
    
    print("\n✅ Proceso completado exitosamente!")
    print("📊 Puedes encontrar las gráficas en: app/Visualization/Charts/")
    print("\nGráficas generadas:")
    print("• evolucion_temporal_puntos.png - Evolución de puntos promedio por temporada")
    print("• barras_apiladas_rendimiento.png - Distribución de rendimiento por temporada")
    print("• boxplot_puntos_decadas.png - Distribución de puntos por décadas")

if __name__ == "__main__":
    generate_charts()