#!/usr/bin/env python3
"""
Script principal para generar visualizaciones de datos NBA.

Este script ejecuta las visualizaciones del proyecto ETLFast desde el directorio raíz.
Las gráficas se guardan en app/Visualization/Charts/

Uso:
    python generate_visualizations.py

Gráficas generadas:
    • Evolución temporal de puntos por temporada
    • Barras apiladas de rendimiento de jugadores  
    • Box plot de distribución de puntos por décadas
"""

import sys
import os

# Añadir el directorio app al path para importar módulos
sys.path.append('app')

from Visualization.SMEVisualization import NBADataVisualizer

def main():
    """Función principal para generar todas las gráficas."""
    print("🏀 ETLFast - Generador de Visualizaciones NBA")
    print("=" * 55)
    
    try:
        # Crear instancia del visualizador
        visualizer = NBADataVisualizer()
        
        # Generar todas las visualizaciones
        visualizer.create_all_visualizations()
        
        print("\n" + "=" * 55)
        print("✅ ¡Todas las visualizaciones se generaron exitosamente!")
        print("📊 Ubicación de las gráficas: app/Visualization/Charts/")
        print("\n📈 Gráficas disponibles:")
        print("   • evolucion_temporal_puntos.png")
        print("   • barras_apiladas_rendimiento.png")
        print("   • boxplot_puntos_decadas.png")
        
    except Exception as e:
        print(f"❌ Error al generar visualizaciones: {e}")
        print("Asegúrate de que:")
        print("1. Los datos estén cargados en la base de datos")
        print("2. Las dependencias estén instaladas (seaborn, matplotlib)")
        return 1
    
    return 0

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)