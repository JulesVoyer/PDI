def getGranularityTree(B_Granules: pd.DataFrame, info_table: pd.DataFrame):
    """
    Construit un arbre de granularité complet à partir d'une table de granules (B_Granules) 
    et de la table d'information (info_table).
    
    Pour chaque branche, on traite d'abord les granules déterminatives (Entropy == 0) en
    ajoutant un nœud par formule déterminative. Ensuite, pour les granules indéterminées, on
    crée un nœud indéterminé pour chacune (lorsque l'index de Jaccard par rapport aux objets
    restant est > 0) et on ajoute chacune de ces branches à une file d'attente pour traitement.
    """
    from bigtree import Node
    import pandas as pd

    # Fonction utilitaire de calcul de l'index de Jaccard entre une granule et un ensemble d'objets
    def jaccard_index(granule, remaining_objects):
        set_granule = set(granule)
        if not set_granule or not remaining_objects:
            return 0
        return len(set_granule.intersection(remaining_objects)) / len(set_granule.union(remaining_objects))

    # On part d'une racine unique
    root = Node('Root')
    
    # Chaque élément de pending est un tuple : (noeud_parent, B_Granules_local, remaining_objects_local)
    pending = [(root, B_Granules.copy(), set(info_table.index))]
    
    while pending:
        current_node, current_B, remaining_objects = pending.pop(0)
        
        # Tant qu'il reste des objets à couvrir et des granules dans ce sous-problème
        while remaining_objects and not current_B.empty:
            # Sélection des granules déterminatives (Entropy == 0)
            det_mask = current_B['Entropy'] == 0
            det_formulas = current_B.loc[det_mask, 'Formula']
            
            # S'il y a au moins une formule déterminative, on l'ajoute comme enfant
            if not det_formulas.empty:
                for idx, formule in det_formulas.iteritems():
                    # On définit la classe selon la confiance (ici, on considère confidence_1 == 1 comme classe 1)
                    class_val = 1 if current_B.loc[idx, 'confidence_1'] == 1 else 0
                    Node(f"{formule}\nClass = {class_val}", parent=current_node)
                    # Mise à jour des objets couverts
                    granule_objs = set(current_B.loc[idx, 'Granule'])
                    remaining_objects -= granule_objs
                # On retire ces lignes déterminatives du DataFrame pour la branche courante
                current_B = current_B[~det_mask]
                # Puis on continue à traiter tant qu'il reste des objets non couverts
                continue

            # Mise à jour des métriques pour la branche (les fonctions modifient current_B in place)
            getGenerality(current_B, info_table)
            getConfidence(current_B, info_table)
            getCoverage(current_B, info_table)
            getEntropy(current_B, info_table)
            
            # Calcul de l'index de Jaccard pour chaque granule par rapport aux objets restants
            current_B = current_B.copy()  # pour éviter le SettingWithCopyWarning
            current_B['jaccard'] = current_B['Granule'].apply(lambda g: jaccard_index(g, remaining_objects))
            
            # On trie les granules par jaccard décroissant pour privilégier celles qui couvrent le plus d'objets restants
            sorted_B = current_B.sort_values(by='jaccard', ascending=False)
            
            # Pour chaque granule ayant un index > 0, on crée un nœud indéterminé
            added_child = False
            for idx, row in sorted_B.iterrows():
                if row['jaccard'] > 0:
                    new_child = Node(f"{row['Formula']}\nNoeud indéterminé", parent=current_node)
                    # Mise à jour des objets restants pour la branche enfant : on retire ceux couverts par cette granule
                    branch_remaining = remaining_objects - set(row['Granule'])
                    # La branche enfant hérite de toutes les granules restantes sauf celle traitée ici
                    branch_B = current_B.drop(idx)
                    pending.append((new_child, branch_B, branch_remaining))
                    added_child = True
            # Si aucun nœud indéterminé n'a été ajouté (aucune granule ne couvre d'objet restant), on sort de la boucle
            if not added_child:
                break
            # On sort de la boucle de la branche actuelle pour passer à la suivante dans la file
            break
    return root