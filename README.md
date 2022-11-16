# Hi, we are the group SSSST5 👋
[![flayer.png](https://i.postimg.cc/28bSv0fN/flayer.png)](https://postimg.cc/D8hh3dZx)

<hr>

## about us and the code

```js
const sssst5 = {
  pronouns: "he" | "she" | "they",
  code: [Python, HTML, CSS],
  tools: [PowerBi, SQL Server, Tableau],
}
```

##  COLABORADORES ✌
* __Sena Martin ismael__
* __Sierra Fernando__
* __Soria Julio Ezequiel__
* __Tissera Jorgelina__

> Esto es lo que una computadora significa para mi: es la herramienta más notable que hemos logrado tener. Es como una bicicleta para nuestras mentes. - Steve Jobs

<hr>

<h4 align="left">1)¿Qué es un web Scraper?</h4>
<p style="text-align: justify;">
Un scraper no es más que un programa el cual tiene como finalidad extraer información de sitios web. Este tipo de programas regularmente simulan la navegación de un usuario a través del protocolo HTTP. 😎<br>
Podemos ver a un scraper como un pequeño bot, el cual, al nosotros indicar un target, es decir una página web, este comenzará un proceso de búsqueda y extracción de información. 🤖<br>
Al software diseñado para scrapear páginas web comúnmente lo conoceremos como bot, spider, crawler o simplemente web scraper.<br>
La ventaja de un web scraper recae en su automatización. Si bien es cierto nosotros podemos extraer información de páginas web, de forma manual, este proceso puede llevarnos una gran cantidad de tiempo y esfuerzo.<br>
Al nosotros realizar un web scraper debemos tomar muy en cuenta nuestro propósito. Recordemos que un scraper simula la navegación de un usuario. Si en dado caso nuestro programa no contempla ciertos parámetros, por ejemplo un número limitado de peticiones o la rapidez con que estas se hacen, podemos hacer que el sitio web el cual estamos scrapeando tenga un rendimiento lento o inclusive llegue colapsar. Es por ello que hay que ser muy conscientes en el número de peticiones y la forma en la cual obtendremos la página web .
</p>  

<h3 align="center">Tecnologias utilizadas</h3>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> </p>

<hr>

<h4 align="center">
Propuesta del proyecto
</h4>

<p>
Extraer y comparar los valores de los autos usados de la web https://www.olx.com.ar/autos_c378 con respecto a los valores de los sueldos actuales en Argentina de algunas profesiones como: Docentes, Industria IT, Comercio, etc. La idea es poder lograr predecir cuanto tiempo le llevaria a un trabajador poder comprarse un auto, teniendo en cuenta el valor de la canasta basica según el INDEC (Instituto Nacional de Estadisticas y Censos).
</p>

<h4 align="center">
Detalles del codigo y sus funciones:
</h4>
<p>
Selenium tecnicamente hablando es un driver que nos permite a nosotros desde un lenguaje de programacion, poder automatizar las acciones que realiza el navegador, como si fuera un humano quien esta realizando las acciones, como por ejemplo "hacer click, sobre determinado boton", hacer un "scroll", "paginacion" y "extraer informaciòn" de la web indicada.
</p>

<h4 align="left">1) IMPORTAMOS LAS LIBRERIAS A UTILIZAR</h4>
<p align="left">
</p>

