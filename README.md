# WhitePaper

# Pages

## Home

- Url : /home
- Template : index.html
- Blueprint : general

Page d'accueil du site :
- Bouton pour accéder aux combats

## History

- Url : /match_history
- Template : match_history.html
- Blueprint : general

Page d'historique des combats :
- Liste des combats avec l'adversaire, le résultat, les récompenses

## Monsters

- Url : /monsters
- Template : monsters.html
- Blueprint : general

Page qui regroupe tous les monstres du jeu : 
- Liste de tous les monstres avec leur rareté, leur nom, l'image

## Battle

- Url : /battle
- Template : battle.html
- Blueprint : general

Page de combat :

## Profil

- Url : /profil
- Template : profil.html
- Blueprint : general

Page de profil du joueur :
- Informations sur le joueur (nom, niveau, pièces, nombre de monstres, nombre de combats, nombre de victoires)
- Liste des monstres du joueur avec leur niveau, leur rareté, leur nom, l'image et le nombre de cartes en hover
- TODO : Ajouter un filtre par rareté ? Ajouter un filtre par niveau ? 
Ajouter un filtre par attaque ? Ajouter un filtre par défense ?


## About us

- Url : /about
- Template : about.html
- Blueprint : general

Page des crédits :
- TODO : remplir la page

## Login

- Url : /login
- Template : login.html
- Blueprint : auth

Page de connexion :
- Formulaire de connexion

## Register

- Url : /signup
- Template : registration.html
- Blueprint : auth

Page d'inscription :
- Formulaire d'inscription


# Progression dans le jeu
Le joueur doit créer un compte pour pouvoir jouer. Il commence avec un monstre aléatoire commun (niveau 1).
Pour progresser il doit combattre des monstres.

À chaque victoire : 
- Le joueur perçoit une récompense en pièces (le montant est à déterminer)
- Le joueur gagne un monstre aléatoire (commun, rare, épique, légendaire) (le niveau est à déterminer)

Le joueur :
- Peut acheter des monstres avec ses pièces (à implémenter)
- Le niveau du joueur correspond à la puissance divisée par 3000
- La puissance du joueur est calculée par la somme de la puissance de chacun de ses monstres
- A un nombre de pièces, de victoires et de combats

Les monstres :
- Peuvent être de 4 raretés : commun, rare, épique, légendaire
- Chaque monstre à une puissance, qui augmente avec son niveau
- Chaque monstre à une attaque, qui augmente avec son niveau
- Chaque monstre à une défense, qui augmente avec son niveau
- Chaque monstre à une image, une description
- Chaque monstre à un niveau, qui augmente avec le nombre de cartes (par palier)

Configuration du jeu :
- Max de pièces : 1000000 (GameConfig.MAX_COINS)
- Max de niveau des monstres : 200 (GameConfig.MAX_MONSTER_LEVEL)

Statistiques des monstres :
- Commun :
    - Défense : 30 (level 1)
    - Attaque : 40 (level 1)
    - Puissance : 500 (level 1) (puissance = niveau * puissance)
    - Nombre de cartes pour améliorer : 10
    - Ratio de cartes à améliorer : 1.2 (Pour multiplier la défense et l'attaque)
- Rare :
    - Défense : 40 (level 1)
    - Attaque : 50 (level 1)
    - Puissance : 1000 (level 1) (puissance = niveau * puissance)
    - Nombre de cartes pour améliorer : 20
    - Ratio de cartes à améliorer : 1.25 (Pour multiplier la défense et l'attaque)
- Épique :
    - Défense : 50 (level 1)
    - Attaque : 60 (level 1)
    - Puissance : 2000 (level 1) (puissance = niveau * puissance)
    - Nombre de cartes pour améliorer : 30
    - Ratio de cartes à améliorer : 1.3 (Pour multiplier la défense et l'attaque)
- Légendaire :
    - Défense : 60 (level 1)
    - Attaque : 70 (level 1)
    - Puissance : 3000 (level 1) (puissance = niveau * puissance)
    - Nombre de cartes pour améliorer : 40
    - Ratio de cartes à améliorer : 1.15 (Pour multiplier la défense et l'attaque)


# Combats
Il y a 2 types de combats :
- Combat dans un donjon, qui consiste à combattre une série de monstres de niveaux de plus en plus élevés
- Combat contre un boss, qui consiste à combattre un monstre de niveau très élevé. Le but est de le battre en un seul combat.

## Donjon
Le donjon est composé de 10 niveaux. Le joueur doit battre tous les monstres de chaque niveau pour passer au niveau suivant.
Le joueur commence au niveau 1, et doit battre tous les monstres du niveau 1 pour passer au niveau 2, etc.
Il existe 50 donjons différents, et le joueur peut choisir le donjon dans lequel il veut combattre.
Le joueur peut quitter le donjon à tout moment. Il se bat avec 3 monstres de son choix.

## Boss
Le boss est un monstre de niveau très élevé. Le joueur doit le battre en un seul combat.
Il existe 3 boss différents, et le joueur peut choisir le boss qu'il veut combattre.
Le joueur peut quitter le combat contre le boss à tout moment. Il se bat avec 3 monstres de son choix.

## Récompenses
À chaque combat, le joueur reçoit une récompense en pièces. Le montant de la récompense est calculé en fonction du niveau du monstre battu.
De plus il a une chance de gagner un monstre aléatoire (commun, rare, épique, légendaire).

## Combat
Le combat se déroule ainsi :
- Des phases d'attaque : Le joueur attaque le monstre
- Des phases de défense : Le monstre attaque le joueur
C'est un combat tour par tour, et le joueur peut choisir d'attaquer ou de se défendre à chaque tour.
- Si le joueur attaque, il inflige des dégâts au monstre
- Si le joueur se défend, il réduit les dégâts qu'il prend du monstre


# TODO
- Ajouter des stats, ou des infos sur le jeu sur la page Home
- Ajouter la date sur l'historique des combats
- jouter un filtre par rareté dans la liste des monstres du jeu, ajouter une mention "owned" sur les monstres possédés
- Créer le système de donjons et de boss, et le système de combat
- Créer ouvertures de coffres


# Liens
- Assets boss : 
  - https://free-game-assets.itch.io/free-2d-orcs-sprite-sheets
  - https://engvee.itch.io/free-animated-isometric-hellbeast
