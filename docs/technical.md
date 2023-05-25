# Technical specification

<details> 
<summary> 📖 Table of contents:</summary>

- [Technical specification](#technical-specification)
  - [1.Project Overview](#1project-overview)
  - [2.Development of the Solution](#2development-of-the-solution)
    - [2\_1.Solution](#2_1solution)
    - [2\_2.The Complexity](#2_2the-complexity)
    - [2\_3.Development : How is it work ?](#2_3development--how-is-it-work-)
    - [2\_4.Cost estimation](#2_4cost-estimation)
  - [3.Risks](#3risks)
    - [3\_1.Accessibility](#3_1accessibility)
    - [3\_2.Success evaluation](#3_2success-evaluation)
  - [4.More about the client :](#4more-about-the-client-)
  - [Glossary](#glossary)

</details>

## 1.Project Overview

The objective of [Krug Champagne](#4more-about-the-client-) project is to minimize the loss of champagne during the blending (4th step of the champagne making process) proposed by the algorithm. 
And to implement a program that blends several wines to achieve a blend as close as possible to the given formula with the least complexity for the program.

## 2.Development of the Solution

### 2_1.Solution
<!--à revoir -->
We choose [<!--language surement C#-->] like language to create the data base of the company and help at the organisazion.

The tanks cannot be half full. They must be either empty or completely full.
<!--they would a total of 400 wines, each embodying the individuality of a specific parcel.-->
### 2_2.The Complexity

### 2_3.Development : How is it work ?
<img src="/docs/technical1.png">
<!--à continuer -->
The formula was given by the Cellar master[^1].

### 2_4.Cost estimation

To make the project, we don't need to buy anything. We will use the tools that we already have.

## 3.Risks

[Risk doc](https://docs.google.com/spreadsheets/d/1c3TqdskpdIjxDfMc5kR791dv1CRFdnPDg-OVfnnxMEE/edit?usp=sharing)


- champagne production slowed down
- bad mixing so loss of wine
- problem with the "site" so delay
- some unit test not passing
- some test don't work 
<!--a ajouté -->

### 3_1.Accessibility

They have access to a Local interface.<!--a ajouté : With two places where you can enter values, one for the mixture and another for the formula. One place to see the chages in the differents tanks.-->

### 3_2.Success evaluation

<!-- renvoie des données (les mixes les plus probables : pourcentage de tankn -> dans tankn2 -->

## 4.More about the client :

The client is the House Krug Champagne, conceptor of champagne since 1843. Based in Reims.

Krug has several labels that testify to the quality of its champagnes. One of the most prestigious labels that Krug has is "Champagne de Prestige", which designates the most upmarket and exceptional champagnes.

It also offers Grande Cuvée champagne (171st edition), each with a unique history and individuality of a specific parcel.


- [Their Website](https://www.krug.com/fr/la-maison-krug)

## Glossary 

[^1]:Cellar master : it is the person who makes the wine or the champagne.
