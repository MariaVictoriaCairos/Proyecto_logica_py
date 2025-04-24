# Proyecto_logica_py

**Katas de lógica de programación en Python**

**Autora:** María Victoria Cairós Gonzalez
**Fecha:** Abril de 2025

### Entrega: 
Se presenta un archivo unificado con todos los ejericios denominado Logica_python.py. Además, se entregan los ejercicios de forma independiente.  
### a) Todos los ejercicios se les aplicó:

- **Entrada interactiva**: Todos los ejercicios están diseñados para que el usuario proporcione los datos necesarios durante la ejecución del programa. Esto permite una mayor flexibilidad, ya que el comportamiento del código puede variar en función de la entrada del usuario.

- **Validación de datos**: 
  - Antes de procesar cualquier entrada, se realizan comprobaciones para asegurar que los datos introducidos cumplen con el formato esperado (por ejemplo, que sean números cuando se esperan números, o cadenas sin caracteres especiales cuando se espera texto limpio).
  - Se han implementado estructuras condicionales (`if`, `try-except`) para manejar errores comunes como valores fuera de rango, tipos de datos incorrectos o entradas vacías.
  - En algunos casos, si el usuario introduce un valor no válido, se le solicita que lo intente de nuevo hasta que la entrada sea aceptable.

- **Robustez en la ejecución**: Estas medidas aseguran que los programas no se detendrán inesperadamente debido a entradas erróneas y pueden guiar al usuario hacia el uso correcto.

- **Comentarios explicativos**: Cada bloque de código contiene comentarios que describen su función y propósito. Estos comentarios están diseñados para facilitar la comprensión del flujo lógico del programa, siendo especialmente útiles para quienes están aprendiendo programación o desean revisar el código con claridad.

- **Experiencia educativa**: Este enfoque fomenta la comprensión de cómo interactuar con programas dinámicos y cómo diseñar software que sea resistente a fallos de entrada, una habilidad clave en el desarrollo de software.


---

## Funciones Definidas en `Logica_python.py`

| **Función/Clase**        | **Descripción**                                                                                   |
|--------------------------|---------------------------------------------------------------------------------------------------|
| `contar_frecuencias`     | Cuenta las frecuencias de letras en una cadena, ignorando espacios.                               |
| `filtrar_por_palabra`    | Filtra una lista de palabras que contengan una palabra objetivo.                                  |
| `diferencia_listas`      | Calcula la diferencia entre elementos de dos listas usando `map()`.                               |
| `Buscar_nombre`          | Busca un nombre en una lista ingresada por el usuario.                                            |
| `Buscar_empleado`        | Busca el cargo de un empleado en un diccionario.                                                  |
| `agregar_elementos`      | Agrega elementos a una lista a partir de una entrada de usuario.                                  |
| `valora_anagrama`        | Verifica si dos palabras son anagramas.                                                           |
| `calcula_aprobado`       | Calcula si un promedio es aprobado o no, basado en una lista de notas.                            |
| `Mascotas_España`        | Filtra mascotas permitidas en España según una lista prohibida.                                   |
| `calcular_promedio`      | Calcula el promedio de una lista de números, lanza excepción si está vacía.                       |
| `lista_palabras`         | Devuelve una lista con las longitudes de cada palabra de una frase.                               |
| `listar_tuplas`          | Genera una lista de tuplas con versiones mayúsculas y minúsculas de caracteres únicos.            |
| `buscar_por_letra`       | Filtra una lista de palabras que comienzan por una letra dada.                                    |
| `suma_lista`             | Suma 3 a cada número de una lista.                                                               |
| `filtro_tamaño`          | Filtra palabras de una lista que tengan más de cierta longitud.                                   |
| `Genera_numero`          | Concatena dígitos de una lista para formar un número.                                             |
| `cuenta_caracteres`      | Cuenta caracteres totales, sin espacios, letras, números y espacios de una cadena.                |
| `promedio`               | Calcula el promedio de una lista de números.                                                      |
| `duplicado`              | Encuentra el primer elemento duplicado en una lista.                                              |
| `transformar`            | Enmascara una cadena con `#` excepto los últimos 4 caracteres.                                     |
| `contar_palabras`        | Cuenta las apariciones de cada palabra en un texto.                                               |
| `reemplazar_palabras`    | Reemplaza palabras en un texto.                                                                  |
| `eliminar_palabra`       | Elimina una palabra específica de un texto.                                                       |
| `procesar_texto`         | Procesa un texto según la opción: contar, reemplazar o eliminar palabras.                         |
| `Arbol` (Clase)          | Modela un árbol con métodos para manipular el tronco y las ramas.                                 |
| `UsuarioBanco` (Clase)   | Modela un usuario de banco, permite transferir, agregar y retirar dinero.                         |
| `Calcula_area`           | Calcula el área de un rectángulo o triángulo.                                                     |
| `resto` (lambda)         | Calcula el resto de una división.                                                                |
| `cubo` (lambda)          | Calcula el cubo de un número.                                                                    |

---

## Comandos y Funciones de Python Utilizados

| **Comando/Función**    | **Descripción**                                                                                    |
|------------------------|----------------------------------------------------------------------------------------------------|
| `int()`                | Convierte una cadena (o número flotante) a un número entero.                                       |
| `zip(lista1, lista2)`  | Une elementos de dos listas en pares: `[(a1, b1), (a2, b2), ...]`.                                 |
| `lambda`               | Crea una función anónima (sin nombre) en una sola línea.                                           |
| `print()`              | Muestra texto o valores en la consola.                                                             |
| `raise ValueError()`   | Lanza un error si se cumple una condición (no se usó directamente aquí).                          |
| `if`, `elif`, `else`   | Condicionales para ejecutar diferentes bloques de código según condiciones.                       |
| `for`, `while`         | Bucles para repetir bloques de código.                                                            |
| `try`, `except`        | Manejo de excepciones para capturar errores durante la ejecución.                                  |
| `input()`              | Recibe datos del usuario por consola.                                                              |
| `map()`                | Aplica una función a cada elemento de una lista (u otro iterable).                                |
| `filter()`             | Filtra elementos de una lista según una condición dada.                                           |
| `set()`                | Crea un conjunto, útil para eliminar duplicados.                                                  |
| `len()`                | Devuelve la longitud de una lista, cadena, etc.                                                    |
| `sorted()`             | Devuelve una lista ordenada.                                                                      |
| `lower()`, `upper()`   | Convierte cadenas a minúsculas o mayúsculas respectivamente.                                       |
| `append()`             | Agrega un elemento al final de una lista.                                                         |
| `split()`              | Divide una cadena en partes, según un separador (por defecto, espacio).                           |


