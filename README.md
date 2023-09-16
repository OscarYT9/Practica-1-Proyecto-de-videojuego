# **Practica-1-Proyecto-de-videojuego**
# <p> <sub>`Tiempo restante`</sub> <img src="https://gen.sendtric.com/countdown/v014ytpdbo" alt="Descripción de la imagen" align="center" width="300" /> <sub>`Click para abrir`</sub> <a  href="https://codesandbox.io/p/github/OscarYT9/Practica-1-Proyecto-de-videojuego/draft/1?workspaceId=a923da0c-be0a-4c5f-a6e5-15ed3514b8c6&file=%2FREADME.md&workspace=%257B%2522activeFileId%2522%253A%2522cle8er4sd0000g4jvesqp9pcq%2522%252C%2522openFiles%2522%253A%255B%2522%252FREADME.md%2522%255D%252C%2522sidebarPanel%2522%253A%2522EXPLORER%2522%252C%2522gitSidebarPanel%2522%253A%2522COMMIT%2522%252C%2522spaces%2522%253A%257B%2522cleauevoq001d336jzl1lezqf%2522%253A%257B%2522key%2522%253A%2522cleauevoq001d336jzl1lezqf%2522%252C%2522name%2522%253A%2522Default%2522%252C%2522devtools%2522%253A%255B%255D%257D%257D%252C%2522currentSpace%2522%253A%2522cleauevoq001d336jzl1lezqf%2522%252C%2522spacesOrder%2522%253A%255B%2522cleauevoq001d336jzl1lezqf%2522%255D%252C%2522hideCodeEditor%2522%253Afalse%257D"><img src="https://codesandbox.io/favicon.ico" alt="CodeSandbox" height="40" style="vertical-align:top; margin:4px"></a> </p>


## 1. Introducción
<details open>
  <summary>📝Prácticas</summary>
  	<details open>
	<summary style="text-align:center;" pointer-events: none;"><img src="https://user-images.githubusercontent.com/113378321/227663867-0a1c397d-c997-43f5-9459-91057135a331.gif" width="40px">Práctica 1</summary>
	
### 1.1 Programación orientada a objetos
>Una compañía de videojuegos quiere comprobar el equilibrio entre los personajes de su próximo juego 
de lucha. Nos envía documentación relativa al conjunto P de N personajes del juego (PJs) y a la lógica 
del combate para que programemos distintas simulaciones y evaluemos si siempre resulta ganador 
un PJ de la misma clase. La documentación incluye varios ficheros de prueba con personajes ya 
definidos (prueba1.txt, prueba2.txt, prueba3.txt) y un main.py con código para abrir y leer los ficheros. [p1.pdf](https://github.com/OscarYT9/Practica-1-Proyecto-de-videojuego/files/10770799/p1.pdf)

### 1.2 Diagrama de clases

```mermaid
%%{init: {'theme': 'dark',
'lineColor': '#F8B229'}}%%
classDiagram
  Avatar <|-- Melee
  Avatar <|-- Caster
  Melee <|-- Warrior
  Caster <|-- Mage

  class Avatar{
    #name string
    #life int
    #strength int
    #defense int
    #weapon  None
    #armor   None
    `#level int`
    
    +get_life()
    +set_life()
    +get_name()
    +set_name()
    +get_strength()
    +set_strength()
    +get_defense()
    `+get_weapon()`
    +get_armor()
    +set_armpt()
    +attack()
    +defend()
    +equip()
  }
  
  class Melee{
	#shield None
	
	+get_shield()
	+set_shield()
    +set_weapon()
    `+use_weapon()`
  }
  
  class Caster{
    +mana int
    `+intelligence int`
    
	 get_mana()
	 set_mana()
	 set_weapon()
    `+castSpell()`
  }
  
  class Warrior{
    -fury int
    `-weaponType string`
    
    -get_fury()
    -set_fury()
    -attack()
    -defend()
  }
  
  class Mage{
    `-element string`
    
    -attack()
    -defend()
    `-summon()`
}


