# Technical specification

<details> 
<summary> 📖 Table of contents:</summary>

- [Technical specification](#technical-specification)
  - [1.Project Overview](#1project-overview)
  - [2.Development of the Solution](#2development-of-the-solution)
    - [2\_1.Solution](#2_1solution)
    - [2\_2.Technical constraints](#2_2technical-constraints)
      - [The tanks](#the-tanks)
      - [The Complexity](#the-complexity)
      - [The language choose](#the-language-choose)
    - [2\_3.Development : How is it work ?](#2_3development--how-is-it-work-)
      - [Value in functions](#value-in-functions)
    - [2\_4.Cost estimation](#2_4cost-estimation)
  - [3.Risks](#3risks)
    - [3\_1.Accessibility](#3_1accessibility)
    - [3\_2.Success evaluation](#3_2success-evaluation)
  - [4.More about the client :](#4more-about-the-client-)
  - [Glossary](#glossary)

</details>

## 1.Project Overview


> <br> The objective of [**Krug Champagne**](#4more-about-the-client-) project is to minimize the loss of champagne during the blending (4th step of the champagne making process) proposed by the algorithm. 
And to implement a program that blends several wines to achieve a blend as close as possible to the given formula with the least complexity for the program.
<br>

## 2.Development of the Solution

### 2_1.Solution
<!--à revoir -->
> <br>We choose **_python_** like language to create the data base of the company and help at the organisazion.
> The tanks cannot be half full. They must be either empty or completely full.
<br>
<!--they would a total of 400 wines, each embodying the individuality of a specific parcel.-->

### 2_2.Technical constraints
#### The tanks
 The tanks cannot be half full. They must be either empty or completely full. This constraint must be taken into account with great importance, as oxidation of the wine must be avoided.
<br>

#### The Complexity
The most important thing to consider throughout the project is to have O(1), O(logn), O(n). 
The values to be avoided absolutely for the efficiency of the program, are O(nlogn), O(n^2), O(2^n), O(n!).
<br>

#### The language choose 
<!--3.14 de vitesse d'execution 11 ème plus rapide -->

|Language |Time | Energy | High level language ou Low level language | interpreted[^3] or compiled[^2]|
|:-----: |:----:|:----:|:----:|:----:|
| C |1.00| 1.00 | high | compiled |
| Rust |1.04| 1.03| high | compiled |
| C++ | 1.56 | 1.34 | high | compiled |
| ... | ... | ... | ... | ... |
| GO  | 2.83 | 3.23 | high | compiled |
| ... | ... | ... | ... | ... |
| C# | 3.14 | 3.14| high | compiled |
| ... | ... | ... | ... | ... |
| F# | 6.30 | 4.13| high | interpreted |
| Javascript | 6.52 | 4.45| high | interpreted |
| ... | ... | ... | ... | ... |
| PHP | 27.64 | 29.30| high | interpreted |
| ... | ... | ... | ... | ... |
| Python | 71.90 | 75.88| high | interpreted |




### 2_3.Development : How is it work ?
<img src="/docs/technical1.png">
<!--à continuer -->
> The formula was given by the Cellar master[^1].

#### Value in functions 

| Where and Class | value | for ? | type |
|:---:|:---:|:---:|:---:|:---:|
| tank.py in Tank : | name | name of the tank.| (str) |
|     | max | Level max of the tank.| (float) |
|     | nodes | The nodes of the tank. | (List) |
|     | liquids | The liquids in the tank.| (float) |
| liquid.py in Liquid :| name | name of where are the liquid (the tank name).| (str) |
|     | level |  Level of Liquids on the tank. | (float/ decimal) |
| analyzer.py in DefaultParser : | formula | formula give by the Cellar master | (str)|


### 2_4.Cost estimation

To make the project, we don't need to buy anything. We will use the tools that we already have.

## 3.Risks

[Risk doc](https://docs.google.com/spreadsheets/d/1c3TqdskpdIjxDfMc5kR791dv1CRFdnPDg-OVfnnxMEE/edit?usp=sharing)


- [x] champagne production slowed down
- [x] bad mixing so loss of wine
- [x] problem with the "site" so delay
- [x] some unit test not passing
- [x] some test don't work 
<!--a ajouté -->

### 3_1.Accessibility

> <br> They have access to a Local interface.<!--a ajouté et chnager si il faut --> With two places where you can enter values, one for the mixture and another for the formula. One place to see the chages in the differents tanks. 
<br>

### 3_2.Success evaluation

> The final goal of our project would be to render at least: a code that returns data (the most likely mixes: percentage of tank this number -> in tank that number).
<!-- renvoie des données (les mixes les plus probables : pourcentage de tankn -> dans tankn2 -->

## 4.More about the client :

The client is the House **Krug Champagne**[*](https://www.krug.com/fr/la-maison-krug), conceptor of champagne since 1843. Based in Reims.

Krug has several labels that testify to the quality of its champagnes. One of the most prestigious labels that Krug has is "_Champagne de Prestige_", which designates the most upmarket and exceptional champagnes.

It also offers Grande Cuvée champagne (_171st edition_), each with a _unique history_ and individuality of a _specific parcel_.

- [Their Website](https://www.krug.com/fr/la-maison-krug)

## Glossary 

[^1]: **Cellar master** : it is the person who makes the wine or the champagne.<br>

[^2]: **compiled** : Compiled languages are converted directly into machine code that the processor can execute. As a result, they tend to be faster and more efficient to execute than interpreted languages. They also give the developer more control over hardware aspects, like memory management and CPU usage.<br>
Compiled languages need a “build” step, they need to be manually compiled first. You need to “rebuild” the program every time you need to make a change. In our hummus example, the entire translation is written before it gets to you. If the original author decides that he wants to use a different kind of olive oil, the entire recipe would need to be translated again and resent to you.<br>

[^3]: **interpreted** : Interpreters run through a program line by line and execute each command. Here, if the author decides he wants to use a different kind of olive oil, he could scratch the old one out and add the new one. Your translator friend can then convey that change to you as it happens.<br>
Interpreted languages were once significantly slower than compiled languages. But, with the development of just-in-time compilation, that gap is shrinking.<br>