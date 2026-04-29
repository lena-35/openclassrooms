# 📓 Notes : Rédigez les spécifications techniques d'une application

> **Cours :** [Lien OpenClassrooms](https://openclassrooms.com/fr/courses/8783756-redigez-les-specifications-techniques-d-une-application)

> **Début du cours :** 10/04/2026

> **Fin du cours :** 27/04/2026

---

## 🧭 Partie 1 : Transformer un besoin en spécifications techniques exploitables
*Notes sur l'importance de transformer un besoin en spécifications techniques exploitables pour la gestion de projet :*
- *Transformer un besoin métier encore flou en spécifications techniques claires et exploitables.*
- *Découvrir comment analyser un projet, comprendre les attentes du client et formuler des User Stories et critères d’acceptation précis.*
- *Apprendre à structurer un document de spécifications complet : architecture, modules, flux de données et contraintes techniques.*
- *Traduire chaque exigence en solutions techniques concrètes, illustrées par des schémas et du pseudocode.*
- *Faire vivre les spécifications dans un cadre Agile, afin qu’elles restent toujours cohérentes, utiles et alignées avec l’évolution du projet.*


	![Modèle de developpement projet](images/Fiche_resume_cours.png)

---

### 1.1 Comprendre le besoin fonctionnel (le QUOI)
**Mission** : développer une **application de gestion de tâches** pour les équipes techniques.

**Risques** : Si l'équipe commence à coder avant d'avoir parfaitement clarifié ce que le client attend, risques des malentendus coûteux, des retards, et pire, la construction d’un outil que personne n'utilisera.
- Transformer l'idée initiale d’application de gestion de tâches en un ensemble d'exigences claires et non ambiguës.
- Passer du besoin métier flou à des critères d'acceptation précis, un élément fondamental pour tout projet réussi.

#### 1.1.1 Identifier le besoin métier :
Adopter le rôle d'enquêteur pour comprendre le "**pourquoi**" du projet:
- **Analyser le contexte du projet** en définissant clairement trois axes essentiels :
	<br>1- Les objectifs (que veut-on atteindre ?),
	<br>2- Les contraintes (temps, budget, technologies existantes),
	<br>3- Et les utilisateurs cibles.
- **Identifier les besoins exprimés et implicites** :
	- Les besoins exprimés sont ceux que le client vous a clairement demandés (« Nous voulons pouvoir assigner des tâches »).
	- Les besoins implicites sont ceux que le client n'a pas formulés, mais qui sont nécessaires au bon fonctionnement de l'application (« Si je crée une tâche, je dois pouvoir la modifier ou la supprimer »).
	> Souvent, les besoins implicites sont découverts en se posant des questions sur le flux de travail réel de l'utilisateur.
- **Recueillir les informations concrètes** en utilisant des **outils de recueil** :
![Modèle de developpement projet](images/Comprehension_du_besoin.png)	
	- Les **entretiens individuels ou collectifs** avec les équipes techniques permettent de saisir leurs frustrations actuelles et leurs attentes précises.
- Les **questionnaires** peuvent être utiles pour valider des hypothèses à grande échelle.
- L'utilisation de **User Stories** (Histoires Utilisateur) est une approche particulièrement efficace dans la démarche Agile. Une User Story capture un besoin du point de vue de l'utilisateur final et constitue une excellente base pour la formalisation des exigences.
> Dans la méthodologie Agile, très courante dans le développement logiciel moderne, une User Story est une description simple et concise d'une fonctionnalité vue par l'utilisateur. Elle suit souvent le format : « En tant que [rôle], je veux [objectif], afin de [bénéfice] ». Cela permet de garder l'accent sur la valeur ajoutée pour l'utilisateur, ici les équipes techniques de la start-up.
- En adoptant une approche opérationnelle et pragmatique, on s'assurez de ne pas simplifier à l'extrême, mais plutôt de faciliter la compréhension des besoins réels des équipes techniques.

#### 1.1.2 Formaliser les exigences fonctionnelles et non fonctionnelles :
Une fois les besoins bruts identifiés, il est impératif de les transformer en exigences formelles:
> C'est le passage d'une idée (« Nous voulons mieux gérer nos tâches ») à une spécification détaillée (« La fonction d'assignation de tâche doit permettre de sélectionner un utilisateur dans une liste prédéfinie »).
- **Rédiger des cas d'utilisation clairs et complets** en rédigeant des User Stories détaillées ainsi que leurs conditions d'exécution :
	- Chaque exigence doit être formulée avec un **vocabulaire précis et non ambigu**.
	- Il faut éviter les termes subjectifs comme « rapide », « facile » ou « intuitif » qui pourraient être interprétés différemment par le client, le Product Owner (PO) et les développeurs.
	> Le **Product Owner** est responsable de traduire les besoins métiers en spécifications techniques claires et exploitables pour l’équipe de développement. Il s’assure que les fonctionnalités décrites répondent aux objectifs produits et aux contraintes techniques. Son rôle est d’assurer la cohérence, la priorisation et la compréhension des exigences tout au long du cycle de développement.
- **Distinguer clairement les exigences fonctionnelles et non fonctionnelles** :
	- **Les exigences fonctionnelles** décrivent ce que le système doit faire. Pour l'application de la start-up, une exigence fonctionnelle serait : « L'application doit permettre la création, la modification et la suppression de tâches » (le "quoi").
	- **Les exigences non fonctionnelles** décrivent comment le système doit fonctionner ou les contraintes qui pèsent sur lui. Elles peuvent concerner la performance, la sécurité, l'ergonomie, ou la maintenabilité (le "comment bien").
- Exemple: 
	- Le client exige que l'application de gestion de tâches soit « rapide ». Cette exigence est floue. Le travail consiste à la décomposer. Si elle est rapide, cela pourrait signifier : « Le temps de chargement de la liste des tâches ne doit jamais excéder 2 secondes, même avec 100 tâches actives. » Le premier est un souhait, le second est une exigence non fonctionnelle mesurable.
	> Éviter absolument de formuler une exigence fonctionnelle comme ceci : « L'utilisateur pourra gérer ses tâches. » Cette phrase est trop vague. Une formulation précise serait : « En tant qu’utilisateur, je peux consulter la liste de toutes mes tâches en cours, triées par date d'échéance. » La clarté est votre meilleure alliée pour éviter les malentendus coûteux.
	- Adopter cette rigueur dans la formalisation garantit que les équipes techniques de la start-up comprennent exactement la portée du travail à réaliser et pourront livrer un produit qui répond réellement aux attentes métier.

#### 1.1.3 Définir les critères dʼacceptation :
- Avec des **exigences claires** interviennent les **critères d’acceptation**, qui servent de jalon de validation.
> Comment savoir si ces exigences ont été correctement implémentées par les équipes techniques ?
- Etablir des critères mesurables pour valider chaque exigence. Ces critères sont essentiels pour que le client (ou le PO) puisse dire « oui, la fonctionnalité est terminée et elle fonctionne comme attendu ». Si une exigence fonctionnelle stipule que l'on peut assigner une tâche, le critère d'acceptation pourrait être : « L'utilisateur reçoit une notification par email lorsque la tâche lui est assignée. »
> Dans le monde Agile, le **formalisme Gherkin** est très répandu pour rédiger ces critères. Il s'agit d'une syntaxe simple utilisant les mots-clés "Étant donné", "Quand", et "Alors" pour décrire le scénario de test :"**Étant donné** que je suis connecté à l'application de gestion de tâches, **Quand** je crée une nouvelle tâche et l'assigne à un autre utilisateur, **Alors** la nouvelle tâche apparaît dans la liste des tâches de l'utilisateur assigné."

#### 1.1.4 Hiérarchiser les besoins :
- Toutes les fonctionnalités ne sont pas égales, c'est pourquoi il faut **classer les fonctionnalités selon leur importance**.
- La classification permet de déterminer l'ordre de développement et ce qui doit absolument être inclus dans la première version (le MVP, Minimum Viable Product).
- Une méthode courante pour cette classification est la méthode MoSCoW :
![Modèle de developpement projet](images/Methode_MoSCoW.png)	
	- Must Have (Doit avoir) : Fonctionnalités absolument critiques sans lesquelles le produit ne peut pas fonctionner (ex : se connecter et créer une tâche).
	- Should Have (Devrait avoir) : Fonctionnalités importantes mais contournables (ex : filtrage avancé des tâches).
	- Could Have (Pourrait avoir) : Fonctionnalités désirables, mais non essentielles (ex : personnalisation des couleurs de l'interface).
	- Won't Have (N'aura pas pour l'instant) : Fonctionnalités reportées à plus tard.

#### 1.1.5 Identifier les dépendances techniques entre fonctionnalités :
- Par exemple, la fonction d'assignation de tâche dépend de l'existence d'une base de données d'utilisateurs.
- Comprendre ces dépendances est essentiel pour planifier le développement et éviter les blocages des équipes techniques de la start-up.
- En définissant des critères mesurables et en hiérarchisant le travail, on s'assure que le produit livré sera non seulement fonctionnel, mais aligné sur les priorités du métier.

#### 1.1.6 Communiquer les besoins à lʼéquipe technique :
- Langage commun entre le client, le Product Owner (PO) et les développeurs :
	- Les termes techniques utilisés par les développeurs (comme API, framework, latency) peuvent ne pas être compris par le client, et inversement, le vocabulaire métier du client doit être traduit en concepts que les développeurs peuvent implémenter.
	- Le PO agit souvent comme ce traducteur essentiel, s'assurant que tout le monde utilise les mêmes définitions pour les mêmes concepts.
	- Par exemple, si le client parle de "Projet", il faut s'assurer que pour le développeur, ce terme ne soit pas confondu avec un "Espace de travail" ou un "Tableau de bord".

- Utiliser des supports visuels. Un simple diagramme peut clarifier un flux de travail complexe plus rapidement que dix pages de texte. 
- Pour l'application de gestion de tâches, utiliser un mock-up (maquette) simple ou un diagramme d'activité montrant le processus de création et de clôture d'une tâche.
> Ne jamais laisser la documentation devenir obsolète. Documenter les décisions et les validations n'est pas une tâche unique, mais un processus continu. Si une exigence change lors d'une réunion avec le client, cette modification doit être immédiatement répercutée dans les User Stories et les critères d'acceptation, puis communiquée aux équipes techniques pour éviter qu'elles ne codent sur des spécifications périmées. C'est le prix à payer pour éviter les malentendus coûteux.
- En démarche Agile, cette communication passe par la formalisation du backlog produit:
	- Le backlog est une liste ordonnée et priorisée de toutes les User Stories et exigences (fonctionnelles et non fonctionnelles) qui constituent le travail à réaliser. Il est le document de référence unique pour les équipes techniques.
	- C'est en transmettant un backlog clair, bien priorisé (grâce à MoSCoW) et doté de critères d'acceptation précis que l'on fournit à la start-up la feuille de route nécessaire pour transformer l'idée d'application de gestion de tâches en réalité fonctionnelle.

### En résumé :
- Commencer par **analyser le contexte du projet** (objectifs, contraintes, utilisateurs cibles) et utiliser des outils comme les User Stories pour **recueillir les besoins exprimés et implicites**, afin de passer d'une idée floue à une base solide de travail.
- Rédiger des cas d'utilisation clairs en employant un vocabulaire précis et non ambigu, tout en distinguant rigoureusement les **exigences fonctionnelles** (ce que le système fait) des **non fonctionnelles** (contraintes de qualité ou de performance).
- Chaque exigence doit être validée par des critères d’acceptation mesurables (souvent rédigés selon le **formalisme Gherkin (User Story (En tant que [rôle], je veux [objectif], afin de [bénéfice]**)) et les fonctionnalités doivent être classées selon leur importance, par exemple grâce à la **méthode MoSCoW**, pour structurer le développement.
- Pour éviter les malentendus coûteux, il faut garantir un **langage commun** entre le client et l'équipe technique, **utiliser des supports visuels** pour clarifier les flux, et maintenir un **backlog produit formalisé et documenté**.
> Après avoir défini le quoi de l'application (exigences fonctionnelles et critères d'acceptation mesurables), il est maintenant temps de préparer le comment en rédigeant les spécifications techniques.

<br>
<br>

### Exercice 1 :
**Contexte :**
<br>L'équipe de la start-up a organisé une réunion initiale pour discuter de la future application de gestion de tâches. Les besoins sont exprimés, mais ils restent formulés de manière vague et ne sont pas mesurables (par exemple : « Il faut que l'on puisse assigner des gens aux tâches », « Il faut que l'application soit sûre »). Ces imprécisions risquent d’engendrer des malentendus coûteux si l'équipe technique commence à travailler sans clarification..

**Consignes :**
1- Rédiger un minimum de trois User Stories pour le besoin "Création et assignation de tâche", en incluant pour chacune d'elles au moins un critère dʼacceptation mesurable.
	- La création de tâche s'effectue à l'aide d'un bouton sur l'écran principal
	- La création de tâche est réalisée à partir d'un formulaire afin de pouvoir définir le type de tâche et y ajouter des informations
	- L'assignation de tâche s'effectue à l'aide d'une liste déroulante contenant le nom de toutes les personnes de l'équipe technique

2- Identifier au moins deux exigences non fonctionnelles (sécurité, performance, etc.) qui s'appliquent à l'application de gestion de tâches, et les formuler de manière précise.
	- Seul les personnes autorisées peuvent créer/modifier/supprimer une tâche
	- La création d'une tâche ne doit pas prendre plus de  clics et minutes

![Modèle de developpement projet](images/Corrige_exercice_1-1.png)

---

### 1.2 Rédiger les spécifications techniques (le COMMENT)
#### 1.2.1 Traduire le langage métier en langage technique :
- Concevoir l’architecture
- Décomposer le projet en composants logiciels
- Rédiger des spécifications techniques solides — véritables plans de construction d’un produit à la fois fonctionnel, performant et évolutif.

#### 1.2.2 Structurer le document de spécifications :
- Organiser l’information de manière logique et exhaustive.
> Ce document est la référence principale pour l'équipe de développement. Il doit être structuré de façon à ce que tout développeur puisse comprendre rapidement l'objectif général, puis se plonger dans les détails d'implémentation de chaque module.
- Pour que votre document soit un guide efficace, il faut inclure trois axes essentiels :
![Modèle de developpement projet](images/Specifications_techniques.png)	

	**1- Présenter le contexte, les objectifs et le périmètre du projet** :
	<br>Il est vital de rappeler le « pourquoi » du projet. Bien que l'équipe technique soit concentrée sur le « comment », elle doit connaître la raison d'être de l'application de gestion de tâches : résoudre les frustrations des équipes techniques de la start-up et améliorer leur flux de travail. Le périmètre définit les limites claires de ce qui sera développé dans cette itération (souvent le MVP, Minimum Viable Product, identifié grâce à la méthode MoSCoW vue au chapitre précédent).

	**2- Décrire les modules, interfaces et flux de données** :
	<br>C'est ici que l'on commence à esquisser la structure interne de l'application. Il faut détailler les principaux modules (par exemple, le module d'authentification, le module de gestion des tâches, le module de notification) et les interfaces qui les relient.
	> Dans la conception logicielle, voici ce que signifie ces trois termes : 
	><br>- **Module** : Un module est une composante autonome d’un logiciel regroupant des fonctionnalités cohérentes et réutilisables.
	><br>- **Interface** : Une interface définit les points de contact et les règles d’échange entre différents modules ou systèmes.
	><br>- **Flux de données** : Un flux de données représente la circulation et la transformation des informations entre les différentes parties d’un logiciel.
	
	Pour représenter les interactions entre ces modules afin qu'elles soient claires, il faut décrire les flux de données.
	Par exemple, lorsque l'utilisateur crée une tâche, le flux pourrait être : *Interface Utilisateur -> Service de Tâches -> Base de Données -> Service de Notification*. Définir ces chemins est opérationnel et concret.

	**3- Indiquer les contraintes techniques et l’environnement d’exécution**
	<br>Les exigences non fonctionnelles qui ont été formalisées au chapitre précédent (comme la performance ou la sécurité) doivent ici être traduites en contraintes techniques spécifiques :
	- Si l'application doit supporter 50 utilisateurs concurrents, cela impose des choix technologiques spécifiques (frameworks, base de données) et des configurations d'environnement (serveurs). 
	- Si l'application est destinée à être développée par des équipes utilisant Python et Java, il faut spécifier comment ces différentes technologies interagiront (par exemple, via des API ou des services web) et dans quel environnement (OS, versions logicielles) le code sera déployé.
	- En structurant le document autour de ces trois axes, cela fournira aux développeurs une fondation solide sur laquelle construire, tout en assurant l'alignement entre les objectifs métier et les solutions technologiques.

#### 1.2.3 Décrire la conception logicielle :
- Les spécifications techniques doivent non seulement détailler les interactions au niveau fonctionnel, mais aussi offrir une vue d’ensemble claire de la manière dont le logiciel est organisé. Cette organisation est dictée par l’**architecture logicielle**, qui est le squelette du système.
- L’architecture définit les grands principes de conception et la manière dont les composants sont structurés. Le choix architectural impacte directement la performance, la maintenabilité et la capacité de l'application à évoluer.

	**1- Présenter l’architecture logicielle retenue** :
	<br>Pour une application moderne comme le gestionnaire de tâches, l’équipe de TechFlow Solutions pourrait choisir une architecture de type Microservices si elle prévoit une forte croissance et souhaite séparer les responsabilités (un service pour les utilisateurs, un service pour les tâches, un service pour les notifications).
	<br>Alternativement, une architecture MVC (Modèle-Vue-Contrôleur) est courante pour les applications web, séparant clairement la logique métier (Modèle), la présentation (Vue) et la gestion des requêtes (Contrôleur).
	> Le modèle Modèle-Vue-Contrôleur (MVC) est un modèle de conception logicielle qui sépare la représentation des informations (le Modèle) des interactions de l'utilisateur avec ces informations (la Vue) et du traitement de l'entrée utilisateur (le Contrôleur). Cette séparation facilite la maintenance et le développement en parallèle des différentes couches de l'application.
	
	**2- Fournir des schémas et diagrammes UML cohérents** :
	<br>Un simple diagramme peut clarifier un flux de travail complexe plus rapidement que dix pages de texte. Les diagrammes UML (Unified Modeling Language) sont le standard de l'industrie pour visualiser la conception logicielle:
	![Modèle de developpement projet](images/Diagramme_classes.png)	
	- Un **diagramme de classes** montrant les attributs et les relations entre les entités principales (Task, User, Project).
	- Un **diagramme de séquence** illustrant l'ordre chronologique des appels de fonctions lors d'un processus spécifique, comme l'assignation d'une tâche.
	- Un **diagramme de composants** décrivant la structure modulaire du système, les dépendances entre les différents modules et la manière dont ils interagissent pour former l’application complète.
	
	**3- Donner des exemples de pseudocode ou de structures de classes** :
	<br>Bien que les spécifications techniques ne soient pas le code final, elles doivent donner un aperçu précis de la logique d'implémentation : 
	- L'utilisation du pseudocode est une méthode excellente pour décrire le processus de résolution d'un problème sans se lier à un langage de programmation spécifique (ce qui est utile pour guider à la fois les développeurs Python et Java).
	- Le pseudocode doit montrer les étapes de vérification, les boucles, et les appels aux fonctions essentielles, garantissant que la logique métier est bien comprise par tous les membres de l'équipe.
	- Par exemple, le pseudocode pour la fonction de mise à jour d'une tâche devra inclure l’étape de vérification des permissions avant de tenter d'accéder à la base de données.
	
	Une description logicielle complète garantit non seulement que le système est fonctionnel, mais aussi qu'il est bien organisé et facile à naviguer pour les futurs développeurs.

#### 1.2.4 Traduire les besoins en solutions techniques :
- Transformation la plus critique : passer d’une exigence utilisateur (« Je veux assigner une tâche ») à un plan d'action technique précis.
> Dans une approche Agile, cela implique de prendre une User Story (US) et de la décomposer en tâches techniques concrètes.
> <br>Si l'on ne décompose pas l'US, les développeurs peuvent interpréter l'exigence de manière trop large ou omettre des étapes nécessaires, entraînant des malentendus coûteux et des retards.

- Pour chaque exigence fonctionnelle, il faut définir la solution technique en suivant trois étapes :
![Modèle de developpement projet](images/Décomposition_US.png)	
	**1- Décomposer chaque exigence en composants logiciels**
	<br>Chaque fonctionnalité n'est pas une action monolithique, mais une série d'interactions entre différents éléments du système. Par exemple, l'US "Modification du statut d'une tâche" se décompose en plusieurs composants :
	- Une Interface Utilisateur qui envoie la requête de mise à jour.
	- Un Contrôleur ou un Service qui reçoit la requête.
	- Un Module de Validation qui vérifie si l'utilisateur a la permission de modifier le statut.
	- Un Module de Persistance qui interagit avec la base de données.
	- Un Module de Notification qui alerte les autres utilisateurs concernés.

	**2- Définir les interactions entre classes, fonctions et modules**
	<br>C'est l'étape de la micro-conception. Si l'on utilise le terme technique « classe » (commun en Python et Java), ilfaut préciser la nature de la communication : quelles méthodes sont appelées ? Quels sont les arguments passés ? Quelles sont les valeurs de retour attendues ? Définir ces interactions permet de s’assurer que les développeurs travaillant sur des modules différents peuvent intégrer leur code sans friction.

	**3- Spécifier les formats d’entrée/sortie et les protocoles de communication**
	<br>C’est le cœur opérationnel de l’échange de données. Si l'application de gestion de tâches utilise des microservices, les services Python et Java doivent communiquer efficacement. Il faut spécifier le format des données échangées (par exemple, JSON ou XML) et le protocole utilisé (par exemple HTTP).
	> Dans le développement logiciel moderne, la spécification des protocoles de communication est cruciale. Si une requête HTTP est utilisée pour créer une tâche, il faut définir l'URL (ex: /api/v1/tasks), la méthode HTTP (POST), et la structure exacte des données attendues en entrées au format JSON (payload) en entrée (ex: {"title": "...", "assigned_to": "..."}) et en sortie (la réponse du serveur, par exemple, un code 201 Créé).

	Cette traduction rigoureuse évite l'ambiguïté et fournit à l'équipe technique des blocs de travail précis, appelés tâches techniques, pour la mise en œuvre de chaque exigence métier.

#### 1.2.5 Intégrez la qualité, la maintenabilité et l’évolutivité
- Un logiciel réussi pour ne se définit pas seulement par sa capacité à créer et assigner des tâches. Il se définit également par sa **qualité** et sa **maintenabilité**. Si le code est illisible, incohérent, ou manque de documentation, les futures modifications engendreront inévitablement des malentendus coûteux et des goulots d'étranglement.

- Les spécifications techniques doivent donc aller au-delà de la simple description fonctionnelle pour imposer des critères de qualité qui guideront les pratiques de codage de l’équipe :

	**1- Préciser les normes de code et conventions de nommage**
	<br>L'uniformité est essentielle. Si les développeurs Python utilisent le snake_case pour les noms de variables, et les développeurs Java le camelCase, il est crucial d'établir des conventions claires pour les interfaces communes (comme les noms d'attributs dans les messages JSON échangés). Il faut spécifier :
	- Le format des commentaires.
	- La longueur maximale des lignes de code.
	- L'utilisation d'outils de formatage automatique (linters).
	- Les conventions de nommage pour les classes, les fonctions et les variables (par exemple,update_task_statusplutôt quefunc1_mod_stat). Ces choix doivent être consignés dans les spécifications pour assurer une cohérence d'ensemble.

	**2- Anticiper les tests dès la phase de spécification**
	<br>Dans le chapitre précédent, vous avez défini des critères d'acceptation (ex: « Le formulaire valide et enregistre la tâche en moins de 3 secondes »). Ces critères sont la base des tests fonctionnels. Cependant, les spécifications techniques doivent anticiper les tests unitaires.
	> Lorsque l'on rédige le pseudocode ou décrit une fonction, il faut se poser la question : "Comment tester ce petit morceau de code de manière isolée ?". Si une fonction est trop complexe (trop de responsabilités), elle est difficile à tester. Les spécifications techniques doivent favoriser une décomposition qui rend les tests unitaires simples et rapides. Par exemple, la vérification des permissions devrait être une fonction testable indépendamment de la mise à jour de la base de données.

	**3- Documenter les dépendances logicielles et versions utilisées**
	<br>Si le service de gestion des tâches dépend d'une bibliothèque spécifique pour le chiffrement des données ou pour l'envoi d'e-mails, ces dépendances doivent être listées précisément, avec leurs numéros de version. La documentation des versions (par exemple, Python 3.10, Java 17) assure que l'environnement de développement et de production reste cohérent et que l'on évite des incompatibilités futures. Cette documentation, qui fait partie du backlog produit de référence, doit être maintenue vivante, car si une dépendance évolue, l'impact sur l'application doit être clairement communiqué.
	
	En intégrant la qualité dès le départ, on s'assure que le travail fourni par les équipes techniques sera non seulement terminé, mais qu'il répondra aux standards de robustesse et de lisibilité essentiels pour la réussite à long terme du projet.

### En résumé :
- Les spécifications techniques traduisent le **« quoi » fonctionnel** en un **« comment » technique** détaillé pour les équipes de développement.
- Un document de ST doit être structuré autour du **contexte et des objectifs, de la description des flux et modules, et des contraintes techniques** (environnement d’exécution).
- Il est crucial de **décomposer les User Stories** en composants logiciels et de définir précisément les **formats d'entrée/sortie et les protocoles** de communication entre ces composants.
- La conception doit être visualisée à l'aide de **diagrammes UML** et le processus de mise en œuvre doit être éclairci par des exemples de **pseudocode**.
- Pour assurer la qualité et la maintenabilité, il faut **préciser les normes de code** (conventions de nommage) et **anticiper les tests unitaires** dès la phase de spécification.

<br>
<br>

### Exercice 2 :
**Contexte :**
<br>Les besoins fonctionnels pour l'application de gestion de tâches de TechFlow Solutions sont désormais validés, y compris les User Stories concernant la mise à jour du statut des tâches. L'équipe de développement s'apprête à concevoir l'architecture, et les développeurs Python et Java ont besoin de spécifications techniques précises pour la mise en œuvre. Il faut maintenant leur fournir la décomposition technique d'une fonctionnalité clé.

**Consignes :**
- Structurer la partie technique du document de spécifications pour la fonctionnalité "Modification du statut d'une tâche". 
- L'objectif est de guider les développeurs sur le processus d'implémentation :
	<br>1- **Décrire le flux de données** et les interactions entre au moins deux composants logiciels (par exemple, l'Interface utilisateur (UI), un Service, et la Base de données (DB)).
	<br>2- **Fournir un exemple de pseudocode synthétique** pour la fonction principale de mise à jour du statut, en respectant une norme de nommage cohérente (utilisez le snake_case pour cette démonstration, comme norme de codage). Le pseudocode doit illustrer les étapes de validation et d'appel à la couche de persistance.

	![Modèle de developpement projet](images/Corrige_exercice_1-2.png)	

---

### 1.3 Maintenir les spécifications techniques à jour
Dans un projet **Agile**, rien n’est jamais figé : les besoins évoluent, le client change d’avis, et les documents doivent suivre.

#### 1.3.1 Valider les spécifications
Avant de commencer le codage, il est essentiel de procéder à une validation rigoureuse. Cette étape garantit que le document est complet, sans ambiguïté et aligné sur les attentes.

- **Impliquer toutes  les parties prenantes**
<br>Le rôle est d’organiser une revue avec :
    * **Product Owners (PO) / Clients :** pour valider l'alignement métier.
    * **Architectes :** pour vérifier que l'architecture (Microservices, MVC) est appropriée.
    * **Développeurs :** pour valider la faisabilité technique et les dépendances.

- **Vérification de la traçabilité**
	<br> - Capacité à lier chaque élément du cycle de vie du projet. 
	<br> - Si le client demande un changement, ou si un test échoue, il faut pouvoir remonter rapidement à l'exigence métier initiale pour comprendre l'impact.
	<br> - Il faut vérifier que :
    1.  Chaque exigence fonctionnelle **User Story (US)** est **couverte par une section des spécifications techniques**.
    2.  Chaque **spécification technique** est associée à un **critère d’acceptation mesurable** et à un scénario de test.

	<br> - Si l'US n'a pas de test associé ou si sa décomposition technique est manquante, il y a un trou de traçabilité. Cela signifie que l'équipe pourrait coder une fonctionnalité non testable ou qui ne répond pas au besoin initial.
	<br> - En organisant des revues croisées et en vérifiant ces liens avant le codage, on assure une fondation solide pour la suite du projet. C'est ainsi que l'on transforme les spécifications techniques d'un simple document en un véritable contrat de travail.

#### 1.3.2 Gérer les modifications et les versions
Une fois le développement lancé, il est primordial d’avoir une méthode stricte pour gérer **les modifications et les versions** du document de spécifications via deux piliers :
- **La gestion de version**
<br> Utilisez des outils comme **Git** ou des systèmes intégrés pour suivre les **modifications**. C'est vital pour que l'équipe travaille toujours sur la version de référence actuelle.
>La documentation vivante : Ne jamais laisser la documentation devenir obsolète. Si une exigence change lors d'une réunion avec le client, cette modification doit être immédiatement répercutée dans les User Stories, les critères d'acceptation et les spécifications techniques, puis communiquée aux équipes. Le prix à payer est le risque de malentendus coûteux.
- **Le Journal des modifications (Changelog)**
<br> Outil pragmatique pour saisir l’historique des évolutions. Un bon Changelog inclut :
    * La **date** et l'**auteur** du changement.
    * La **nature** de la modification (ex: ajout d'exigence, correction API).
    * La **raison** (ex: retour client, adaptation légale).

	Le changement doit être documenté dans le journal et la nouvelle dépendance logicielle (avec sa version exacte) doit être listée dans les spécifications pour **garantir la cohérence entre le code et la documentation**.

#### 1.3.3 La documentation "vivante" (Living Documentation)
Dans un contexte Agile, la documentation ne doit pas être un poids mort. Elle doit évoluer au même rythme que le code.
- **Le concept de "Docs as Code"** : Consiste à stocker la documentation (fichiers Markdown) dans le même dépôt Git que le code source. Cela permet de soumettre les changements documentaires à la même procédure de validation que le code (Pull Requests).
- **Synchronisation automatique** : Utiliser des outils pour générer une partie de la documentation technique à partir du code lui-même (comme Swagger/OpenAPI pour les API), garantissant que les spécifications d'interface sont toujours exactes.

#### 1.3.4 Adapter les spécifications à la méthodologie de projet (Agile)
En Agile, les spécifications sont un **artefact vivant** qui évolue par itérations (ou sprints).

- **Le Backlog Produit**
	- C'est la source de vérité. C'est la liste ordonnée et priorisée de tout le travail à effectuer, composé de User Stories (US) et d’exigences (fonctionnelles et non fonctionnelles).  Les specs techniques se situent juste en dessous des User Stories (US).	
	- Une méthode opérationnelle pour maintenir ce lien est d'utiliser les tickets du backlog pour compléter le document de spécifications :
	![Modèle de developpement projet](images/Tracabilite_backlog_specs.png)
- **Just-in-time documentation**
	- La spec détaillée n'est rédigée que juste avant que l'équipe de développement ne commence à travailler sur la fonctionnalité.
	- Le reste des spécifications reste à un niveau plus élevé tant que la fonctionnalité n'est pas prioritaire, souvent classée grâce à MoSCoW (Must Have, Should Have, etc.).
- **Évolution à chaque itération**
	- Si une solution technique plus efficace est proposée lors d'une revue de sprint, elle doit être consignée immédiatement dans les spécifications de référence.
	- Si une US est reportée au statut Won't Have, les spécifications détaillées associées peuvent être dépriorisées.

L'adaptation à la méthodologie Agile encourage un niveau de spécification suffisant mais pas excessif. Viser la clarté et l'opérationalité.
>Le détail technique (diagrammes UML, spécification des protocoles JSON/REST) est là pour éviter l'ambiguïté, mais il doit se concentrer sur les éléments critiques de l'architecture et de l'intégration, permettant aux développeurs de se concentrer sur la résolution effective du problème.

#### 1.3.5 Maintenir la qualité documentaire
- Une documentation de mauvaise qualité est source de malentendus coûteux.
	1.  **Éviter la sur-spécification :**
	<br>Ne pas dicter les détails d'implémentation interne qui devraient être laissés à la discrétion du développeur.
	<br>Se concentrer sur le **quoi** et les **interfaces** (format des données, protocoles d'échanges, normes de code), et non sur tous les détails d'implémentation interne, qui risqueraient de rendre la documentation rigide et difficile à mettre à jour.
	2.  **Rester précis sur le critique :**
	<br>Les exigences non fonctionnelles (performance, sécurité) doivent être traduites en choix technologiques précis et non ambigus dans les spécifications techniques.
	<br>C'est la distinction entre imposer un temps de chargement maximal (ENF critique) et imposer la façon dont le développeur doit écrire une boucle (détail inutile).
	3.  **Centralisation et lisibilité :**
	<br>Utiliser un référentiel de documentation unique où toute l'équipe (PO, développeurs, QA) peut trouver la version actuelle et validée des spécifications. 
	<br>Utiliser des phrases courtes, en définissant les termes techniques (comme API, framework), et en s'appuyant sur des supports visuels, comme les schémas et diagrammes, qui clarifient les flux de travail complexes plus rapidement qu'un long texte.

- Le maintien de la qualité documentaire exige de favoriser la collaboration continue entre PO, développeurs et QA (Quality Assurance):
	![Modèle de developpement projet](images/Boucle_collaboration.png)
	- Le **PO** s'assure que les modifications correspondent aux priorités MoSCoW,
	- Les **développeurs** s'assurent que les normes de code (snake_case, camelCase) sont respectées et documentées,
	- L'équipe **QA** utilise les critères d'acceptation Gherkin pour créer des tests de validation.

	Cette boucle de rétroaction constante garantit que le document de spécifications est non seulement cohérent, mais qu'il reflète fidèlement l'état réel et l'évolution du produit développé par TechFlow Solutions. En maintenant ces standards, vous assurez la robustesse et l'évolutivité de l'application à long terme.

---

### 1.4 Synthèse du Flux de Travail (Workflow)
Pour récapituler la Partie 1, voici le flux logique de transformation d'un besoin en produit :

Cadrage : Recueil des besoins (User Stories) et définition des critères d'acceptation (Gherkin).

Conception : Traduction en architecture, modules et diagrammes UML (Classes, Séquence).

Décomposition : Transformation des US en tâches techniques (spécification JSON/HTTP).

Réalisation & Qualité : Codage respectant les normes (snake_case, tests unitaires) et mise à jour des Changelogs.

---

### En résumé
La réussite du projet repose sur un flux logique de transformation d'un besoin en produit, soutenu par une gestion rigoureuse de la qualité documentaire
	
1- **Le Pipeline de Transformation**
- **Cadrage** : Recueil des besoins via les **User Stories** et définition des critères d'acceptation selon le formalisme **Gherkin**.
- **Conception** : Traduction du besoin métier en **architecture logicielle** (Microservices, MVC), illustrée par des diagrammes **UML** (Classes, Séquence, Composants).
- **Décomposition** : Fragmentation des US en tâches techniques concrètes avec spécification des interfaces et protocoles (**JSON/HTTP**).
- **Réalisation & Qualité** : Codage respectant les normes (ex: **snake_case**), développement des tests unitaires et mise à jour systématique des **Changelogs**.

2- **Les Piliers de la Gouvernance Documentaire**
- **Validation & Traçabilité** : Impliquer toutes les parties prenantes (clients, développeurs, architectes, testeurs) pour vérifier que chaque exigence fonctionnelle est couverte par une conception technique et un test de validation.
- **Gestion du Changement** : Utiliser un système de **gestion de version (Git)** pour la documentation et consigner chaque évolution dans un **Changelog** afin d'éviter tout désalignement entre le code et les specs.
- **Agilité Opérationnelle** : Pratiquer la **documentation juste-à-temps** en faisant évoluer les specs au rythme du Backlog et des itérations. Les tickets de développement servent de ponts vivants vers la documentation technique.
- **Collaboration & Sobriété** : Maintenir une documentation centralisée et lisible en évitant la **sur-spécification**. L'accent doit être mis sur les interfaces et les contraintes critiques, laissant la liberté d'implémentation interne aux développeurs.
<br>
<br>

### Exercice 3 :

**Contexte :**
<br>L'équipe Ops exige l'intégration rapide d'une nouvelle fonctionnalité : **lier une tâche à un ticket JIRA externe**.

**Consignes :**
1.  Consigner ce changement dans un **Changelog** synthétique.
2.  Décrire comment aller vérifier la **traçabilité** de cette nouvelle exigence par rapport aux tests et aux User Stories.
3.  Expliquer comment s'assurer que le document reste **cohérent et à jour**.

![Modèle de developpement projet](images/Corrige_exercice_1-3.png)

<br>

---


## 💡 Mes Réflexions "Data Architect"
- **La donnée comme pivot** : En tant qu'architecte, je note que la définition des flux de données (section 1.2.2) est l'étape la plus critique. Si le schéma de données est mal conçu au départ, aucune qualité de code ne pourra compenser la rigidité du système.
- **L'imposition du format** JSON et des méthodes REST (POST, GET) dès la phase de spécification est ce qui permet l'interopérabilité réelle entre les services Python et Java de la start-up.
- **Le danger du "Ghost Doc"** : Une spécification qui n'est pas mise à jour après un changement en Sprint devient une dette technique documentaire. Il est crucial d'intégrer la mise à jour du Wiki dans la "Definition of Done" (DoD) des tickets.
- **Interfaces vs Implémentation** : En tant qu'architecte, mon focus doit rester sur la robustesse des contrats d'interface (API). Tant que le JSON de sortie est respecté, la logique interne du microservice appartient au développeur.

## ❓ Points à approfondir / Questions
- [ ] **Automatisation** : Comment lier techniquement un ticket Azure Boards à une section précise du Wiki pour automatiser la traçabilité ?
- [ ] **Versionnage** : Comment gérer le versionnage des schémas UML (ex: format .drawio ou .plantuml) directement dans le dépôt Git pour suivre le "Docs as Code" ?
- [ ] **Gherkin & QA** : Existe-t-il des outils pour transformer automatiquement les critères d'acceptation Gherkin du PO en scripts de tests automatisés ?