# DSA2019 - GO MOVING - Sport Analytics Liga ACB
autor: Marco Russo
contact: mrusso@paradigmadigital.com
date: septiembre 2019


## Biography

Hola a todos, mi nombre es Marco Russo y para mí es un placer participar a este reto. De primera parto con bastante retraso por un imprevisto.

Sobre mí, tengo formación en ciencias económicas con especialización en finanza de mercado de valores y banca, sucesivamente he estudiado marketing, marketing digital , analítica de datos y finalmente con la UOC el posgrado de Business Analytics, además de formación en analítica de datos y aprendizaje automático.

Trabajo como consultor de datos y BI en Paradigma Digital en Madrid, empresa asociada con Indra en diferentes proyectos de transformación digital y área de Big Data (principalmente minería de datos y visualización). También soy formador in-company y apoyo en la formación de otros empleados en visualización de datos (las herramientas que utilizamos entre otras, Data Studio, Tableau, PowerBI principalmente), y nuestros clientes son casi la mayoría del Ibex35. A nivel interno trabajo en proyectos de apoyo al área de finanza y RRHH (business intelligence).

Por último desde hace 7 años he colaborado como docente impartiendo programas de comercio electrónico, marketing digital y datos en la Cámara de Comercio y otras escuelas de negocios como profesor de analítica principalmente. Cómo último profesor colaborador en la UOC en la asignatura de Data Mining y en NEOLAND como profesor principal del Máster de Data Science.

Me hace más ilusión el poder compartir estos retos a mis estudiantes a que yo lo envie, porque la verdad, me ha faltado tiempo.

Que gane el mejor!

gracias, un saludo
[marcusRB](www.marcusrb.com)

***

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




## Entrega del reto

La entrega del reto deberá contar con los siguientes documentos entregables:

Memoria del proyecto: Ésta se presentará en formato PDF y no podrá superar las 30 páginas. La fuente empleada en el contenido será Arial Narrow de tamaño 12pt con un interlineado sencillo. Dicha memoria estará dividida en los siguientes apartados:
Portada con título e identificación del concursante.
Metodología y planificación.
Descripción de los datos y procesamiento de los mismos.
Explicación justificada del diseño e implementación de la infraestructura y componentes/servicios usados.
Explicación justificada de la parte analítica (con validación analítica incluida).
Explicación justificada del Backend implementado (en caso de disponer).
Explicación justificada del Frontend implementado (en caso de disponer).
Demostración mediante ejemplos (casos de uso). Si fuera posible, enviar link a la aplicación interactiva implementada.
Ficheros que documenten el proyecto: código fuente, fuentes de datos, ...
Fichero descripción.txt que enumere y describa cada uno de los ficheros presentados (obligatorio).
Todos estos ficheros anteriormente descritos deberán ser almacenados (con directorios o no) en un fichero comprimido .zip, con el nombre que se desee. El fichero .zip no deberá ocupar más de 200MB, ya que el sistema no permite ficheros de tamaño superior.


***


# Resumen del trabajo

En mi opinión, el baloncesto es un deporte maravilloso, se puede decir mucho sobre una persona por la forma en que jugaba baloncesto, cosas como cogió la pelota? ¿Presumió en la cancha? ¿La persona tenía miedo de tirar y fallar? ¿La persona mintió acerca de haber recibido una falta? Además de eso, ¡es divertido jugar y hacer un gran ejercicio!

También en mi opinión, Data Analytics / Data Science es un campo increíblemente popular y en crecimiento, tanto es así que fue nombrado "el trabajo más sexy del siglo XXI". La ciencia de datos es una mezcla de estadísticas, análisis de datos, aprendizaje automático, informática y conocimiento de los datos / negocios que tiene como objetivo proporcionar información y comprensión de los datos.

Históricamente, la recogida de datos y el análisis de datos en los diferentes deportes se centra en estadísticas acumuladas anuales para comparar el desempeño de los diferentes jugadores, tanto que la liga amricana NBA ahora ejecuta un Hackathon anual, lo que les permite obtener nuevas ideas geniales y encontrar nuevos analistas de datos con talento.

Con el gran avance que se ha producido en la recogida y procesamiento de datos, existe la posibilidad de realizar análisis más avanzados. Serán análisis que nos permitan ponderar y realizar una clasificación, aplicando los conceptos del learning to rank, de los jugadores en función de aspectos que puedan ser influyentes a la hora de comparar su desempeño.

La hipótesis en que se basa este estudio sobre el baloncesto, en particular aplicado a la LIGA ACB es que hay dos factores interrelacionados que influyen en el desempeño y que no suelen tomarse en consideración.
El *primero*, es el conocimiento del juego que permite a un jugador aplicar la estrategia correcta según se plantee un problema en forma de defensa adversaria.
El *segundo* es la importancia del partido, ya que varía mucho según el momento de la temporada sea. Tomando como ejemplo en la NBA no existen descensos de categoría, la temporada regular es muy larga y en los playoffs las franquicias se juegan el trabajo de todo el año.

