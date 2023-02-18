# **Practica-1-Proyecto-de-videojuego**
## >1. Introducción
### 1.1 Programación orientada a objetos
>Una compañía de videojuegos quiere comprobar el equilibrio entre los personajes de su próximo juego 
de lucha. Nos envía documentación relativa al conjunto P de N personajes del juego (PJs) y a la lógica 
del combate para que programemos distintas simulaciones y evaluemos si siempre resulta ganador 
un PJ de la misma clase. La documentación incluye varios ficheros de prueba con personajes ya 
definidos (prueba1.txt, prueba2.txt, prueba3.txt) y un main.py con código para abrir y leer los ficheros. [p1.pdf](https://github.com/OscarYT9/Practica-1-Proyecto-de-videojuego/files/10770799/p1.pdf)

### 1.2 Programación orientada a objetos

```mermaid
%%{init: {'theme': 'dark',
'lineColor': '#F8B229'}}%%
classDiagram
  Avatar <|-- Melee
  Avatar <|-- Caster
  Melee <|-- Warrior
  Caster <|-- Mage

  class Avatar{
    +String name
    +int level
    +equip()
    +attack()
  }
  
  class Melee{
    +int strength
    +int defense
    +useWeapon()
  }
  
  class Caster{
    +int intelligence
    +int mana
    +castSpell()
  }
  
  class Warrior{
    -String weaponType
    -rage()
  }
  
  class Mage{
    -String element
    -summon()
}

```
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


## >**2. Programas usados**
<div style="max-width: 600px; display: flex; flex-wrap: wrap; justify-content: center;">
  <div style="margin: 10px;">
    <a href="https://codesandbox.io/" target="_blank">
      <img src="https://img.shields.io/badge/CodeSandbox-entorno_de_desarrollo_utlizado-grey?style=for-the-badge&logo=CodeSandbox&logoColor=white&labelColor=151515" alt="CodeSandbox Logo">
    </a>
  </div>
  <div style="margin: 10px;">
    <a href="https://code.visualstudio.com/" target="_blank">
      <img src="https://img.shields.io/badge/Visual_Studio_Code-entorno_de_desarrollo_utlizado-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=blue&labelColor=151515" alt="Visual Studio Code Logo">
    </a>
  </div>
</div>

<details>
  <summary>👀Mostrar configuración</summary>
 <ul>
    <h2>Descargar los editores de código</h2>
    <ul>
      <li><a href="https://codeSandbox.io/dashboard" target="_blank">Codesandbox</a></li>
      > En el caso de CodeSandbox no es necesario descargarlo ya que se utiliza como un simple espacio donde se almacena el proyecto que posteriormente se sube al  repostiorio de GitHub.
      <li><a href="https://code.visualstudio.com/" target="_blank">VisualStudio</a></li>
    </ul>
    
    
   <ul>
   <h2>Descargar las extensiones (en caso de trabajar con VSCode)</h2>
     <li><a href="https://marketplace.visualstudio.com/items?itemName=CodeSandbox-io.codesandbox-projects" target="_blank">CodeSandbox support in VSCode</a></li>
     > Es necesario inciar sesión (GitHub).<br>
     > El espacio de CodeSandbox se importa automaticamente a la extensión si formas parte del mismo.<br>
     > Todos los editores del repositorio tienen acceso al espacio de trabajo de CodeSandbox.<br>
     <li><a href="https://marketplace.visualstudio.com/items?itemName=ms-python.python" target="_blank">Python</a></li>
     > Es necesario para ejecutar codigo python (.py) en VSCode, además proporciona métodos que ayudan a la escritura y también se puede instalar en una instancia de CodeSanbox (sería necesario installar Docker para que funcione, para más info consultar el vídeo de <a href="https://www.youtube.com/watch?v=5T848HAHGfs" target="_blank">Devcontainers y Programación en la Nube</a>
  </ul>

</details>

<a href="https://www.youtube.com/watch?v=9IULfQH7E90">
  <img src="https://cdn.dribbble.com/users/7040/screenshots/8214019/media/9d162bf2d3303da6f3e777bbae322b33.gif" alt="Texto alternativo" width="500px">
</a>

*Proceso de configuración finalizado* <img src="https://media.tenor.com/M5dR7qb1f1sAAAAC/loading-thinking.gif" alt="Texto alternativo" width="40px">

## >**3. Flujo de trabajo**
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

## >**4. Tareas**

- [x] Crear el repositorio
- [x] Configurar el editor de texto 
- [x] Divertirse 😁

## >**5. Patrocinadores** 

<a href="https://www.youtube.com/watch?v=9IULfQH7E90">
  <img src="https://api.products.aspose.app/slides/api/Common/DownloadFile/b0ecc963-11f6-4b46-a2ba-004b730c3861?file=result.gif" alt="Texto alternativo" width="500px">
</a>

[![IMAGE ALT TEXT HERE](https://w.wallha.com/ws/3/UIhkCsjd.jpg)](https://www.youtube.com/watch?v=gXzMD065HEk)
