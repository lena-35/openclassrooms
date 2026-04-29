# 📓 Notes : Réalisez un cahier des charges fonctionnel

> **Cours :** [Lien OpenClassrooms](https://openclassrooms.com/fr/courses/6739646-realisez-un-cahier-des-charges-fonctionnel)

> **Début du cours :** 31/03/2026

> **Fin du cours :** 06/04/2026

---

## 🧭 Partie 1 : Découvrez le rôle de la documentation projet
*Notes sur l'importance de documenter pour un Data Architect.*

### 1.1 Documenter pour mieux communiquer
- Les risques d'une mauvaise documentation :
	- Coût des changements à apporter au cours de l'élaboration du projet.
![Modèle de developpement projet](images/Modèle_Dev_Projet.jpg)

- Faciliter la communication par la documentation :
	- Informer les intervenants.
	- Définir l'interaction entre plusieurs systèmes.
	- Faciliter la communication entre les équipes distantes.
	- Soutenir le dé veloppement agile: utilisation et la maintenance du produit.
	- Préparer des audits de projets et/ou de systèmes : vérification de sécurité ou de conformité aux réglementations.
	- Pour son propre bénéfice : garder mes pensées organisées et me souvenir dans le temps.

- Rédiger une documentation :
	- Écrire dans un but clair.
	- Etre attentif au public.
	- Amener le lecteur directement au but.

### 1.2 Communiquer efficacement les idées grâce à la documentation
- Déterminez quand vous avez besoin de documentation :
	- A-t-on besoin de la documentation tout de suite ?
	- Documentation juste à temps : ne pas planifier entièrement les processus futurs.

- Écrivez dans un état d'esprit agile :
	- Rédiger la documentation en fonction des besoins.
	- Rédiger uniquement la documentation qui s’applique au sprint en cours.
	
- Identifier le public cible avec la documentation appropriée (outil de référence, manuel de formation,...).

- Déterminer le coût en temps :
	- Documenter juste ce dont les parties prenantes ont besoin, ni plus ni moins.

- Déterminez le quand de votre documentation :
	1.  Avant le début du projet :
		- Quelques diagrammes d'architecture de haut niveau pour identifier les principaux composants de la solution que vous allez implémenter.
		- Une description des caractéristiques essentielles du produit proposé.
		- La liste des exigences principales – elles peuvent être de haut niveau ou détaillées, selon la qualité de la définition du projet à ce stade.
	2.  Pendant le projet :
		- Des besoins, minimalistes mais suffisants – ils sont donnés aux développeurs avant chaque sprint.
		- Une description du système et des processus à l’intérieur du projet – par exemple, les résultats de chaque sprint seront partagés avec les parties prenantes et plus tard avec les équipes de maintenance. 
		- Documenter le code.
	3. Après la réalisation du projet :
		- Manuel utilisateur.
		- Manuel maintenance.

- Déterminez le où de votre documentation :
	- Eviter Word ! Il faut un document vivant et non static.
	- Google Docs.
	- Wiki GitHub.

- Déterminez le quoi de votre documentation: les 7 règles :
	1. Divertir le lecteur pour ne pas qu'il s'ennuie :
		- Si je ne me soucie pas de ce que j'écris, le lecteur ne se souciera pas de le lire.
	2. Avant de commencer, être clair sur ce que l'on veut que le lecteur fasse une fois qu'il aura terminé :
		- Enoncer l'intention et les objectifs.
	3. Écrire en suivant un plan bien défini :
		- Ajouter un sommaire.
	4. Éviter les mots ambigus.
	5. Clarté :
		- Illustrations (graphiques, tableaux, images,...) + mots pour expliquer.
		- Numéroter et nommer les légendes.
		- Faire référence aux illustrations dans le texte avec le bon nom.
	6. Lorsqu'il s'agit de concepts abstraits... illustrer avec des exemples logiques :
		- Illustration appropriée.
		- Exemple logique associé.
	7. Réviser la documentation pour la tenir à jour.

- Une documentation efficace apporte de la valeur au lecteur lorsqu'elle :
	- N'ennuie pas le lecteur,
	- Est claire sur ce que le lecteur doit faire après la lecture,
	- Evite les mots ambigus,
	- Utilise des illustrations couplées à des exemples pour plus de clarté,
	- Est facile à réviser.

### 1.3 Avantages du Cahier des Charges Fonctionnel (CDCF)
- Un cahier des charges peut être défini comme un résumé des faits, des constatations et des objectifs visant à fournir au lecteur un bref aperçu au niveau d'un plan, d'une situation ou d'un projet.

- Il existe différents types de cahier des charges mais 4 sont très courants :
	- Recueil des besoins commerciaux (dans certains cas),
	- Cahier des charges fonctionnel,
	- Brief créatif,
	- Cahier des charges technique ;

- Le cahier des charges fonctionnel n’est généralement pas écrit par le client, mais plutôt par le chef de projet. Le client peut préparer un cahier des charges pour l'agence de développement, ou le chef de projet peut mener des entretiens avec le client afin de déterminer les besoins du projet. Le chef de projet prépare ensuite le cahier des charges fonctionnel qui est un résumé du projet que le client a demandé et qui est présenté au client pour vérification et approbation. Cela donne au client l'assurance que le chef de projet comprend exactement ce qu'il veut et sert d'énoncé de ce qui sera livré.
	- Un résumé du projet demandé par le client.
	- L'assurance que le chef de projet comprend exactement ce que l'on attend de lui.
	- Un énoncé de ce qui doit être livré.
	
- Les méthodologies agiles suppriment le SRS (software requirements specifications qui demande à ce que le projet soit planifié dans son intégralité, jusque dans les moindres détails, avant même que la conception ou le développement n’aient eu lieu), au profit de documents beaucoup plus courts qui contiennent juste assez d'informations et qui sont produits juste à temps pour être utilisés. Ce modèle constitue naturellement un support efficace pour l'évolution des projets et de la documentation. Si des modifications sont apportées, seules de petites modifications dans la documentation seront nécessaires, et les documents suivants seront écrits avec les modifications déjà appliquées.

### Résumé de la partie 1
- Une bonne planification est essentielle à la réussite d'un projet.

- Les méthodologies agiles peuvent aplatir la courbe du coût du changement.

- L'objectif premier de toute documentation est la communication.

 - N’écrivez que la documentation nécessaire à votre projet, ni plus, ni moins.

- Les documents agiles sont des documents vivants, c'est-à-dire qu'ils sont constamment mis à jour au fur et à mesure qu'ils évoluent avec le projet. Pour cela, GitHub est un bon point de départ.

 - Une documentation efficace apporte de la valeur au lecteur lorsqu'elle :
	- N'ennuie pas le lecteur,
	- Est claire sur ce que vous voulez que votre lecteur fasse après la lecture,
	- Evite les mots ambigus,
	- Utilise des illustrations couplées à des exemples pour plus de clarté,
	- Est facile à réviser ;

- Un cahier des charges  est un résumé des faits, des constatations et des objectifs visant à fournir au lecteur un bref aperçu de haut niveau d'un plan, d'une situation ou d'un projet.

- Le cahier des charges fonctionnel, dans le cadre d'un projet de développement agile, fournit :
	- Un résumé du projet demandé par le client.
	- L'assurance que le chef de projet comprend exactement ce que l'on attend de lui.
	- Un énoncé de ce qui doit être livré.

---

## 🛠️ Partie 2 : Préparez un cahier des charges fonctionnel
*Notes sur la phase de conception et de recueil.*

### 2.1 Contenu type d'un CDCF
- Un cahier des charges fonctionnel bien construit doit être concis (1 ou 2 pages), simple, organisé et répondre au critère agile de juste assez (quand il fait partie d'un processus agile). Il doit énoncer des objectifs clairs, orienter le lecteur et le langage utilisé doit être concret et éviter les termes vagues et peu clairs.

- Un cahier des charges fonctionnel bien construit aide :
	- L'équipe à produire un travail de meilleure qualité, et à mesurer l’avancement du projet,
	- L'équipe à gagner du temps et de l'argent,
	- A démontrer l’intérêt du travail effectué auprès du client.

	- Se poser les questions suivantes :
		1. Comment vous et votre client allez gérer le projet ? (Direction du projet)
		2. En ce qui concerne le projet, où en sommes-nous maintenant ?
		3. Où voulons-nous arriver ?
		4. Qu’allons-nous faire pour y parvenir ?
		5. À qui devons-nous nous adresser ? 
		6. Comment saurons-nous si le projet est réussi ?
		7. Quels sont les aspects pratiques ?
		8. Quelles approbations sont nécessaires pour procéder ?
		
- *Exemple* :

		DIRECTION DE PROJET
			- Toutes les données courantes du projet et les coordonnées des personnes ressources doivent être indiquées ici.
			- Nom et type du projet
			- Date 
			- Nom de l'entreprise (client)
			- Marque ou variante (le cas échéant)
			- Coordonnées du client (inclure tous les noms/titres et coordonnées)
			- Nom et coordonnées de votre agence 

		OÙ EN SOMMES-NOUS MAINTENANT ?
			- Décrivez la situation actuelle, tout contexte nécessaire et les principaux problèmes auxquels le client est confronté et qui ont motivé le lancement de ce projet. 

		OÙ VOULONS-NOUS ARRIVER?
			- Décrivez le(s) objectif(s) du client pour le projet. 

		QU’ALLONS-NOUS FAIRE POUR Y PARVENIR ?
			- De nombreux projets ont des composantes multiples et plusieurs équipes y travaillent. Si vous concevez une architecture système, il se peut qu'une équipe de conception d'UX soit également impliquée. C'est ici que vous documentez les détails supplémentaires qui sont pertinents à votre succès sur le projet.

		À QUI DEVONS-NOUS NOUS ADRESSER ?
			- Chaque projet a un public cible. Il s'agit des personnes directement concernées par le projet, dont la vie et/ou les emplois peuvent être directement affectés. Il est souvent important d'obtenir des réponses de ce groupe, tant avant la conception du projet qu'après son achèvement. Définissez ici les différents publics et classez-les par ordre de priorité en fonction de leurs besoins en termes de contacts.

		COMMENT SAURONS-NOUS SI LE PROJET EST RÉUSSI ?
			- Vous et votre client devez établir à quoi ressemblera le succès. Pour ce faire, vous devrez répondre aux questions suivantes pour chacun des objectifs : 
			- Comment le succès sera-t-il mesuré ? 
			- Quand sera-t-il mesuré ? 
			- Qui le mesurera ? 
			- Il est essentiel de connaître cette information. C'est le seul moyen d'évaluer la rentabilité de l'investissement du client (ROI pour Return On Investment, en anglais).

		QUELS SONT LES ASPECTS PRATIQUES ?
			- Les aspects pratiques font référence à tout élément du projet qui n'a pas été décrit précédemment et qui nécessite un examen pratique lors de la planification du projet. Ils peuvent être différents pour chaque client, mais voici quelques considérations communes :
			- Etapes clés du projet et dates de livraison.
			- Dates d'inscription ou dates limites pour les activités internes/externes associées.
			- Intégration avec d'autres activités de développement ou de marketing (par exemple, le client planifie-t-il une campagne de marketing pour le déploiement de ce projet et cette campagne a-t-elle une date précise à laquelle le projet doit être prêt ?).
			- Dépendances et contraintes (ou faire référence à un document spécifique si trop long)
			- Autres considérations. C'est souvent un lieu réservé à la documentation des contraintes. Chaque client et chaque projet aura des aspects pratiques différents que vous devrez passer au crible avant de pouvoir commencer le projet. 

		APPROBATIONS
			- C'est la dernière partie du cahier des charges . Déterminez qui a le pouvoir d'approuver ou de vérifier le travail que vous produisez. Il devrait s'agir de la ou des mêmes personnes qui approuvent le cahier des charges avant le début des travaux du projet.

- Les sujets importants pour rédiger un CDCF:
	- Le cahier des charges fonctionnel est l'élément d'information le plus important sur lequel vous et votre client vous entendrez ;
	- Un cahier des charges doit être bref (1 ou 2 pages). Il est conçu dans un but précis, ni plus ni moins. ;
	- Un cahier des charges efficace énonce des objectifs clairs ;
	- Les objectifs d'un cahier des charges définissent les critères de réussite du projet ;
	- Un cahier des charges fonctionnel peut presque s'écrire tout seul lorsque vous posez les bonnes questions.


### 2.2 Recueillir les besoins du client
- Les séances de brainstorming frénétiques ne sont pas de bonnes méthodes pour recueillir les besoins. Elles sont parfaites pour générer des idées, mais ces idées doivent ensuite être passées au crible, analysées et comparées les unes aux autres pour déterminer ce qui est faisable et ce qui ne l'est pas, ce qui est important et ce qui ne l'est pas, ce qui procure un avantage vérifiable et ce qui ne le fait pas.

- Faire un résumé des besoins :
	- Le client a identifié un problème à résoudre, mais il ne sait pas comment le résoudre ni comprendre ce que la solution pourrait exiger.
	- Aider le client à nous aider à identifier ses besoins.

- Mener des entretiens avec les clients et les intervenants :
	- Extraire les besoins auprès du client et/ou des intervenants
	- Parler à plusieurs personnes aide à obtenir une bien meilleure vue d'ensemble du problème et de ce qui est nécessaire pour le résoudre. 
	- Les personnes qui utilisent quotidiennement sont les plus susceptibles de donner un véritable aperçu du problème et de ses effets, permettant ainsi de définir plus clairement des besoins concrets.

- Observer en temps réel :
	- Observer des personnes interagissant avec le système actuel peut vous fournir une mine de renseignements sur les points problématiques.
	- 
	
- Comparer observations avec cahier des charges client et les entretiens.
	- Informations sur le problème et les remèdes souhaités = rédiger des objectifs (besoins) clairs et précis.

- Réalisez un cahier des charges fonctionnel :
	- Posez les bonnes questions :
		1. "**Où en sommes-nous maintenant?**" fournit une description et le contexte du problème à résoudre.
		2. "**Où voulons-nous arriver?**" constitue la base des objectifs du projet.
	- Si les objectifs ne sont pas aussi clairs qu'ils devraient l'être, approfondir les questions pour obtenir de la clarté :
		- Quelle est la raison commerciale d'investir dans cet objectif particulier ? 
		- Qu'est-ce que cela entraîne pour l’entreprise? 
		- Comment la réalisation de cet objectif sera-t-elle mesurée ?
		- Pour quel niveau d'amélioration le retour sur investissement est-il optimal ?

- Catégorisez les besoins :
	- Les **besoins fonctionnels** sont ceux qui précisent ce que le système doit faire, comme une fonction, un comportement ou une action qu'il doit exécuter :
		- Fonctions administratives ;
		- Authentification ;
		- Autorisation ;
		- Suivi des audits ;
		- Besoins en matière de certification ;
		- Besoins en matière de rapports ;
		- Besoins légaux ou réglementaires.
	- Les **besoins non fonctionnels** décrivent comment le système doit fonctionner.
		- Précise les critères selon lesquels un système est jugé, plutôt que des comportements spécifiques.
			- Exemple "besoins de performance"  : « Toutes les procédures stockées dans la base de données doivent renvoyer les résultats dans les 0,5 secondes. »
		- En plus des besoins de performance, il peut y avoir d'autres besoins non fonctionnels :
			- Disponibilité,
			- Capacité,
			- Intégrité des données,
			- Environnemental,
			- Maintenabilité,
			- Recouvrabilité,
			- Fiabilité,
			- Evolutivité,
			- Sécurité,
			- Utilisabilité.

-  Prioriser les besoins :
	- A faire avec le client :
		- Identifier les dépendances entre les différents besoins.
		- Définir l'ordre des priorités.
	> Utiliser cet ordre de priorité pour planifier les sprints.

- Recueillir les besoins :
	- Méthodes courantes de collecte des besoins : un résumé des **besoins fonctionnels et non fonctionnels**, des **entretiens** avec les clients et les intervenants et des **observations en temps réel**.
	- Les deux questions les plus importantes pour la collecte des besoins constituent également les titres dans le cahier de charges  du client : **Où sommes-nous maintenant?** et **Où voulons-nous être?**
	- Les besoins peuvent être classés comme étant **fonctionnels** et **non fonctionnels**.
	- Les besoins fonctionnels décrivent **ce** qu'un système devrait réaliser, alors que les besoins non fonctionnels décrivent **comment** un système fonctionne.
	- Prioriser les besoins




- *Exercice* :

		**BESOINS FONCTIONNELS** (ce que le système doit faire)
			- Analyser les ventes
				- Comparaison ventes gamme actuelle et nouvelle game
					-> comment on récupère les données des anciennes ventes?
				- Surveiller les achats faits par les femmes pour elles-mêmes
			- Anticiper 
				- Définir le volume des ventes de la nouvelle collection d'une semaine à l'autre
				- Définir la réduction du volume des ventes de la gamme actuelle
				-> sur quoi on se base
			- Fournir le nombre de produits adéquat pour les deux collections
				-> il faut avoir réussi a anticiper comment chaque collection va s'ajuster en vente
			- Analyser quelles couleurs et/ou quels motifs de la collection féminine sont les plus vendus
			- Recueillir les données de vente
			- Suivre les données
			- Analyser les données
				-> analyse générale ou pour chaque plateforme ou magasin physique?
			- Analyses statistiques sur la population dans un rayon de 25 km autour de chacun de nos magasins physiques
				- quel pourcentage de la population locale sont des femmes
				- quelles sont les catégories d'âge
				- les tranches de revenus les plus représentées
				- le pourcentage de célibataires et de couples mariés (ou autre)
				- pouvoir rajouter des catégories
				- être en mesure d’observer les changements démographiques au cours du temps	
				-> donc uniquement pour des achats physiques ou bien il faut rattacher un achat en ligne à un magasin?
				-> les gens ne vont peut être pas vouloir répondre à toutes ces questions intrusives
			- Identifier des tendances entre un profil démographique et les ventes de la nouvelle gamme	pour mieux évaluer comment gérer les stocks de chaque magasin
				-> sous les combien de temps?
				-> stock des magasins et pas en ligne du coup
			- Recueil des données démographiques une fois par trimestre pour chaque magasin
				-> sous quelle forme le recueil?
			- Repérer des changements importants
				-> sous quelle forme?
				
		**BESOINS NON FONCTIONNELS** (comment le système doit fonctionner)
			- Multiplateforme : magasins physiques USA & UE + boutique en ligne + Amazon
	

	
	
	
	
### 2.3 Identifier les contraintes et risques du projet
- Les **contraintes** et les **risques**, comme les **dépendances**, affectent la façon de planifier les phases de votre projet. Les contraintes **limitent** ou **restreignent** vos options et doivent être exprimées avec **clarté**.

- Au fur et à mesure de l'élaboration du cahier des charges fonctionnel, il est impératif de documenter les contraintes d'une manière aussi claire et concise que pour les besoins.

- Identifier le type de contraintes :
	- Contraintes de temps (planning),
		- Mauvais : « Le projet doit être terminé dès que possible. » Qu'est-ce que cela signifie ? Y-a-t-il quelque chose ici qui soit utile à qui que ce soit ?  
		- Bon : « Le projet doit être terminé et livré avant 18 h le 17 octobre. »
	- Contraintes de ressources,
		- Mauvais : « Deux développeurs à temps partiel sont affectés à ce projet. » Eh bien, nous savons combien de développeurs à temps partiel nous pouvons avoir, mais nous n'avons aucune idée de ce que constitue le temps partiel. Combien d'heures peuvent-ils travailler ? Est-ce l'équivalent d'un développeur à temps plein ? Peut-on en avoir un à plein temps à la place ? D'où viennent les développeurs ? Le client les fournit-il à partir de son propre personnel ou devons-nous faire appel à des freelances ?
		- Bon : « Deux développeurs à temps partiel seront fournis par le client pour un maximum de trois heures par jour pour les deux premiers sprints du projet. »
	- Contraintes techniques (Formats de données, APIs),
	- Contraintes de budget.

- Documentez et gérez les contraintes/risques :
	- Étape 1 : Créer un **registre de toutes les dépendances** du projet
		- Une dépendance est une contrainte qui impose qu’un élément du projet soit terminé avant qu'un autre puisse être commencé. Évaluer les besoins du projet et documenter toutes les dépendances qui ont un impact sur celui-ci. Créer un registre des dépendances/contraintes (ou utiliser un modèle). Ce registre deviendra une ressource importante, non seulement pour la rédaction du cahier des charges, mais aussi pour votre interaction continue avec le projet et la documentation subséquente.
	- Étape 2 : Créer un **registre de toutes les contraintes** de projet
		- Évaluer le projet, faire un brainstorming avec les parties prenantes et documenter toutes les contraintes qui ont un impact sur le projet. Utiliser le registre des dépendances/contraintes pour cataloguer ces contraintes. Si beaucoup de contraintes à documenter, créer deux registres distincts.
	- Étape 3 : Créer un **registre de tous les risques** de projet
		- Si une contrainte sera en fait un problème, l'inscrire dans le registre des risques.
	- Étape 4 : S'assurer que les principales dépendances, contraintes et risques se trouvent dans le document de lancement du projet (ou le CDCF).
		- Les dépendances,contraintes et risques peuvent être répertoriées dans le chapitre *Quels sont les aspects pratiques ?*. Si beaucoup de dépendances/contraintes/risques, lister les principales dans le CDCF puis faire un lien vers le document à part correspondant pour le reste.
	- Étape 5 : Convenir de la façon de surveiller les dépendances et les contraintes
		- Trouver un moyen de surveiller et d'évaluer les dépendances et les contraintes au fur et à mesure que le projet évolue et s'achève, afin que tout impact sur la réussite du projet puisse être rapidement identifié et traité.

- L'importance des contraintes :
	- Les contraintes limitent ou restreignent vos options.
	- Les types de contraintes les plus courants sont ceux qui limitent le temps, les ressources ou le budget.
	- Les contraintes, comme les besoins, doivent être clairement documentés, sinon elles laissent des trous béants dans le projet et peuvent mener à un échec catastrophique de livraison.
	- Une documentation efficace des contraintes vous aide à concevoir une stratégie pour gérer et travailler dans le respect de ces contraintes tout au long du cycle de vie du projet.




- *Exercice* :

		- Améliorer le système existant, ne pas en créer un nouveau
		- Utiliser le code existant
		- Système Web multi applicatif (pilote notre site web, notre boutique en ligne, nos ressources humaines, la gestion de la paie, etc...)
		- Regarder s'il existe déjà une solution existante
		- Back-End construit avec ASP.NET
		- Front-End incluant toutes les pages web, construit avec AngularJS
		- Plusieurs bases de données SQL Server pour toutes nos données
		- Tout fonctionne sur MS Azure
		- Actuellement abonnement premium P2 pour MS Azure
		- Voir s'il faut modifier l'abonnement MS Azure pour les nouvelle fonctionnalités
		- Ajouter une application mobile en plus du navigateur Web sous Android et IOS
		

		## 1. REGISTRE DES CONTRAINTES
		*Limites non négociables qui impactent les choix techniques et l'organisation.*

		| ID | Nature de la Contrainte | Tâche Impactée | Source / Justification | Impact sur le Projet |
		| :--- | :--- | :--- | :--- | :--- |
		| **CON-01** | Développement existant | Langages et architecture de développement | Standardisation IT Client | Respecter les langages et l'architecture existants. |
		| **CON-02** | Langage : ASP.NET | Développement Back-End | Standardisation IT Client | Vérifier si faisable dans ce langage développeur ASP.NET. |
		| **CON-03** | Langage : AngularJS | Développement Front-End | Standardisation IT Client | Vérifier si faisable dans ce langage + développeur AngularJS. |
		| **CON-04** | Langage : SQL Server | Développement bases de données | Standardisation IT Client | Rajouter de nouvelles bases de données et lier avec l'existant |
		| **CON-05** | Multiapplicatif : Site Web + boutiques ligne + RH + paie + ...  |  |  |  |
		| **CON-06** | Environnement : MS Azure |  |  |  |
		| **CON-07** | Abonnement : MS Azure |  |  |  |
		| **CON-08** | Multiplateforme : Web + application Android et IOS |  |  |  |
	
		---
		
		## 2. REGISTRE DES DÉPENDANCES
		*Éléments indispensables (internes ou externes) à la progression du projet.*

		| ID | Tâche Antécédente (La Source) | Tâche Bloquée (La Conséquence) | Responsable | Échéance | Impact |
		| :--- | :--- | :--- | :--- | :--- | :--- |
		| **DEP-01** | Validation du développement Web | Application Androir et IOS | Développeurs | [Date] | **Report global** planning. |
			
		---
				
		## 3. ANALYSE DES RISQUES (AMDEC)
		*Anticipation des menaces. Criticité (C) = Gravité (G) x Probabilité (P) sur 5.*

		| ID | Risque Identifié (Événement) | G | P | C | Tâche Impactée | Plan de Mitigation (Action) |
		| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
		| **RSQ-01** | Développement existant : ne pas réussir à se greffer sur le code existant | 5 | 3 | **15** | Tout le développement | Etudie le code existant |






		
### 2.4 Elaborer un plan de gestion des intervenants
- Chaque projet nécessite la participation d'autres personnes. Les personnes qui contribuent à l'élaboration du projet sont celles qui ont un intérêt dans la réussite du projet.

- La gestion des intervenants est le processus par lequel développer et entretenir des relations de qualité avec les intervenants. Apprendre à communiquer avec chaque intervenant à son niveau est important pour maintenir et renforcer ces relations, accroître leur confiance envers le chef de projet et son équipe, et assurer leur intérêt continu dans la réussite du projet.

- Différents types d'intervenants peuvent être impliqués dans le projet :
	- **Les intervenants externes** comprennent le client, ses gestionnaires et d'autres personnes avec lesquelles il est possible de travailler ;
	- **Les intervenants internes** sont l'équipe de projet, les entrepreneurs ou les fournisseurs que participent au projet, l'équipe de gestion et toute autre personne de l'entreprise qui souhaite la réussite du projet ;
	- **Les parties prenantes élargies** comprennent un grand nombre de personnes très diverses qui peuvent contribuer au projet, qu'il s'agisse de consultants, de testeurs, de clients potentiels ou d'utilisateurs du système, et bien d'autres.

- Apprendre à connaitre les intervenants :
	- Identifier les intervenants pour le projet.
	- Apprendre à les connaître afin d'optimiser au mieux les communications avec eux.
	- Poser des questions précises et être extrêmement honnête en documentant les réponses.
	- Elaborer un plan de gestion et de communication avec eux tout au long du cycle de vie du projet
	- Exemple de questions pour l'élaboration du plan de gestion des intervenants ou PGI :
		- *Quels sont les intervenants qui ont le plus d'influence sur le projet ?*
			- Il s'agira très probablement de membres de l'équipe du client.
		- *Quels intervenants seront les plus touchés par le projet ?*
			- Il s'agira encore une fois de l'équipe du client, mais il peut aussi s'agir de personnes de l'extérieur.
		- *Comment traiter les personnes d'influence qui ne sont pas considérées comme des intervenants, mais qui se considèrent comme importantes pour le projet ?*
			- Ce sont des personnes qui devraient rester à distance lorsqu'il s'agit du projet. Elles peuvent souvent soulever des préoccupations inutiles et créer des obstacles au développement. Bien qu'il soit peut-être nécessaire de les tenir au courant du projet, leur participation n'est pas nécessaire.
		- *Qu'est-ce qui motive et intéresse chaque intervenant par rapport au projet ?*
			- Pour répondre à cette question, vous devrez répondre à quelques autres et faire quelques recherches pour obtenir vos réponses :
				- Qui a un intérêt financier dans le projet ?
				- Qui a un intérêt ou un enjeu affectif ? 
				- Qui sont les principaux soutiens du projet ?
				- Qui sont les principaux détracteurs du projet ?

- Créer un PGI :
	- Un bon PGI peut être quelque chose d'aussi simple qu'une feuille de calcul qui énumère les intervenants et leurs principaux intérêts. Il comprendra certains points de repère clés pour lesquels l'intervenant peut avoir un intérêt particulier, même financier ou affectif.
	- Le PGI ne fait pas partie du cahier des charges fonctionnel, mais il constitue une partie importante des besoins de documentation préliminaire. Il va aider à identifier les intervenants qui pourraient souhaiter voir le cahier des charges mais que vous n'auriez pas envisagés autrement.
	- Comprendre les liens entre certains besoins du projet et les facteurs de motivation de vos intervenants peut aider à prioriser le développement de certains besoins par rapport à d'autres lorsque l'occasion le permet, contribuant ainsi à la satisfaction et à l'enthousiasme des intervenants à l'égard du projet.

- Les avantages d'un PGI :
	- La perspicacité des intervenants peut aider à façonner un projet et propulser vers le succès. Il est important de savoir qui sont ces intervenants afin de ne pas perdre de temps à communiquer et à essayer de travailler avec des gens qui n'ont pas besoin d'être informés de l'avancement du projet. En outre, les intervenants les plus influents peuvent aider à lever les obstacles, à localiser et à obtenir les ressources nécessaires, et même à lever des contraintes. Il est souvent essentiel pour la réussite d'un projet de veiller à ce que ces intervenants soient satisfaits.

- L'importance du PGI :
	- Le PGI est un document distinct qui n'est pas nécessairement lié au cahier des charges fonctionnel, mais qui est essentiel au début de tout projet.
	- Cela signifie apprendre à connaître les parties prenantes afin d'optimiser au mieux les communications avec eux.
	- Un bon PGI peut aider à prioriser certains besoins par rapport à d'autres si nécessaire, ce qui mène à une plus grande satisfaction des intervenants.
	- La perspicacité des intervenants peut aider à façonner le projet et est souvent essentielle à sa réussite.


### Résumé de la partie 2
- Le cahier des charges fonctionnel est l'élément d'information le plus important sur lequel le chef de projet et le client vont s'entendre.

- Un cahier des charges efficace énonce des objectifs clairs et concis (1 ou 2 pages).

- Les objectifs d'un cahier des charges  définissent les critères de réussite du projet :
	- Il existe des méthodes courantes de collecte des besoins : résumé des besoins fonctionnels et non fonctionnels, entretiens avec les clients et les intervenants et observations en temps réel.
	- Les deux questions les plus importantes pour la collecte des besoins constituent également les titres des sections dans le cahier des charges : "Où sommes-nous maintenant ?" et "Où voulons-nous être ?".

- Les besoins fonctionnels décrivent ce qu'un système devrait faire, alors que les besoins non fonctionnels décrivent comment un système fonctionne.

- Les types de contraintes les plus courants sont ceux qui limitent le temps, les ressources, les besoins techniques ou le budget.

- Les contraintes, comme les besoins, doivent être clairement documentés.

- Le PGI est un document distinct qui n'est pas nécessairement lié au cahier des charges fonctionnel, mais qui est essentiel au début de tout projet.

- Un bon PGI peut vous aider à prioriser certains besoins par rapport à d'autres si nécessaire, ce qui mène à une plus grande satisfaction des intervenants.

---

## 🔄 Partie 3 : Méthodologie Agile et Communication
*Notes sur l'adaptation du document dans un cycle itératif...*

### 3.1 Adapter le CDCF en contexte Agile
- Planifier les sprints et rendre les livrables à temps : 
	- Tout comme le développement agile, la documentation agile est composée de sprints, qui sont des cycles de documentation courts dans lesquels il n’y a généralement qu’un seul livrable pour le sprint en question.
	
- Les questions suivantes sont souvent d'une grande valeur dans la planification d'un sprint :
	1. Quel sera l'objectif ? 
		- 1er sprint = Le cahier des charges fonctionnel pour le client afin de faire une proposition du projet.
	2. À quoi ressemblera le livrable ?
		- Répondre à cette question vous aidera à définir le backlog, qui est la liste des tâches qui doivent être accomplies pendant le sprint pour atteindre le but du sprint.
			- Document CDCF :
				- Envoyé pour révision par le lient? : juste le document
				- Présenté au client? : document + diapositives de présentation
			- Document PGI
	3. Qui sera impliqué ? 
		-  Identifier les ressources nécessaires pour exécuter les tâches décrites dans le backlog afin d'atteindre l'objectif.
	4. Qui a besoin du livrable ? 
		- Répondre à cette question permet d'identifier le public cible du livrable.
	5. Le livrable est-il tributaire d'autres livrables ?
			- Permet de définir si d'autres sprints doivent être effectués en premier.
			- Permet d'établir facilement l'ordre dans lequel la documentation doit être écrite.
	6. Quand en a-t-on besoin ?
		- Cette dernière question fixe la date limite pour le sprint.
		- Les délais de sprint sont des jalons à court terme pour le projet et aident à faire avancer le projet à un rythme efficace.
		- La planification de vos sprints de documentation n'a pas besoin d'être difficile, mais elle doit être minutieuse.

- Exemple de CDCF: https://s3-eu-west-1.amazonaws.com/course.oc-static.com/courses/6398026/Exemple+de+cahier+des+charges.pdf

### 3.2 Gérer le "Scope Creep" (Dérive des objectifs)
- Découvrez la dérive des objectifs :
	- Nouvelle demande du client en cours de développeent : 
		- «Pourrions-nous changer la caractéristique X pour qu'elle fasse le comportement Z au lieu du comportement Y ?»
		- « Peut-on ajouter la fonction A ? »
		- « Nous avons besoin de la fonction B dès que possible. »
	- La portée du projet continue de s'étendre lentement et le projet devient de plus en plus vaste.
	- Les changements et les ajouts s'accumulent et commencent à affecter d'autres aspects du projet qui sont déjà terminés, et ils doivent maintenant être refaits...
	- Petites demandes, de minuscules ajustements, qui deviennent graduellement de plus en plus grands.

- Appréhendez le risque de la dérive des objectifs dans un projet agile :
	- Les documents agiles, de par leur nature, sont plus fluides et sont destinés à être facilement modifiés. Ce sont des documents vivants.
	- La tentation avec de tels documents est d'accepter facilement des changements sans tenir dûment compte de leurs implications.
	- L’implication naturelle du client dans un projet agile peut également poser un problème : 
		- Lorsque le client reçoit des livrables régulièrement, les éléments qui nécessitent des changements sont repérés et traités rapidement.
		- Toutefois, cela crée également de nombreuses possibilités de demandes supplémentaires qui dépassent la portée initiale.
	- Pour éviter de faire face à ce genre de situation :
		- Une planification adéquate est essentielle à l'élaboration d'une documentation efficace.
		- L'élaboration d'une documentation efficace est essentielle à la réussite de la planification d'un projet. 	
		- Une bonne planification de projet est essentielle à la réussite de tout projet.
	- Une bonne planification de la documentation est essentielle à la réussite de tout projet.

- Atténuez le risque de dérive des objectifs :
	- Besoin d'un plan pour faire face aux dérives quand elles se produisent.
	- Cahier des charges fonctionnel :
		- Fondement de votre relation et du projet.
		- Doit définir clairement les besoins commerciaux, les livrables attendus et les critères de réussite de ceux-ci.
	- Documenter le plan de gestion des intervenants :
		- Le PGI donnera un aperçu supplémentaire de la gestion de la relation avec le client et, lorsqu'il est associé au cahier des charges fonctionnel, il  peut fournir une protection supplémentaire contre la dérive des objectifs.
	- Documenter un plan de traitement des demandes de modification et de fonctions supplémentaires
		- Avant d'accepter tout changement par rapport à la portée initiale, effectuer des recherches approfondies, documenter le changement et ses implications pour le reste du projet, et présenter vos conclusions au client pour validation.

- La dérive des objectifs : 
	- Commence par de petites demandes, mais peut finalement s'avérer désastreux pour un projet.
	- En ce qui concerne la planification :
		- Une planification adéquate est essentielle à l'élaboration d'une documentation efficace.
		- L'élaboration d'une documentation efficace est essentielle à la réussite de la planification d'un projet.
		- Une bonne planification de projet est essentielle à la réussite de tout projet.
		- Par conséquent, une bonne planification de la documentation est essentielle à la réussite de tout projet.
	- Les meilleurs outils pour atténuer le risque de dérive sont un cahier des charges fonctionnel efficace et un plan de gestion des intervenants bien préparé.	
	
### 3.3 Utiliser des modèles pour la documentation
- Obtenez cohérence, clarté et efficacité grâce à un bon modèle de document :
	- **La cohérence des documents** : tous les documents d'un type particulier provenant de l'entreprise suivront le même modèle et seront facilement reconnaissables.
	- **Une efficacité accrue** : en éliminant le temps consacré au formatage des documents et au contenu commun, le temps consacré à un document particulier est limité aux données propres au client.
	- **Une clarté accrue** : tous les documents utilisent le même contenu commun et un langage commun, ainsi qu'un format uniforme, ce qui améliore la clarté du contenu pour le lecteur.  

- Trouvez de « bons » modèles :
	- Gratuits : De nombreux modèles en ligne peuvent être téléchargés, utilisés et modifiés gratuitement.. Trouver des modèles individuels peut prendre beaucoup de temps, mais c'est souvent une option préférable pour les particuliers ou les petites entreprises ayant un budget serré.
	- Payants : Un bon logiciel de création de modèles peut représenter une importante économie de coûts. La plupart de ces formules sont disponibles par abonnement et par utilisateur. Les frais d'abonnement sont généralement raisonnables et sont largement compensés par les économies réalisées grâce à l'utilisation du logiciel et des modèles associés.
- Modèles de documents individuels
	- MyPM – deux bibliothèques de modèles de documents de haute qualité gratuites.
		- [Modèles de gestion de projet](https://www.mypmllc.com/project-management-resources/free-project-management-templates/)
		- [Modèles de gestion des propositions](https://www.mypmllc.com/project-management-resources/proposal-management-templates/)
	- [Institut de gestion de projet (PMI)](https://www.pmi.org/learning/tools-templates)
	- [ProjectManagement.com](https://www.projectmanagement.com/)

- Logiciels
	- [Smartsheet](https://www.smartsheet.com/)
	- [SmoothDocs](http://smoothdocs.com/)
	- [Templafy](https://www.templafy.com/)

- L'importance d'un modèle de document :
	- L'utilisation d'un modèle de document peut améliorer la cohérence, l'efficacité et la clarté.
	- Les ressources en ligne pour les modèles de documents sont abondantes, mais il faut faire quelques recherches pour trouver les meilleures options.
	- Les modèles de documents individuels sont une excellente option pour les utilisateurs particuliers ou les petites entreprises ayant un budget limité.
	- Les logiciels de gestion de la documentation et/ou de création de modèles sont une bonne solution pour les grandes entreprises ou les particuliers qui créent une grande variété de documents sur une base régulière.


### Résumé de la partie 3
- Importance sur la sur la rédaction de cahier des charges fonctionnels efficaces à l'intention des clients.

- Documentation agile composée d'une série de documents réalisés pendant les différents sprints du projet.

- Les documents que nous utilisons pour planifier et réaliser le développement d'un projet ne sont pas le projet lui-même, et ils ne sont ni le bon ni le mauvais choix pour la documentation. C'est la qualité de la documentation qui compte.

- Utiliser une série de cahiers des charges pour la documentation du projet :
	- Permet de garder le développement du projet sur la bonne voie, bien mieux qu'un SRS.
	- Les cahiers des charges offrent un niveau de partitionnement que l'on obtient tout simplement pas avec les gros documents. 

---

## 💡 Mes Réflexions "Data Architect"
- C'est compliqué de bien comprendre comment remplir tous les documents comme il faut.
- Ca serait bien de pouvoir avoir un mentor sur ce sujet.

## ❓ Points à approfondir / Questions
- [ ] Etudier des CDCF déjà existants pour avoir une meilleur idée.
- [ ] Dois-je passer par un logiciel de gestion de projet?