[![Captura1.jpg](https://i.postimg.cc/fbTpmjx1/Captura1.jpg)](https://postimg.cc/HrR6CMvt)

<h4 align="left">LIBRERIAS USADAS EN EL PROYECTO:</h4>
<p align="left">
</p>

*[Selenium](#Selenium)

*[Time](#Time)

*[Random](#Random)

*[Pandas](#Pandas)
<hr>

<h4 align="left">2) INSTANCIAR EL Chromedriver:</h4>
<p align="left">
</p>

<p>Dentro de una variable vamos a instanciar "chromedriver.exe", quien nos va a permitir hacer la simulación en el navegador y abrir la web a traves del metodo "driver.get()"</p>

[![Captura2.jpg](https://i.postimg.cc/zBZrW2kp/Captura2.jpg)](https://postimg.cc/wtVZYVZs)

<hr>

<h4 align="left">3) INSPECCIONAR LA WEB:</h4>
<p align="left">
</p>

<p style="text-align: justify;">De esta manera podremos visualizar los elementos de la web que corresponde al contenido de la web. En nuestro caso como se trata de extraer datos correspondientes a la descripción, modelo y precio, hacemos un recorrido para detectar cual o cuales son esos elementos que se repiten dentro del codigo html, para asi usarlos como referencias a la hora de seleccionarlo con el "xpath" y almacenada en una variable</p>

[![Captura3.jpg](https://i.postimg.cc/fTtkxp7Q/Captura3.jpg)](https://postimg.cc/jLTsT8kM)

<hr>

<h4 align="left">4) BOTON Y CICLO FOR:</h4>
<p align="left">
</p>

<p>Al hacer scroll sobre la web, nos topamos con que la misma no sigue cargando mas aritculos, sino que tiene un boton "CARGAR MAS" la cual permite traer mas resultados en la busqueda. Es por eso que se tuvo que detercar a traves de una inspeccion de la web y traer en codigo el xpath del mismo, para luego automatizar el click con la funcion ".click()".</p>
<p>La funcion "sleep" cumple una función importante a la hora de la automatización, ya que el mismo permite darle un tiempo de espera a nuestro codigo y a la web, antes de seguir corriendo el script. Esta funcion debe ser lo mas parecida a un "humano", ya que si siempre damos un mismo valor, la web podria detectar que es un "robot" y asi es que evadimos si la misma tiene un detector de "bot", asi que es necesario "randomizar" ese intervalo de tiempo " sleep(random.uniform(8.0, 10.0))" Uniform lo que hace es darnos un valor aleatorio entre 8" y 10" </p>

[![Captura4.jpg](https://i.postimg.cc/436TZbz0/Captura4.jpg)](https://postimg.cc/sBgL4WHP)

<hr>

<h4 align="left">5) SEGUNDO CICLO FOR Y DICCIONARIO:</h4>

<p style="text-align: justify;">Este paso es importante, ya que debemos identificar los elementos que queremos extraer de la web y cuale o cuales son los atributos que la representan dentro del codigo HTML. Decidimos identificarlo a traves de un "xpath" ya que es la forma mas acertada y la cual podria generar menos errores a futuro en en recorrido de los datos a scrapear.<br> Los elementos a obtener son: PRECIOS, DESCRIPCION, AÑO Y KM. Las mismas son identificadas a traves de xpath y almacenadas en una variable distintiva para cada una y a su vez tenian la funcion "append" el cual cumplira con el almacenamiento de los datos extraidos. En la ultimas dos, nos surgio un problema, ambos elementos estaban alojados dentro de un mismo xpath: './/span[@data-aut-id="itemDetails"]', el cual tenia tanto AÑO como KM y se las necesitaba de manera separada para poder luego hacer la parte estadistica.<br> Por este motivo, luego del segundo ciclo for, se agrega uno mas el cual va a recorrer el ultimo xpath y se le da como intruccion a traves del metodo "lista=i.split('-')" que va a detectar el separador y va a almacenar los datos por separado "año.append(lista[0]), km.append(lista[1])". De esta manera pudimos comprobar a traves de un "print" que los datos ya estaban en columnas por separado.<br> Por ultimo, se almacenan los datos en una variable *"mi_diccionario"* para luego ser alojado en un *DataFrame*.</p>

[![Captura5.jpg](https://i.postimg.cc/KY1RNYgf/Captura5.jpg)](https://postimg.cc/67NW6tc4)

<hr>

<h4 align="left">6) PASAJE DE DATOS A UN CSV:</h4>

<p>En este ultimo paso realizamos el pasaje de los datos a un archivo CSV la cual luego nos va a permitir poder trabajar con herramientas de visualizacion.</p>

[![Captura6.jpg](https://i.postimg.cc/W1jL2YnP/Captura6.jpg)](https://postimg.cc/pp01CZ40)

<hr>

<h4 align="center">
Conclusión final
</h4>
<p style="text-align;"> Mediante el archivo CSV obtenido con la técnica de Web Scrapping se realizo el análisis de los datos, para lo cual se decidio trabajar con rangos de precios de autos. Los intervalos que se consideraron son: de $500000 a $1.5M, de $1.5M a $2.5M, de $3.5M a $5M, de $5M a $6.5M y mayores de $6.5M. El propósito de estos intervalos fue el de obtener un valor promedio de los automóviles en los intervalos analizados</p>

[![Captura7.png](https://i.postimg.cc/8cKrbFfk/Captura7.png)](https://postimg.cc/T5bwd3cB)


<p style="text-align;"> Con esta información que fuimos obteniendo además de quedar guardada en un archivo CSV se decidio plasmarla en gráficos de forma tal que resulte más amigable para interpretarla. Se realizó un gráfico de torta, que nos muestra el porcentaje de autos que hay en cada rango de precio; y también un gráfico de barras con la cantidad de años según el modelo de auto. Si bien la técnica de Scrapping se llevo a cabo en 512 elementos, varios tuvieron que ser descartados, ya que no incluian el valor del auto, que es fundamental para realizar nuestro análisis</p>

[![Captura-de-pantalla-5.png](https://i.postimg.cc/JhMZMW8L/Captura-de-pantalla-5.png)](https://postimg.cc/nXSCGgMR)

[![Captura-de-pantalla-6.png](https://i.postimg.cc/28WH2v7X/Captura-de-pantalla-6.png)](https://postimg.cc/0b8dNz3p)

[![Captura-de-pantalla1.png](https://i.postimg.cc/9fsR84pJ/Captura-de-pantalla1.png)](https://postimg.cc/WD61t1xk)

<p style="text-align,"> Tambien se recopilo información a traves de un archivo CSV de los sueldos según el cargo, para poder realizar promedios en rangos de salarios con el fin de poder determinar la cantidad de meses que le puede llevar a una persona dependiendo de su capacidad de ahorro</p>

[![Captura-de-pantalla-8.png](https://i.postimg.cc/Ss79nS6d/Captura-de-pantalla-8.png)](https://postimg.cc/mzkkqG61)

<p style="text-align,"> Con dicha información se planteo la búsqueda de sueldos promedios en función de intervalos que planteamos. Los intervalos que se analizaron son: sueldos menores a $150000, sueldos entre $150000 y $300000, sueldos entre $300000 y $500000 y sueldos mayores a $500000. A los sueldos promedio que encontramos en estos intervalos se les desconto el valor de la canasta básica, con el fin de obtener la capacidad de ahorro. </p>

[![Captura-de-pantalla-9.png](https://i.postimg.cc/fyM0QG0P/Captura-de-pantalla-9.png)](https://postimg.cc/JDdhbdx3)

<p style="text-align,"> Cabe destacar que fueron finalmente excluidos del análisis el primer intervalo de Sueldos, ya que no cubren las necesidades básicas de la canasta familiar, se realizaron graficas con los porcentajes según los rangos de sueldos. También se presenta un gráfico de barras que refleja la capacidad de ahorro que se tiene según el intervalo de sueldos que se analiza </p>

[![Captura-de-pantalla-11.png](https://i.postimg.cc/PJqr4TDd/Captura-de-pantalla-11.png)](https://postimg.cc/R6jBCrGY)


[![Captura-de-pantalla-12.png](https://i.postimg.cc/PqhHydG0/Captura-de-pantalla-12.png)](https://postimg.cc/9DxsF5QB)


<p style="text-align,"> Con todos la información obtenida se procede a hacer el análisis de el tiempo estimado en meses que demorara una persona en poder adquirir un auto, esto dependerá, de su capacidad de ahorro y del valor del vehículo que quiera adquirir, se presentan las conclusiones y también se realizan los gráficos que hacen referencia a dicho informe </p>

[![Captura-de-pantalla-13.png](https://i.postimg.cc/15hyXGC9/Captura-de-pantalla-13.png)](https://postimg.cc/Hj2qPy1K)
<br>
[![Captura-de-pantalla-14.png](https://i.postimg.cc/3JS99Bsh/Captura-de-pantalla-14.png)](https://postimg.cc/dLC8V8QN)
<br>


[![Captura-de-pantalla-15.png](https://i.postimg.cc/xT4yLdmT/Captura-de-pantalla-15.png)](https://postimg.cc/mt7HsBV0)
<br>

[![Captura-de-pantalla-16.png](https://i.postimg.cc/VLrbQWSm/Captura-de-pantalla-16.png)](https://postimg.cc/2VY5nvFK)


[![Captura-de-pantalla-17.png](https://i.postimg.cc/PJBJr0Lh/Captura-de-pantalla-17.png)](https://postimg.cc/4HQsWLbF)






