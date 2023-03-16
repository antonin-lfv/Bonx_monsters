# WhitePaper

# Pages

## Home

- Url : /home
- Template : index.html
- Blueprint : general

Page d'accueil du site :
- Bouton pour accéder aux combats
- TODO : Ajouter des stats, ou des infos sur le jeu ?

## History

- Url : /match_history
- Template : match_history.html
- Blueprint : general

Page d'historique des combats :
- Liste des combats avec l'adversaire, le résultat, les récompenses
- TODO : Ajouter la date ?

## Monsters

- Url : /monsters
- Template : monsters.html
- Blueprint : general

Page qui regroupe tous les monstres du jeu : 
- Liste de tous les monstres avec leur rareté, leur nom, l'image
- TODO : Ajouter un filtre par rareté ?

## Battle

- Url : /battle
- Template : battle.html
- Blueprint : general

Page de combat :
- TODO : Créer le système de combat

## Profil

- Url : /profil
- Template : profil.html
- Blueprint : general

Page de profil du joueur :
- Informations sur le joueur (nom, niveau, pièces, nombre de monstres, nombre de combats, nombre de victoires)
- Liste des monstres du joueur avec leur niveau, leur rareté, leur nom, l'image et le nombre de cartes en hover
- TODO : Ajouter un filtre par rareté ? Ajouter un filtre par niveau ? 
Ajouter un filtre par attaque ? Ajouter un filtre par défense ?



# Logique de jeux
- A chaque victoire, le joueur perçoit une récompense en coins
- Le niveau du joueur correspond à la puissance divisée par 1000
- La puissance du joueur est calculé par la somme de la puissance de chacun de ses monstres
- Chaque monstre à une puissance, qui augmente avec son niveau etc

# TODO 
Créer les monstres à battre (sinon toujours les monstres de bases)