El objetivo de este estudio es conseguir un __análisis estadístico__ que tenga en cuenta ambos factores para poder comparar los puntos fuertes y débiles de los jugadores. El resultado del estudio aportará información que permita a los entrenadores y directores deportivos realizar una rápida toma de decisiones en un mercado de fichajes muy cambiante.


## Estructura del trabajo

Al disponer solo de pocos días a la semana para dedicar a este proyecto, es comenzado con una pequeña exploración de los datos proporcionados y tener un poco más la libertad de ver que hay más allá de estos dataset que se podemos concluir. Finalmente he visto muchos más trabajos y avanzados en este sentido, en la liga _NBA_ y la universitaria _NCAA_. De hecho hay sub-proyectos muy interesantes a la hora de poder abordar un __PoC__ con un equipo de baloncesto de la liga española.


Enumeraré los sub-proyectos que he ido enumerando que he estado desarrollando (y estaré trabajando con mis alumnos del próximo curso):

- **Data weareble**: Utilizar los datos biométricos a la hora de detectar con antelación los posibles cambios durante el partido. Se ha comprobado el mismo a través de la aplicación conocida en este mundo del deporte (y que se utiliza bastante en Movistar Cycling), **STRAVA**, además de utilizar los variables propias del jugador y así crear un nueva métrica con el fin de obtener: _%potencia_, _%cansancio_, _%lucidez_, _%lesiones_, _%respiración_, _%pulsaciones_, _%impacto_, _%estado_estrés_, etc. Además viendo muchos videojuegos utilizan exactamente un algoritmo muy similar. Aquí la noticia [NBA and RDF](https://www.zdnet.com/article/nba-analytics-and-rdf-graphs-game-data-and-metadata-evolution-and-occams-razor/)

Acompañando este primer sub-proyecto, hablaré del __Perfomance_Analysis__ que obviamente al faltar los primeros datos que creo sean muy útiles para determinar la métrica que hasta ahora se calcula de una manera, __PER__, el control de datos biométricos muy importantes para tomar decisiones basadados en tiempo real de dispositvos visto anteriormente, el atleta tendrá en todo momento incluso alertas de cuando está llegado a su límite de fuerzas.

- **Deep Learning aplicado a los tiros**: Otro sub-proyecto a realizar y ya estudiando en la _NCAA_ es la capacidad de estudiar a través de técnicas de deep-learning y redes neuronales a estudiar y ser capaz de detectar a una distancia x con otros factores si el equipo va a canasta o no. El artículo que hace mención a esto es en [FiveThirtyEight](https://fivethirtyeight.com/features/how-mapping-shots-in-the-nba-changed-it-forever/).

- **Track de Movimientos**: Una de las cosas más interesantes es un estudio desde 2009 de grabacione de partidos, que están aprovenchando con __Tensorflow__, __Keras__, __PyTorch__, para analizar cada uno de ellos y detectar patrones. Aquí el extracto :

> _En 2009, la liga comenzó a utilizar un sistema de video de última generación para rastrear el movimiento de los jugadores en la cancha y la pelota. Tener este nuevo sistema de video le permitió a la NBA recopilar nuevos datos, lo que a su vez permitió a los científicos de datos utilizar el aprendizaje automático y la cartografía (la ciencia o la práctica de dibujar mapas) para evaluar mejor qué jugadores ayudaron a su equipo a ganar_.

- **Rediseñando el equipo** : Será que la NBA es otro nivel que sin duda ni se acerca a cualquier europea (hasta incluso pienso que ni la NCAA), pero sin embargo algo se mueve en la dirección correcta y hay físicos, científicos, matemáticos, analistas, estadísticos tan buenos como en EEUU, así mejor aprovecharlo al máximo. Lo que se estudio lo que muestro a continuación es algo muy amplio y basado en un _método de clasificación_. [Estudio completo](http://www.sloansportsconference.com/wp-content/uploads/2012/03/Alagappan-Muthu-EOSMarch2012PPT.pdf?utm_source=twitter&utm_medium=socialmedia&utm_campaign=wiredplaybookclickthru)

> ¿Se ha preguntado por qué solo hay 5 posiciones en el baloncesto o cómo se determina la posición de un jugador? Nosotros también. Pero ahora, utilizando el motor de análisis de datos patentado de Ayasdi y décadas de investigación de topología computacional en Stanford, hemos categorizado matemáticamente a los jugadores en 13 nuevas posiciones: las posiciones reales del baloncesto (que se presentará en esta presentación). Describiré esta visión revolucionaria y cómo puede agregar un gran valor para los entrenadores, propietarios, gerentes generales y fanáticos de todos los días. Al visualizar la forma de los datos en términos de posiciones basadas en el rendimiento, podemos descubrir jugadores infravalorados, administrar decisiones en el juego, optimizar listas y redactar de manera más inteligente. Y esta mayor granularidad en las posiciones de baloncesto es solo el comienzo. También describiré cómo el análisis de datos topológicos puede abrir el camino a más evoluciones en los pensamientos en el baloncesto y otros deportes.


## Métricas

Aquí unas cuantas métricas recogidas, separadas por:

* Moneyball
* Player Evaluation Metrics
* Team Evaluation Metrics

cada una están indicadas y especificadas en [nbastuffer](https://www.nbastuffer.com/analytics-101/)
