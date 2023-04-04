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

Page de choix d'un combat :
- Choix entre 3 bosses ou 8 donjons

## Profil

- Url : /profil
- Template : profil.html
- Blueprint : general

Page de profil du joueur :
- Informations sur le joueur (nom, niveau, pièces, nombre de monstres, nombre de combats, nombre de victoires)
- Liste des monstres du joueur avec leur niveau, leur rareté, leur nom, l'image et le nombre de cartes en hover
- Possibilité de filtrer les monstres par rareté

## Shop

- Url : /shop
- Template : shop.html
- Blueprint : general

Page de la boutique :
- Liste de 6 monstres aléatoires qui peuvent être achetés avec des pièces.
- On peut acheter un monstre en cliquant sur son image avec un maximum de 1 monstre légendaire, 2 monstres épiques, 
3 monstres rares et 5 monstres communs.
- Est affiché le nombre de pièces restantes dynamiquement

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
Le joueur doit créer un compte pour pouvoir jouer. Il commence avec 6 monstres aléatoires (niveau 1).
Pour progresser il doit combattre des monstres.

À chaque victoire : 
- Le joueur perçoit une récompense en pièces
- Le joueur gagne un monstre aléatoire (commun, rare, épique, légendaire)

Le joueur :
- Peut acheter des cartes de monstres avec ses pièces (à implémenter)
- Le niveau du joueur correspond à la puissance divisée par 2000
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
    - Défense : 70 (level 1)
    - Attaque : 40 (level 1)
    - Puissance : 100 (level 1) (puissance = niveau * puissance au level 1)
    - Nombre de cartes pour améliorer : 10
- Rare :
    - Défense : 90 (level 1)
    - Attaque : 50 (level 1)
    - Puissance : 200 (level 1) (puissance = niveau * puissance au level 1)
    - Nombre de cartes pour améliorer : 20
- Épique :
    - Défense : 110 (level 1)
    - Attaque : 60 (level 1)
    - Puissance : 300 (level 1) (puissance = niveau * puissance au level 1)
    - Nombre de cartes pour améliorer : 30
- Légendaire :
    - Défense : 150 (level 1)
    - Attaque : 80 (level 1)
    - Puissance : 500 (level 1) (puissance = niveau * puissance au level 1)
    - Nombre de cartes pour améliorer : 40


# Combats
Il y a 2 types de combats :
- Combat dans un donjon, qui consiste à combattre une horde de monstres
- Combat contre un boss, qui consiste à combattre un monstre de niveau très élevé. Le but est de le battre en un seul combat

## Donjon
Le donjon est composé de 6 monstres
Il existe 8 donjons différents, et le joueur peut choisir le donjon dans lequel il veut combattre.
Il se bat avec 6 monstres de son choix.

## Boss
Le boss est un monstre de niveau très élevé. Le joueur doit le battre en un seul combat.
Il existe 3 boss différents, et le joueur peut choisir le boss qu'il veut combattre.
Le joueur peut quitter le combat contre le boss à tout moment. Il se bat avec 6 monstres de son choix.
Chaque monstre du joueur inflige des dégâts au boss, et le boss inflige des dégâts à un monstre aléatoire du joueur encore vivant.

## Récompenses
À chaque combat gagné, le joueur reçoit une récompense en pièces. Le montant de la récompense est calculé en fonction du niveau du monstre battu.
De plus il a une chance de gagner un monstre aléatoire (commun, rare, épique, légendaire).


# TODO
- [ ] Ajouter des stats, ou des infos sur le jeu sur la page Home
- [X] Ajouter un filtre par rareté dans la liste des monstres du jeu
- [X] Ajouter un filtre par rareté dans la liste des monstres du joueur
- [ ] Créer le système de donjons
- [X] Créer le système de boss
- [X] Créer récompenses aléatoires après chaque combat (monstre)
- [X] Créer un shop pour acheter des cartes de monstres avec des pièces (à implémenter)
- [X] Ajouter des messages lors du login, de l'inscription etc
- [ ] Ajouter des cartes gratuites dans le shop
- [X] Animation après victoire pour afficher les cartes gagnées
- [ ] Ajouter les cartes gagnées dans l'historique des combats
- [X] Navbar responsive


# Liens
- Assets boss : 
  - https://free-game-assets.itch.io/free-2d-orcs-sprite-sheets
  - https://engvee.itch.io/free-animated-isometric-hellbeast

- Assets level up :
  - https://uiverse.io/challenges/level-up-challenge
