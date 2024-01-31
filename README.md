
Carrera de vehículos 🏁
Este programa simula una carrera entre un coche 🚗, una moto 🏍 y un dragón 🏃‍♂️ 🐉 en un tramo de carretera con obstáculos. Cada vehículo avanza aleatoriamente evitando los obstáculos (representados por árboles 🌲) hasta alcanzar la meta (🏁).

Requisitos
Python 3.x instalado en tu sistema.
Ejecución
Clona este repositorio o descarga el archivo race.py.
Abre una terminal o línea de comandos en el directorio donde se encuentra el archivo Carrera_cochecitos.py.
Ejecuta el siguiente comando para iniciar la carrera:
Copy code
python Carrera_cochecitos.py
Descripción del código
start_race(): Esta función muestra una secuencia de luces de semáforo para indicar el inicio de la carrera.
race(track_length): Esta función principal inicia la carrera, crea las pistas con obstáculos aleatorios, mueve los vehículos y verifica quién gana.
create_tracks(track_length): Esta función crea las pistas para los tres vehículos con una longitud especificada y coloca obstáculos aleatorios (árboles 🌲) en ellas.
print_race(track1, track2, track3): Esta función imprime visualmente el progreso de la carrera mostrando las posiciones de los vehículos en las pistas.
check_race(position1, position2, position3): Esta función verifica quién ha ganado la carrera según las posiciones finales de los vehículos.
Personalización
Puedes ajustar la longitud de la pista modificando el valor pasado a la función race().
También puedes modificar los símbolos utilizados para representar los vehículos y los obstáculos cambiando los caracteres Unicode en el código.
¡Disfruta de la carrera y que gane el mejor vehículo!
