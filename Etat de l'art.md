# État de l'art : Utilisation de l'intelligence artificielle pour détecter les erreurs de prescription

## Introduction

La prévention des erreurs de prescription est une priorité majeure dans les soins de santé, tant pour garantir la sécurité des patients que pour réduire les coûts liés aux événements indésirables. Ces erreurs incluent des dosages incorrects, des interactions médicamenteuses toxiques et des administrations inadéquates. Selon des études, la prévalence des erreurs de prescription varie entre 6 % et 10 % des patients hospitalisés, avec des conséquences graves pour leur santé et des coûts économiques significatifs (Ouzar et al., 2024; Ben Othman et al., 2023). La réduction de ces erreurs est donc essentielle pour améliorer les résultats des soins tout en optimisant les ressources disponibles.

Avec l’émergence des dossiers médicaux électroniques et des bases de données massives telles que MIMIC-III et MIMIC-IV, l'intelligence artificielle (IA) offre des opportunités uniques pour détecter et prévenir ces erreurs. En exploitant des méthodes avancées de traitement de données et de modélisation, les outils basés sur l’IA ont montré leur potentiel pour résoudre des problématiques complexes liées à la sécurité des patients. Cet état de l'art explore les approches actuelles, les outils disponibles et les perspectives futures pour l’utilisation de l’IA dans ce domaine critique.

## Typologie des erreurs de prescription

#### Nature des erreurs

Les erreurs de prescription peuvent survenir à différents niveaux du processus médical. Elles incluent des erreurs de dosage, des routes d'administration inappropriées, des interactions médicamenteuses non identifiées, ainsi que des omissions dans les indications. Par exemple, une étude a révélé que 42,9 % des erreurs concernent la route d'administration, tandis que 28,6 % impliquent une fréquence incorrecte de dosage (Ouzar et al., 2024). Ces erreurs peuvent être aggravées par des facteurs tels que la charge de travail des professionnels de santé ou le manque de standardisation des protocoles (Unknown Author, 2022).

D'autres erreurs comprennent des incompatibilités biologiques non détectées, par exemple une interaction toxique avec des médicaments déjà pris par le patient. Ces situations mettent en évidence la complexité des décisions cliniques et l’importance d’intégrer des systèmes d’assistance automatisés.

#### Impact clinique et économique

L’iatrogénie médicamenteuse est une des conséquences majeures des erreurs de prescription. Elle représente une charge importante pour les systèmes de santé, causant 3,5 % des décès hospitaliers. En outre, elle entraîne une augmentation des durées d’hospitalisation et des coûts associés. Une étude française a révélé que 51,2 % des réactions indésirables graves pourraient être évitées grâce à une meilleure prévention (Unknown Author, 2022).

Les conséquences économiques ne sont pas moins importantes. Une mauvaise gestion des prescriptions peut entraîner des litiges légaux, des pertes de ressources humaines et matérielles, ainsi que des atteintes à la réputation des établissements de santé.

## Outils actuels pour la détection des erreurs

#### Systèmes basés sur les règles

Les systèmes d'aide à la décision clinique (CDSS) reposent sur des règles d’expert pour analyser les prescriptions. Ces règles sont souvent dérivées des lignes directrices cliniques et des connaissances médicales accumulées. Ces systèmes permettent de détecter des erreurs prédéfinies, comme un dosage non conforme aux recommandations ou des interactions médicamenteuses connues. Cependant, ils souffrent de limitations importantes : rigidité des règles, incapacité à s’adapter à de nouvelles situations et fatigue des alertes due à un excès de notifications (Ben Othman et al., 2023).

#### Méthodes basées sur les données

Les approches d'apprentissage automatique (Machine Learning, ML) permettent de détecter des modèles complexes dans les données sans nécessiter de règles explicites. Par exemple, des modèles supervisés tels que Random Forest et XGBoost ont atteint une précision de 99,4 % dans la classification des prescriptions valides et invalides (Unknown Author, 2022). Ces méthodes offrent une plus grande flexibilité et une capacité à s’adapter aux nouvelles données. Cependant, elles nécessitent des ensembles de données bien étiquetés et suffisamment équilibrés.

