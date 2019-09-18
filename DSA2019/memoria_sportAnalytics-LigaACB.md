# DSA2019 - Sport Analytics - Liga ACB

## Transformando el mundo del baloncesto a través de Sports Analytics en España

La analítica deportiva se entiende como el uso de estadísticas históricas y relevantes, que, aplicadas correctamente, pueden proporcionar una ventaja competitiva a un equipo o deportista. A través de la colección y el análisis de estos datos, la analítica deportiva puede ayudar a jugadores y entrenadores en el proceso de la toma de decisiones previo y durante los eventos deportivos.
Esta industria se popularizo masivamente tras el lanzamiento en 2011 de la película Moneyball, en la que el manager general del equipo de los Oakland Athletics de Béisbol, Billy Bean, basó la construcción de su equipo en métodos analíticos y cuantitativos. Conociendo la influencia de que los jugadores llegasen a bases para conseguir victorias, Beane se centró en fichar jugadores con un alto porcentaje de conversiones de base con la lógica de que los equipos con mayor porcentaje de conversiones de base eran más propensos a lograr carreras. Esto resultó en la construcción de un equipo tremendamente competitivo con el presupuesto más limitado de la Major League Baseball (MLB). Este éxito no pasó desapercibido para los ejecutivos de equipos profesionales de otros deportes. Hoy en día, y favorecido por el avance tecnológico, es difícil encontrar equipos profesionales que no utilizan datos para la toma de decisiones estratégicas.

