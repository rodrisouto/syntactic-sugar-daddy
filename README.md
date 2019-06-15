# 75.29 Teoría de Algoritmos (Advanced Algorithms) 
### Grupo: syntactic-sugar-daddy

---

## TP1
**Enunciado:** <https://algoritmos-rw.github.io/tda/2019-1c/tp1/>

**Informe:** <https://docs.google.com/document/d/1wukVApGxkKssDwqx8ksv96ne0KKz6ubpYY-vP4jp3y8/edit>

### Parte I: El Club “PICA-PICA”
##### Try it with:
```bash
# From top directory.
cd tp1
# Can use random or alphabetic as tie solvers.
python3 main.py 4 players.csv random
```

### Parte II: Funciones matemáticas / estadísticas
##### Try it with:
```bash
# From top directory.
cd tp1/collection-functions
python3 main_functions file.txt function
```
- file.txt: archivo de entrada, un número por línea.
- function: función a utilizar. Puede ser una de las siguientes:
    - maximo
    - media
    - mediana
    - moda
    - permutaciones
    - desviacion_estandar
    - variaciones
    - variaciones_repeticion

## TP2
**Enunciado:** <https://algoritmos-rw.github.io/tda/2019-1c/tp2/>

**Informe:** <https://docs.google.com/document/d/1nFYM8Y1zf6EJGmZUUowmsTsZ5lmmnx3fFJduSYzAQ-U/edit>

### Parte I: Laberintos”

#### Generar laberintos
##### Try it with:
```bash
# From top directory.
cd tp2/maze
# Can use d&c or dfs as maze generators.
python3 api_maze_generator.py 'd&c' 7 20
```

#### Resolver laberintos
##### Try it with:
```bash
# From top directory.
cd tp2/maze
# Can use d&c or dfs as maze generators.
python3 api_solve_maze a_maze.txt
```

### Parte II: El golpe comando
#### Try it with:
```bash
# From top directory.
cd tp2/suspects
python3 suspects_main.py filename_in.txt [filename_out.txt]
```
