# Mes Projets Cybersécurité (Python)
Bienvenue sur mon portfolio de sécurité ! Ce dépôt regroupe les outils que je développe pour mettre en pratique mes connaissances en cybersécurité après l'obtention de ma certification Coursera.

## Projet 1 : Générateur de Mots de Passe Cryptographique
Ce script est un outil simple mais puissant conçu pour générer des mots de passe hautement sécurisés, résistants aux attaques par force brute.

### Pourquoi ce projet est "Cyber-Safe" ?
Contrairement aux générateurs classiques qui utilisent le module random (prévisible), ce projet utilise le module secrets de Python.

CSPRNG (Cryptographically Secure Pseudo-Random Number Generator) : Le module secrets est spécifiquement conçu pour la cryptographie, rendant le hasard généré impossible à prédire pour un attaquant.

### Fonctionnalités :
Complexité totale : Inclut des lettres (majuscules/minuscules), des chiffres et des caractères spéciaux.

Entrée utilisateur : L'utilisateur définit lui-même la longueur souhaitée pour le mot de passe.

Flexibilité : Peut générer aussi bien des codes PIN courts que des clés de sécurité très longues.

### Comment l'exécuter :
python generateur.py

Projet réalisé par Nancy - 2026