```
### 1.3 Diagrama de objetos

```mermaid
%%{init: {'theme': 'dark',
'lineColor': '#F8B229'}}%%
classDiagram
  Item <|-- Covering
  Item <|-- Weapon
  Covering <|-- Armor
  Covering <|-- Shield
  Weapon <|-- Sword
  Weapon <|-- Hand

  class Item{
    +String name
    +int value
    +equip()
    +use()
  }
  
  class Covering{
    +int defense
    +protect()
  }
  
  class Weapon{
    +int damage
    +attack()
  }
  
  class Armor{
    -String material
    -absorb()
  }
  
  class Shield{
    -String shape
    -block()
  }
  
  class Sword{
    -String bladeType
    -slash()
  }
  
  class Hand{
    -String gloveType
    -punch()
}
```
</details>
<details open>
	<summary style="text-align:center;"><img src="https://user-images.githubusercontent.com/113378321/227663814-05674c31-2426-4d3c-9021-4baf6c1831f3.gif" width="40px">Práctica 2</summary>
	
### 1.4 Colas
>El control de vuelo de un aeropuerto necesita un nuevo programa informático que gestione el 
despegue de aviones. Este proceso se realizará siguiendo el orden establecido por una prioridad 
que viene determinada por la clase de vuelo. [Practica_2.pdf](https://github.com/OscarYT9/Practica-1-Proyecto-de-videojuego/files/11066198/Practica_2.pdf)

| Clase de vuelo | Prioridad |
| --- | --- |
| Doméstico | 1 (MAX) |
| Privado | 2 |
| Regular | 3 |
| Charter | 4 |
| Transoceánico | 5 (MIN) |

</details>
<details open>
	<summary style="text-align:center;"><img src="https://user-images.githubusercontent.com/113378321/232179870-fb58e526-751a-48bd-886b-5dd723f06c39.gif" width="40px">Práctica 3</summary>
	
### 1.5 Listas posicionales ordenadas
>En esta práctica, se simulará la gestión del servicio de préstamos de una biblioteca. De cada libro tenemos 
la  siguiente  información:  Título  del  libro,  Autor,  Año  de  edición  y Número  de  préstamos  realizados.  En  la 
actualidad, la biblioteca posee un listado ineficiente y no ordenado en el que puede haber múltiples copias 
y/o ediciones de cada libro. [P3.pdf](https://github.com/OscarYT9/Practica-1-Proyecto-de-videojuego/files/11238155/P3.pdf)
 
**Se pide implementar un sistema con menú que permita realizar las siguientes acciones:**
<ol>
  <li><strong>Leer de un fichero los datos sobre los libros y almacenarlos en una lista posicional ordenada:</strong><br>
    <ul>
      <li>Los libros deben ser ordenados por autor, título y año de edición.</li>
    </ul>
  </li><br>

  <li><strong>Determinar la media de préstamos por libro:</strong><br>
    <ul>
      <li>Calcular el promedio de préstamos realizados por cada libro en la biblioteca.</li>
    </ul>
  </li><br>

  <li><strong>Eliminar los libros con mismo título y autor:</strong><br>
    <ul>
      <li>Dejar solo la versión más reciente de los libros con mismo título y autor.</li>
    </ul>
  </li><br>

  <li><strong>Visualizar en pantalla un listado tabulado de libros:</strong><br>
    <ul>
      <li>Se puede elegir entre todos los libros de la biblioteca, los escritos por un autor específico o los editados en un año determinado por el usuario.</li>
      <li>Si hay varias copias y/o ediciones de un libro, se deben incluir todas en el listado.</li>
    </ul>
  </li><br>
</ol>



| Objetivos |
| --- |
| Las estructuras de datos deberán manipular objetos de una clase Libro, que incluirá las variables de instancia y métodos necesarios, respetando los principios de orientación a objetos (herencia, encapsulación y polimorfismo). |
| Todo el procesamiento se realizará con el TAD Lista Posicional. La práctica debe funcionar (alternativamente) con ambas implementaciones (array_ordered_positional_list y linked_ordered_positional_list). |

*Queda por implementar correctamente una función*

</details>
<details open>
	<summary style="text-align:center;"><img src="https://github.com/OscarYT9/Practica-1-Proyecto-de-videojuego/assets/113378321/a91e9b85-6be2-4923-8076-a735947e0cb2" width="40px">Práctica 4</summary>

### 1.6 Árboles AVL
>Dos empresas de “Actividades de Ocio” A y B han decidido fusionarse, dando lugar 
a la empresa C. Para generar su nuevo catálogo, precisan conocer la “suma de 
actividades” (las ofertadas en al menos una de las empresas) y a la “oferta mínima 
común” (las ofertadas en ambas empresas). [P4.pdf](https://github.com/OscarYT9/Practica-1-Proyecto-de-videojuego/files/12639759/P4.pdf)


- Fusión de Empresas (Empresa C)
  - Suma de Actividades
    - Actividades de la Empresa A
    - Actividades de la Empresa B
  - Oferta Mínima Común
    - Actividades Comunes a A y B
  - Datos de las Actividades
    - Actividad 1
      - Nombre: [Nombre de la Actividad 1]
      - Duración: [Duración en minutos]
      - Número de Participantes: [Número de Participantes]
      - Precio Total: [Precio Total]
    - Actividad 2
      - Nombre: [Nombre de la Actividad 2]
      - Duración: [Duración en minutos]
      - Número de Participantes: [Número de Participantes]
      - Precio Total: [Precio Total]
    - ...

</details>
</details>

## **2. Programas utilizados**
<div style="max-width: 600px; display: flex; flex-wrap: wrap; justify-content: center;">
  <div style="margin: 10px;">
    <a href="https://codesandbox.io/" target="_blank">
      <img src="https://img.shields.io/badge/CodeSandbox-entorno_de_desarrollo_en_la_nube-grey?style=for-the-badge&logo=CodeSandbox&logoColor=white&labelColor=151515" alt="CodeSandbox Logo">
    </a>
  </div>
  <div style="margin: 10px;">
    <a href="https://code.visualstudio.com/" target="_blank">
      <img src="https://img.shields.io/badge/Visual_Studio_Code-editor_de_código_avanzado_(IDE)-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=blue&labelColor=151515" alt="Visual Studio Code Logo">
    </a>
  </div>
</div>

<details>
  <summary>👀Mostrar configuración</summary>
 <ul>
    <h2>Descargar los editores de código</h2>
    <ul>
      <li><a href="https://codeSandbox.io/dashboard" target="_blank">Codesandbox</a></li>
      > En el caso de CodeSandbox no es necesario descargarlo ya que se utiliza como un simple espacio donde se almacena el proyecto que posteriormente se sube al  repostiorio de GitHub. Aunque igualmente existe un <a href="https://github.com/codesandbox/codesandbox-client" target="_blank">cliente de escritorio</a> para mayor comodidad.
      <li><a href="https://code.visualstudio.com/" target="_blank">VisualStudio</a></li>
    </ul>
    
    
   <ul>
   <h2>Descargar las extensiones (en caso de trabajar con VSCode)</h2>
     <li><a href="https://marketplace.visualstudio.com/items?itemName=CodeSandbox-io.codesandbox-projects" target="_blank">CodeSandbox support in VSCode</a></li>
     > Es necesario inciar sesión (GitHub).<br>
     > El espacio de CodeSandbox se importa automaticamente a la extensión si formas parte del mismo.<br>
     > Todos los editores del repositorio tienen acceso al espacio de trabajo de CodeSandbox.<br>
     <li><a href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" target="_blank">Python</a></li><sub>(Ya está instalado en el entorno de trabajo de CodeSandbox)</sub><br>
     > Es necesario para ejecutar codigo python (.py) en VSCode, además proporciona métodos que ayudan a la escritura y también se puede instalar en una instancia de CodeSanbox (sería necesario installar Docker para que funcione, para más info consultar el vídeo de <a href="https://www.youtube.com/watch?v=5T848HAHGfs" target="_blank">Devcontainers y Programación en la Nube</a>)
	   <ul>

>**Opcional** *<sub>(Estos cambios ya están aplicados al entorno de trabajo de CodeSandbox):</sub>*
De normal VSCode no actualiza el código en tiempo real, sino que solo lo actualiza cuando sales de la vista del código, para modificar su comportamiento debes ir a Configuración> Remoto> Files:Auto Save y cambiar el `onFocusChange` por el `afterDealy`
	![Captura13](https://user-images.githubusercontent.com/113378321/219981179-6f3af867-703f-4df3-bacf-3b7c3ae793d3.PNG)
	Tambien se puede cambiar el tiempo (ms) que tarda en actualizarlo con `files.autoSaveDelay`
	   ![Captura14](https://user-images.githubusercontent.com/113378321/219981364-fb8dbb6c-a28d-43a6-84b7-8393457b5a0a.PNG)
	<!--P.D: los cambios en el VSCode solo aparecen una vez que minimizas la aplicación o el que está en el CodeSanbox sale de la vista del código.(Esto no está muy claro tengo que seguir provando)-->
		   
  </ul>

</details>

<a href="https://www.youtube.com/watch?v=9IULfQH7E90">
  <img src="https://cdn.dribbble.com/users/7040/screenshots/8214019/media/9d162bf2d3303da6f3e777bbae322b33.gif" alt="Texto alternativo" width="500px">
</a>

*Proceso de configuración finalizado* <img src="https://user-images.githubusercontent.com/113378321/219910030-aac724a3-2159-4336-986c-d192fad7dbb1.gif" width="20px">

## **3. Flujo de trabajo**
1. Ejecutar el VSCode y utilizar la extensión de CodeSandbox, o en cuyo caso utlizar la web de CodeSandbox para acceder a la copia del repositorio.

<div style="display: flex;">
  <img src="https://user-images.githubusercontent.com/113378321/219816082-e9fd14fa-8b0f-44a1-b573-f0a6e81d7026.PNG" width="304px  alt="CodeSandbox">
  <img src="https://user-images.githubusercontent.com/113378321/219824618-8647d592-9b2b-40bb-997b-8f0cab849ace.PNG" width="702px alt="CodeSandbox2 ">
</div>


2. Elegir la Rama, <a href="https://www.youtube.com/watch?v=tFr0Vg1q9Eg&t=609s" target="_blank">Branch</a> para trabajar sobre ella. 
En principio para este pequeño proyecto el Equipo debería trabajar sobre la misma **Rama Secundaria (draft/1)** ya que CodeSandbox permite programar en paralelo *(si el Equipo fuese más grande, entonces sería necesario crear más ramas secundarías para realizar después una selección de cambios que pasarían a la **Rama principal**)*. 

![CodeSandbox4](https://user-images.githubusercontent.com/113378321/219825126-4b8687d6-4b7f-4f84-96ff-2fa14fc41351.PNG)
<div style="display: flex;">
  <img src="https://user-images.githubusercontent.com/113378321/219825291-2ff81899-e64b-41f1-a6f7-89b76e61456c.PNG" width="1100px alt="CodeSandbox2 ">
</div>

3. **Una vez terminado el programa actualizaremos el repositorio de GitHub:** subiremos/actualizaremos la Rama Secundaria sobre la que hemos estado trabjando en CodeSandbox a GitHub y una vez la tengamos subida a GitHub la mezclaremos con la Primaria.</u> 

![CodeSandbox7](https://user-images.githubusercontent.com/113378321/219825720-92edfb67-9a9e-4024-b844-b09f5c2fc473.PNG)
<div style="display: flex;">
  <img src="https://user-images.githubusercontent.com/113378321/219825717-9494a96b-645d-4d08-ab24-2b8484777063.PNG" width="1100px alt="CodeSandbox2 ">
</div>



>Para más info sobre los  diferentes métodos que proporcionan los repositorios GitHub consultar el vídeo <a href="https://www.youtube.com/watch?v=tFr0Vg1q9Eg&t" target="_blank">GIT / GITHUB ♥ Ramas o Branch, Uniones o Merge ♥</a>

## **4. Tareas**
- [x] Crear el repositorio
- [x] Configurar el editor de texto 
- [x] Divertirse 😁


## **5. Colaboradores**
<table>
<tr><td align="center"><a href="https://github.com/ggarciaengelmo"><img src="https://avatars.githubusercontent.com/u/125547323?v=4" width="100px;" alt="Nino"/><br /><sub><b>ggarciaengelmo</b></sub></a><br /> <a href="https://github.com/OscarYT9/Practica-1-Proyecto-de-videojuego/commits?author=ggarciaengelmo" title="Code">💻</a></td>
<td align="center"><a href="https://github.com/OscarYT9"><img 	src="https://avatars.githubusercontent.com/u/113378321?s=96&v=4" width="100px;" alt="Nino"/><br /><sub><b>OscarYT9</b></sub></a><br /> <a href="https://github.com/OscarYT9/Practica-1-Proyecto-de-videojuego/commits?author=OscarYT9" title="Code">💻</a></td></tr>
</table>

## **6. Patrocinadores** 

<a href="https://www.youtube.com/watch?v=xxIsmbVZuSI">
  <img src="https://api.products.aspose.app/slides/api/Common/DownloadFile/b0ecc963-11f6-4b46-a2ba-004b730c3861?file=result.gif" alt="Texto alternativo" width="500px">
</a>

[![IMAGE ALT TEXT HERE](https://w.wallha.com/ws/3/UIhkCsjd.jpg)](https://www.youtube.com/watch?v=gXzMD065HEk)
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/113378321/221442306-891c2632-81d9-4ca1-9ffc-6aa329b13b95.png)](https://www.youtube.com/watch?v=oATfORhqelk)
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/113378321/221443350-b860c641-6df2-449a-8b36-07c78e0505e4.jpg)](https://www.youtube.com/watch?v=2SVzBVsoY_Q)
[![IMAGE ALT TEXT HERE](https://is4-ssl.mzstatic.com/image/thumb/Music113/v4/2c/c7/d1/2cc7d1ae-21ad-8f52-6744-4f3503210702/cover.jpg/3000x3000bb.jpg)](https://www.youtube.com/watch?v=5_tjeX0B8UU&list=OLAK5uy_kFPsnC6pAdlxg1ahchvANmJHzVv2BmXik)
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/113378321/223850696-5bd205e5-bb2b-41ba-a44b-bdd92c75e0b1.jpg)](https://www.youtube.com/watch?v=F_-TPa8iS70)
[![IMAGE ALT TEXT HERE](https://images.squarespace-cdn.com/content/v1/52c9d908e4b0e87887310693/1555177699048-3WV3CHFJDSRPUPHPKN4F/SonniesEdge_LDR_09.jpg)](https://www.youtube.com/watch?v=hl_BEyYrguE)
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/113378321/222863458-f4585721-1bf2-4c0b-96b8-897f8ec36236.jpg)](https://www.youtube.com/watch?v=QzjZcMsGm3M&t=18s)
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/113378321/222863677-61c380cd-f2a6-4dd8-95dd-a3a9d06c8608.jpg)](https://www.youtube.com/watch?v=-dXRClwk-h0)
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/113378321/223845009-11c90628-7d08-42fa-9365-55ebcbf01039.png)](https://www.youtube.com/watch?v=qnACJZm_BYw)
[![IMAGE ALT TEXT HERE](https://cdna.artstation.com/p/assets/images/images/016/502/820/large/lee-j-p-.jpg?1552406319)](https://www.youtube.com/watch?v=fWTRBsNHzco)
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/113378321/227637813-e43af441-6f7d-4a01-8e6e-9f489560237e.jpg)](https://www.youtube.com/watch?v=crgpxKsal18)
[![IMAGE ALT TEXT HERE](https://user-images.githubusercontent.com/113378321/232178549-4f55e27a-c4a0-4083-b3fb-3f40809eb7a5.jpg)](https://www.youtube.com/watch?v=BVbm31ybqlU)


<a href="https://code.visualstudio.com/">
  <img align="right" alt="Juego | VSCode" width="21px" src="https://raw.githubusercontent.com/vscode-icons/vscode-icons/master/icons/file_type_vscode.svg" />
</a>

<a href="https://codesandbox.io/p/github/OscarYT9/Practica-1-Proyecto-de-videojuego/draft/1?workspaceId=a923da0c-be0a-4c5f-a6e5-15ed3514b8c6&file=%2FREADME.md&workspace=%257B%2522activeFileId%2522%253A%2522cle8er4sd0000g4jvesqp9pcq%2522%252C%2522openFiles%2522%253A%255B%2522%252FREADME.md%2522%255D%252C%2522sidebarPanel%2522%253A%2522EXPLORER%2522%252C%2522gitSidebarPanel%2522%253A%2522COMMIT%2522%252C%2522spaces%2522%253A%257B%2522cleauevoq001d336jzl1lezqf%2522%253A%257B%2522key%2522%253A%2522cleauevoq001d336jzl1lezqf%2522%252C%2522name%2522%253A%2522Default%2522%252C%2522devtools%2522%253A%255B%255D%257D%257D%252C%2522currentSpace%2522%253A%2522cleauevoq001d336jzl1lezqf%2522%252C%2522spacesOrder%2522%253A%255B%2522cleauevoq001d336jzl1lezqf%2522%255D%252C%2522hideCodeEditor%2522%253Afalse%257D">
  <img align="right" alt="Juego | CodeSandbox" width="20px" src="https://raw.githubusercontent.com/anuraghazra/anuraghazra/master/assets/codesandbox.svg" />
</a>

<img src="https://img.shields.io/badge/markdown-000000?style=for-the-badge&logo=markdown&logoColor=white" alt="markdown" style="vertical-align:top; margin:4px">

<p align="center">
        <img src="https://raw.githubusercontent.com/mayhemantt/mayhemantt/Update/svg/Bottom.svg" alt="Github Stats" />
</p>
	 
##  **7. Referencias** 
<a href="https://www.youtube.com/@Dimasmas/videos" target="_blank">@Dimasmas</a> [^1]

<a href="https://www.youtube.com/@FaztCode/videos" target="_blank">@FaztCode</a> [^2]

<a href="https://www.youtube.com/@EDteam/videos" target="_blank">@EDteam</a> [^3]

<a href="https://www.youtube.com/@AntonioSarosi/videos" target="_blank">@AntonioSarosi</a> [^4]

<a href="https://www.youtube.com/@bluuweb/videos" target="_blank">@bluuweb</a> [^5]

<a href="https://www.youtube.com/@CodeSandbox/videos" target="_blank">@CodeSandbox</a> [^6]

<a href="https://www.youtube.com/@BitBoss/videos" target="_blank">@BitBoss</a> [^7][^8]

<a href="https://www.youtube.com/@MrPSolver/videos" target="_blank">@MrPSolver</a> [^9]


[^1]: **<a href="https://www.youtube.com/watch?v=Ji8uoRvi17s" target="_blank"> # ❗PRINCIPIO de la Programación Orientada a Objetos: ABSTRACCIÓN - [EN PYTHON] - Curso PYTHON de cero</a>**

[^2]: **<a href="https://www.youtube.com/watch?v=pmVx7Ic3ITE" target="_blank"> # Github CodeSpaces, Visual Studio Code en la nube</a>**

[^3]: **<a href="https://www.youtube.com/watch?v=G2LphORsbLw" target="_blank"> # ¿Cómo programar desde la nube sin instalar editores de código?</a>**

[^4]: **<a href="https://www.youtube.com/watch?v=5T848HAHGfs" target="_blank"> # Devcontainers y Programación en la Nube. ¿Es el Futuro?</a>**

[^5]: **<a href="https://www.youtube.com/watch?v=tFr0Vg1q9Eg" target="_blank"> # GIT / GITHUB ♥ Ramas o Branch, Uniones o Merge ♥ [ Tutorial en Español - Parte 3]</a>**

[^6]: **<a href="https://www.youtube.com/watch?v=HfPIhxWacfs" target="_blank"># How to import a GitHub repository on CodeSandbox | CodeSandbox 101</a>**

[^7]: **<a href="https://www.youtube.com/watch?v=SI7O81GMG2A" target="_blank"># Programación Orientada a Objetos (POO): Abstracción, Encapsulamiento, Herencia, Polimorfismo</a>**

[^8]: **<a href="https://www.youtube.com/watch?v=JVNirg9qs4M" target="_blank"># CLASES en PYTHON, TODOS los pilares de POO aplicados a un EJEMPLO COMPLETO desde CERO</a>**

[^9]: **<a href="https://www.youtube.com/watch?v=0MhVkKHYUAY" target="_blank"># New Python Coders Be Like...</a>**
