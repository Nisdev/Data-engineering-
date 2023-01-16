
## Structure du projet

### **Folders :**

**Biobert NER :** This folder contains two implemented models allowing the recognition of named entities and the dataset in format csv that was used to train the models 

**Corpus :** Contains a description on tha data used as well as how it was seperated into train and test sets

**Data :** Contains the clinical notes in format .txt and their annotations in format .ann ( this folder was used to create a compatible dataset to be used during the extraction relation step )

**Kg_construction :** This folder contains a notebook that allows to generate the triplets (node_source, relation_label, node_target) the output is the csv file named triplets_kg. it also contains another notebook allowing the construction of the graph in neo4j based on the triplets already generated.

**projet_git :** it contains the models implemented to extract the relations between the entities. Train_aug.txt and pre_test.txt are the files used to train and evaluate the models in order to choose the best one. There is another notebook that allows to increase the text, we applied text augmentation on training set in order to allow the model to learn more the relation labels that occurs less.

### **Python files :**

**Kg_contruction_triplets.py**: this code was generated automatically from the notebook "kg_construction_triplets.ipynb" which exists in the kg_construction folder. Its generation was done to create a docker from the main branch.

**main.py :** An API created using Flask in order to run the model in a back-end as it's linked to the folder **templates**, we had the idea to add a feature that will allow the display of grammatical labels of the words contained in any paragraph entered. Since grammatical labels of words are needed in the named entity recognition task. 

## Simulation d’un projet réel :

Les hôpitaux génèrent une quantité massive des données cliniques, cette formidable augmentation de la quantité de données disponibles rend désormais presque impossible pour les médecins ou les patients de comprendre correctement et d'extraire de nouvelles connaissances sans aide, a cet égard le fait d’extraire d’une manière efficace des nouvelles connaissances à partir de ces données représente une tâche fastidieuse et qui consomme beaucoup de temps pour les médecines et les patients pour trouver l’information pertinente ou la connaissance dont ils ont besoin.

 **Comment peut-on faire usage des techniques de l’intelligence artificielle afin de construire une solution qui permettra aux médecins d’organiser, gérer et utiliser d’énormes quantités d’informations dans le domaine médicale, sans perdre de temps ni d’efforts fourni durant l’extraction manuelle des données à partir des sources diverses, et qui va leur faciliter la prise de décision concernant la détection de différents types de maladies chez les patients ?**
 
Ceci nous pousse à réfléchir à des méthodes récentes et efficaces pour créer des représentations de connaissances dans un format qui nous permet de naviguer entre les données afin de soutenir la recherche contextuelle d’information dans le domaine biomédical. A cet égard on évoque les graphes de connaissance, celles-ci nous permettent de mieux traiter des concepts biomédical abstraits tels que les relations et les interactions entre les entités médicales (Linked Data). De même Ils offrent également un moyen intuitif et visuel de réfléchir à ces concepts.
Encore ils peuvent résoudre des problèmes de recherche des connaissances qui sont plus complexes en les simplifiant en des représentations plus simples ou en transformant les problèmes en des représentations selon différentes perspectives.

## Objectifs
L’objectif principale du travail est de construire un graphe de connaissances dans le domaine médicale à partir duquel les médecins pourront récupérer et utiliser des informations pour prendre une décision concernant les maladies.
 Plus précisément, il va falloir créer des triplets sémantiques sur un ensemble de notes cliniques, en utilisant des approches d’apprentissage en profondeur afin d’extraire les relations possibles. Une fois le Knowledge Graph est créé, les médecins pourront l’interroger en des requêtes et à trouver des interactions entre les différents types de maladies ainsi que d’obtenir rapidement les informations nécessaires contre une maladie précise.
On peut diviser l’objectif principale de ce travail en six points directifs (fonctionnalités) :
1.	Prétraitement des données pour la tâche NER
2.	Produire un modèle permettant d’extraire les entités à partir du corpus 
3.	Prétraitement des données pour la tâche d’Extraction des relations 
4.	Produire un algorithme d’extraction de relations qui va permettre la bonne prédiction des relations entre différentes entités spécifiques déjà extraites. 
5.	 Construction du Knowledge Graph en tenant compte des entités et des relations obtenues.

La fonctionnalité que nous avons développé vers la fin concerne l’implémentation d’une api avec le framework Flask dans laquelle les médecins pourront facilement visualiser et avoir une idée sur les POS tags des entités qui existent dans une note clinique. 