En outre, les systèmes d'apprentissage profond (Deep Learning) ont récemment émergé comme des outils puissants pour capturer des relations complexes. Ils permettent d’analyser des ensembles de données volumineux et variés, comme des dossiers médicaux et des images radiologiques.

## Intelligence artificielle appliquée à la détection des erreurs

#### Méthodes supervisées

Les algorithmes supervisés, comme XGBoost et Random Forest, ont démontré leur efficacité en exploitant des prescriptions validées ainsi que des données synthétiques représentant des erreurs potentielles. Les résultats montrent une excellente performance avec des scores F1 supérieurs à 0,99 (Unknown Author, 2022). Ces modèles apprennent à partir de données préalablement étiquetées pour distinguer les prescriptions correctes des anomalies.

#### Méthodes non supervisées

La classification à une seule classe (One-Class Classification) est adaptée pour des contextes où seules des données valides sont disponibles. Les techniques comme le Local Outlier Factor et les machines à vecteurs de support (SVM) permettent de détecter des anomalies avec une précision et un rappel élevés (Ouzar et al., 2024). Cette approche est particulièrement utile dans les contextes où les exemples d'erreurs sont rares ou difficiles à collecter.

#### Explicabilité et confiance

Pour améliorer l’adoption par les cliniciens, l’intégration d’outils d’explicabilité tels que SHAP (Shapley Additive Explanations) aide à interpréter les prédictions des modèles. Ces outils fournissent des visualisations des facteurs déterminants dans les décisions des modèles, renforçant ainsi la confiance des utilisateurs dans les systèmes basés sur l'IA.

## Études de cas et applications

#### Projets spécifiques

Au CHU de Lille, des systèmes basés sur l’IA ont été déployés pour analyser les prescriptions en tenant compte des données biologiques des patients et des interactions médicamenteuses potentielles. Ces outils combinent le clustering pour la classification initiale et le ML pour affiner les résultats (Ben Othman et al., 2023). Ces efforts illustrent la valeur de collaborations interdisciplinaires pour concevoir des solutions adaptées aux besoins cliniques.

#### Données synthétiques

Pour pallier le déséquilibre des données, des prescriptions synthétiques contenant des erreurs ont été générées. Ces données ont permis de tester et de valider les modèles, assurant une robustesse face à divers scénarios cliniques (Ben Othman et al., 2023). Cette stratégie est essentielle pour évaluer les performances des modèles dans des environnements contrôlés.

## Défis et perspectives

#### Défis techniques

Les systèmes déjà en place rencontrent des obstacles tels que la gestion des données manquantes, la normalisation des unités de mesure et la validation clinique des modèles. Les approches actuelles basées sur le clustering sont limitées par des calculs de distances qui ne reflètent pas toujours la complexité des données cliniques (Unknown Author, 2022).

#### Perspectives futures

Une intégration plus poussée de connaissances pharmacologiques dans les modèles d’IA, combinée à des approches hybrides mélangeant expertise humaine et automatisation, promet d’améliorer la précision et la portée des systèmes (Unknown Author, 2022). La formation continue des professionnels de santé pour utiliser ces systèmes est également cruciale pour leur succès.

## Conclusion

L’intelligence artificielle offre des solutions prometteuses pour réduire les erreurs de prescription et améliorer la sécurité des patients. Bien que des défis subsistent, les avancées technologiques et les collaborations interdisciplinaires ouvriront de nouvelles perspectives pour une adoption plus large et plus efficace dans le domaine clinique. En intégrant des outils d’IA adaptés et en encourageant une adoption collaborative, les systèmes de santé peuvent évoluer vers une pratique médicale plus sécurisée et efficace.

## Bibliographie

Ouzar Y., Ajmi F., Ben Othman S., et al. (2024). "Interpretable One-Class Classification Framework for Prescription Error Detection Using BERT Embeddings and Dimensionality Reduction". International Journal of Medical Informatics.

Ben Othman S., Decaudin B., Odou P., et al. (2023). "Artificial Intelligence to Analyze and Limit Drug-Related Problems in Hospitals". Medinfo 2023 Proceedings.

Unknown Author, (2022). "A Clinical Support System Analyzing Drug Prescriptions Based on AI, in Order to Limit Drug Iatrogeny in Hospitals".


