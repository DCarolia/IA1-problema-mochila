import time
import itertools

# -------------------------------------------------------------
# 0. Datos del Problema
# -------------------------------------------------------------
# Cada objeto se define como: (id, peso, valor)
objetos = [
    {"id": 1, "peso": 2, "valor": 10},
    {"id": 2, "peso": 3, "valor": 15},
    {"id": 3, "peso": 5, "valor": 25},
    {"id": 4, "peso": 7, "valor": 30},
    {"id": 5, "peso": 1, "valor": 5},
    {"id": 6, "peso": 4, "valor": 20},
    {"id": 7, "peso": 6, "valor": 18}
]
W = 15  # Capacidad máxima de la mochila

# -------------------------------------------------------------
# 1. Implementación: Búsqueda Exhaustiva (Fuerza Bruta)
# -------------------------------------------------------------
def busqueda_exhaustiva(items, max_w):
    inicio = time.perf_counter()
    mejor_valor = -1
    mejor_combinacion = []
    mejor_peso = 0
    n = len(items)
    
    # Generar todas las combinaciones posibles (2^n)
    for r in range(n + 1):
        for comb in itertools.combinations(items, r):
            peso_total = sum(item["peso"] for item in comb)
            valor_total = sum(item["valor"] for item in comb)
            
            # Evaluar si es válida y si mejora la mejor solución
            if peso_total <= max_w and valor_total > mejor_valor:
                mejor_valor = valor_total
                mejor_combinacion = comb
                mejor_peso = peso_total
                
    fin = time.perf_counter()
    ids_seleccionados = [item["id"] for item in mejor_combinacion]
    return mejor_valor, mejor_peso, ids_seleccionados, fin - inicio

# -------------------------------------------------------------
# 2. Implementación: Búsqueda Greedy (Algoritmo Voraz)
# -------------------------------------------------------------
def busqueda_greedy(items, max_w, criterio):
    inicio = time.perf_counter()
    
    # Ordenar según el criterio elegido
    if criterio == "valor":
        items_ordenados = sorted(items, key=lambda x: x["valor"], reverse=True)
    elif criterio == "peso":
        items_ordenados = sorted(items, key=lambda x: x["peso"])
    elif criterio == "densidad":
        items_ordenados = sorted(items, key=lambda x: x["valor"] / x["peso"], reverse=True)
    
    peso_actual = 0
    valor_total = 0
    ids_seleccionados = []
    
    # Agregar objetos mientras quepan
    for item in items_ordenados:
        if peso_actual + item["peso"] <= max_w:
            ids_seleccionados.append(item["id"])
            peso_actual += item["peso"]
            valor_total += item["valor"]
            
    fin = time.perf_counter()
    return valor_total, peso_actual, ids_seleccionados, fin - inicio

# -------------------------------------------------------------
# 3. Ejecución y Comparación de Resultados
# -------------------------------------------------------------
resultados = {}

# Ejecutar Fuerza Bruta
resultados["Exhaustiva"] = busqueda_exhaustiva(objetos, W)

# Ejecutar variantes Greedy
resultados["Greedy por Valor"] = busqueda_greedy(objetos, W, "valor")
resultados["Greedy por Peso"] = busqueda_greedy(objetos, W, "peso")
resultados["Greedy por Densidad"] = busqueda_greedy(objetos, W, "densidad")

# Imprimir resultados formateados
print(f"{'Método':<20} | {'Valor ($)':<10} | {'Peso (kg)':<10} | {'Objetos':<20} | {'Tiempo (s)':<12}")
print("-" * 80)
for metodo, res in resultados.items():
    valor, peso, ids, t = res
    print(f"{metodo:<20} | {valor:<10} | {peso:<10} | {str(ids):<20} | {t:.8f}")
