# WATER

## Présentation

Water est une application de suivi de consommation d'eau.

A chaque clic, cela signifie qu'un verre d'eau a été consommé.
Les informations sont sauvegardées dans un fichier au format JSON.
Il est possible de fournir un récapitulatif par jour de la consommation d'eau.
A la mi journée, il faut une alerte si le seuil minimal n'est pas atteint à 50%.

## Compilation

### Local

Pour préparer l'environnement, vous devez créer un environnement virtuel et l'activer

```bash
python -m venv waterenv
source ./waterenv/bin/activate
```

Pour lancer les tests et l'analyse de couverture de code au format XML, utilisez le script build.sh.

```bash
./build.sh
```

### Environnement Docker

Pour lancer les tests et l'analyse de couverture de code au format XML, sans avoir besoin de créer un environnement virtuel directement, reprenez la commande ci-après en remplaçant le chemin HOME_PROJECT/project-tofix par le chemin absolu vers le projet.

```bash
docker run --rm \
    -v HOME_PROJECT/project-tofix:/usr/src \
    -w /usr/src \
    python:3.11 ./build.sh
```


Envoyer l'analyse de code à une instance SonarQube en local.

```bash
#FIXME
```

## Utilisation

Pour utiliser et tester en situation nominale le service, utilisez les commandes suivantes.

```bash
python -m venv .venv
. ./.venv/bin/activate
pip install -f requirements.txt
python app.py
```

Si l'application ne démarre pas correctement, ajouter le fichier json à la racine de votre application.

```json
{"water": 0}
```

## Evolution alerte

Plutôt que chaque client vérifie si une alerte doit être déclenchée à la mi-journée, faites-en sorte d'enregistrer la liste des clients à contacter en cas de trop faible quantité d'eau consommée.

La notification d'un client sera seulement une simulation vous devez donc afficher le message suivant dans un fichier de log appelé `notification.log`.

```
Alerte, manque d'eau pour le profile XXXX
```


## POO

Refactoriser l'application pour regrouper les différentes parties/fonctionnalités au sein de classes afin de ne plus avoir de simples fonctions appelées directement les points d'accès.


## Résumé des modifications

1. Tester l'application pour faire fonctionner les éléments de base
2. Absorber la dette technique en sélectionnant les actions rapides
3. Refactoriser le code en suivant les principes de la POO