Por ejemplo, el [Movistar Cycling Team](https://www.youtube.com/watch?v=LEreBnaDW2A), el [Movistar Riders](https://luca-d3.com/sports-analytics-2/index.html), la [Rafa Nadal Academy by Movistar](https://www.elmundo.es/promociones/native/2018/06/02/index.html) o el [Movistar Estudiantes de Baloncesto](https://luca-d3.com/sports-analytics-2/index.html) que ya implementan soluciones analíticas para impulsar la toma de decisiones deportivas basadas en datos.

Es precisamente de baloncesto sobre lo que trata este reto. Se busca encontrar ventajas competitivas para los equipos de baloncesto a partir del análisis de datos de partidos, equipos y jugadores. Al contrario que en Béisbol donde el rendimiento de cada jugador se puede cuantificar fácilmente, en el baloncesto los cinco jugadores son factores en cada jugada, y muchas de las contribuciones de algunos jugadores no se reflejan en las estadísticas tradicionales que se muestran al final de cada partido. Por ejemplo, los bloqueos o las ayudas defensivas rara vez se cuantifican en las estadísticas finales, pero ciertamente contribuyen favorablemente al equipo. Se trata por lo tanto de encontrar estadísticas avanzadas que vayan más allá de lo que se ve en las estadísticas tradicionales, con el fin de cuantificar lo más precisamente posible, el rendimiento de cada jugador, así como su impacto en el equipo.

Un claro ejemplo de cómo un equipo se ha beneficiado del poder de la analítica avanzada son los Houston Rockets. Como se observa en esta [noticia](https://as.com/baloncesto/2018/04/16/nba/1523870600_734693.html), se dieron cuenta mediante la analítica, que les convenía aumentar considerablemente los intentos de tiros de 3. En reacción a este cambio de juego, muchos equipos de la NBA han tomado medidas prescriptivas al respecto y han cambiado la manera de defender a los Houston Rockets. Algunas de ellas se han hecho virales como la [defensa](https://www.youtube.com/watch?v=buYqOJWc-fE&t=1s) de Ricky Rubio a James Hardem, jugador insignia de los Rockets.

### Objetivo

El objetivo de este reto es descubrir ventajas competitivas para los equipos españoles de baloncesto a partir de la analítica deportiva.
Como punto de partida sugerimos varias propuestas, pero el reto está abierto a otras posibilidades:
* Variables más influyentes en determinar el resultado de los equipos de la Liga Endesa
* Creación de KPI’s para evaluar el rendimiento deportivo de jugadores de la liga Endesa
* Análisis de los jugadores y equipos de la Liga Endesa durante el “clutch time” (durante el último cuarto con menos de 5 minutos para el final del partido y cuando ningún equipo tiene una ventaja de más de 5 puntos). Las estadísticas durante el “clutch” no están a priori disponibles abiertamente, pero se pueden extraer a partir del play-by-play
* Rendimiento según parámetros de estadísticas avanzadas por quintetos de todos los equipos (incluido el “clutch” de los quintetos)
* Diferencias en estadísticas avanzadas del jugador y del equipo cuando se gana y cuando se pierde
* Diferencias en estadísticas avanzadas del jugador y del equipo cuando juega en casa y cuando juega como visitante
* Análisis espacial de las posiciones desde las que los jugadores realizan tiros (coordenadas), del posicionamiento defensivo de los rivales...etc. Posterior creación de cartas de tiro para encontrar patrones da acierto o fallo en determinadas posiciones por determinados jugadores y equipos
* Categorización y clusterización de equipos y jugadores en base a su estilo de juego / estadísticas para encontrar jugadores y equipos que compartan patrones de juego
* Propuestas de fichajes de jugadores y de renegociación de contratos a partir de todas las propuestas anteriores

### Requisitos

Para realizar el reto existen los siguientes requisitos:
* Metodología científica del problema, donde se indica los pasos necesarios para obtener la solución al problema.
* Diseño e implementación de software, donde se justifican los motivos de utilización de una tecnología/software/algoritmo u otra.
* Explicación analítica del proceso de selección, aprendizaje y evaluación de los modelos usados en el proyecto.

### Data Set

Para este reto, proporcionamos algunos data sets que pueden ser utilizados por los participantes, pero aparte de estos data sets, se pueden utilizar otras fuentes adicionales.
Los data sets proporcionados son los siguientes:
* ACB_Players_18-19.xlsx: Data set con estadísticas avanzadas de los jugadores de la ACB durante la temporada 2018-2019.
* ACB_Players_2012to2018.xlsx: Data set con estadísticas avanzadas de los jugadores de la ACB desde la temporada 2011-2012 hasta la temporada 2017-2018.
* ACB_Teams_18-19.xlsx: Data set con estadísticas avanzadas de los equipos de la ACB durante la temporada 2018-2019.
* Dataset-Variables-Description.docx: Documento con la descripción de las variables de los data sets.

Se sugieren páginas de baloncesto especializadas como [RealGM](https://basketball.realgm.com/) o la página oficial de la [Liga ACB](http://www.acb.com/) para la obtención de datos abiertos sobre partidos, equipos y jugadores.

### Valoración

Para afrontar el reto, se valorarán los siguientes aspectos:
* El valor y la ventaja competitiva de los resultados
* La creatividad para encontrar “insights” más allá de los visibles a primera vista, así como el uso de técnicas descriptivas bien ejecutadas para su correcta visualización
* El uso de data sets adicionales que permiten “ insights” creativos
* Recomendaciones concretas para los equipos

## DESCRIPCIONES VARIABLES

#### RealGM's Basic Stat Line

G: Games

Min: Minutes

FGM-A: Field Goals Made - Field Goals Attempts

FG%: Field Goal Percentage

3PTM-A: Three-Point Field Goals Made – Three-Point Field Goals Attempted

3PT%: Three-Point Field Goal Percentage

FTM-A: Free Throws Made – Free Throws Attempted

FT%: Free Throw

FIC (Floor Impact Counter): A formula to encompass all aspects of the box score into a single statistic. The intent of the statistic is similar to other efficiency stats, but assists, shot creation and offensive rebounding are given greater importance. Created by Chris Reina in 2007. 

Formula: (Points + ORB. + 0.75 DRB + AST + STL + BLK –0.75 FGA – 0.375 FTA – TO – 0.5 PF)

FIC40 (Floor Impact Counter per 40 minutes): The FIC total presented on a per-40 minute basis.

OFF: Offensive Rebounds

DEF: Defensive Rebounds

REB: Total Rebounds

AST: Assists

STL: Steals

BLK: Blocks

TO: Turnovers

PTS: Points

#### Advanced/Misc. Stats

TS% (True Shooting Percentage): A measurement of efficiency as a shooter in field goal attempts, three-point field goal attempts and free throws.

Formula: (Points x 50) / [(FGA + 0,44 * FTA)]

eFG% (Effective Field Goal Percentage): A measurement of efficiency as a shooter in all field goal attempts with three-point attempts weighted fairly.

Formula: (FG + 0.5 * 3P) / FGA

ORB% (Offensive Rebound Percentage): A measurement of the percentage of offensive rebounds a player secures that are available to his team. 

Formula: 100 * [Player ORB * (Team Minutes / 5)] / [Player Minutes * (Team ORB + Opponent DRB)]

DRB% (Defensive Rebound Percentage): A measurement of the percentage of defensive rebounds a player secures that are available to his team.

Formula: 100 * [Player DRB * (Team Minutes / 5)] / [Player Minutes * (Team DRB + Opponent ORB)]

TRB% (Total Rebound Percentage): A measurement of the percentage of both offensive and defensive rebounds a player secures that are available to his team.

Formula: 100 * [Total Player Rebounds * (Team Minutes / 5)] / [Player Minutes * (Team Total Rebounds + Opponent Total Rebounds)]

AST% (Assist Percentage): A measurement of the percentage of assists a player records in relation to the team's overall total while he is in the game. 

Formula: 100 * Player ASTs / [((Player Minutes / (Team Minutes Played / 5)) * Team FGs) – Player FGs]

STL% (Steal Percentage): A measurement of the percentage of steals a player records in relation to the team's overall total while he is in the game.

Formula: 100 * [Player STLs * (Team Minutes / 5)] / (Player Minutes * Opponent Possessions)

BLK% (Block Percentage): A measurement of the percentage of blocks a player records in relation to the opponents two point field goal attemps.

Formula: 100 * [Player BLKs * (Team Minutes / 5)] / (Player Minutes * Opponent FGA - Opponent 3PA)

TOV% (Turnover Percentage): A measurement of the percentage of turnovers a player records in relation to the team's overall total while he is in the game.

Formula: 100 * Turnovers / (FGA + 0.44 * FTA + TOV)

Total S % (Total Shooting Percentage): The sum of a player's field goal, free throw and three-point percentage.

ORtg (Offensive Rating): The number of points a player produces per 100 possessions. Created by Dean Oliver.

DRtg (Defensive Rating): The number of points a player allows per 100 possessions. Created by Dean Oliver.

eDiff (Efficiency Differential): The difference between a team or player's ORtg and DRtg.

Formula: (ORtg - DRtg)

PER: An efficiency statistic created by John Hollinger. [Click here for more information.](https://en.wikipedia.org/wiki/Player_efficiency_rating)
