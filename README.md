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
<p align="text-justify">
Un scraper no es más que un programa el cual tiene como finalidad extraer información de sitios web. Este tipo de programas regularmente simulan la navegación de un usuario a través del protocolo HTTP. 😎<br>
Podemos ver a un scraper como un pequeño bot, el cual, al nosotros indicar un target, es decir una página web, este comenzará un proceso de búsqueda y extracción de información. 🤖<br>
Al software diseñado para scrapear páginas web comúnmente lo conoceremos como bot, spider, crawler o simplemente web scraper.<br>
La ventaja de un web scraper recae en su automatización. Si bien es cierto nosotros podemos extraer información de páginas web, de forma manual, este proceso puede llevarnos una gran cantidad de tiempo y esfuerzo.<br>
Al nosotros realizar un web scraper debemos tomar muy en cuenta nuestro propósito. Recordemos que un scraper simula la navegación de un usuario. Si en dado caso nuestro programa no contempla ciertos parámetros, por ejemplo un número limitado de peticiones o la rapidez con que estas se hacen, podemos hacer que el sitio web el cual estamos scrapeando tenga un rendimiento lento o inclusive llegue colapsar. Es por ello que hay que ser muy conscientes en el número de peticiones y la forma en la cual obtendremos la página web .
</p>  

<h3 align="center">Tecnologias utilizadas</h3>

<h3 align="left">Languages and Tools:</h3>
<p align="left"> <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/> </a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.selenium.dev" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/detain/svg-logos/780f25886640cef088af994181646db2f6b1a3f8/svg/selenium-logo.svg" alt="selenium" width="40" height="40"/> </a> </p>

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

<h4 align="left">INSTANCIAR EL Chromedriver:</h4>
<p align="left">
</p>

<p>Dentro de una variable vamos a instanciar "chromedriver.exe", quien nos va a permitir hacer la simulación en el navegador y abrir la web a traves del metodo "driver.get()"</p>

[![Captura2.jpg](https://i.postimg.cc/zBZrW2kp/Captura2.jpg)](https://postimg.cc/wtVZYVZs)

<hr>

<h4 align="left">INSPECCIONAR LA WEB:</h4>
<p align="left">
</p>

<p>De esta manera podremos visualizar los elementos de la web que corresponde al contenido de la web. En nuestro caso como se trata de extraer datos correspondientes a la descripción, modelo y precio, hacemos un recorrido para detectar cual o cuales son esos elementos que se repiten dentro del codigo html, para asi usarlos como referencias a la hora de seleccionarlo con el "xpath" y almacenada en una variable</p>

[![Captura3.jpg](https://i.postimg.cc/fTtkxp7Q/Captura3.jpg)](https://postimg.cc/jLTsT8kM)

<hr>

<h4 align="left">BOTON Y CICLO FOR:</h4>
<p align="left">
</p>

<p>Al hacer scroll sobre la web, nos topamos con que la misma no sigue cargando mas aritculos, sino que tiene un boton "CARGAR MAS" la cual permite traer mas resultados en la busqueda. Es por eso que se tuvo que detercar a traves de una inspeccion de la web y traer en codigo el xpath del mismo, para luego automatizar el click con la funcion ".click()".</p>
<p>La funcion "sleep" cumple una función importante a la hora de la automatización, ya que el mismo permite darle un tiempo de espera a nuestro codigo y a la web, antes de seguir corriendo el script. Esta funcion debe ser lo mas parecida a un "humano", ya que si siempre damos un mismo valor, la web podria detectar que es un "robot" y asi es que evadimos si la misma tiene un detector de "bot", asi que es necesario "randomizar" ese intervalo de tiempo " sleep(random.uniform(8.0, 10.0))" Uniform lo que hace es darnos un valor aleatorio entre 8" y 10" </p>

[![Captura4.jpg](https://i.postimg.cc/436TZbz0/Captura4.jpg)](https://postimg.cc/sBgL4WHP)

<hr>
