def getGranularityTree(B_Granules: pd.DataFrame, info_table: pd.DataFrame, max_depth: int):
    """
    Construit un arbre de granularité complet à partir d'une table de granules (B_Granules) 
    et de la table d'information (info_table), jusqu'à une profondeur maximale max_depth.
    
    Pour chaque branche, on traite d'abord les granules déterminatives (Entropy == 0)
    en ajoutant un nœud pour chacune. Pour les granules indéterminées, on crée un nœud
    indéterminé pour chaque granule couvrant au moins un objet restant, et on les ajoute
    à une file d'attente pour traitement ultérieur.
    
    Lorsque la profondeur maximale est atteinte ou qu'aucune granule ne couvre davantage d'objets,
    le nœud final se voit attribuer une probabilité d'état calculée comme la moyenne pondérée
    de confidence_1 par coverage_1.
    """
    from bigtree import Node
    import pandas as pd

    # Fonction utilitaire de calcul de l'index de Jaccard entre une granule et un ensemble d'objets
    def jaccard_index(granule, remaining_objects):
        set_granule = set(granule)
        if not set_granule or not remaining_objects:
            return 0
        return len(set_granule.intersection(remaining_objects)) / len(set_granule.union(remaining_objects))
    
    # Fonction pour calculer la probabilité d'état à partir d'un DataFrame de granules
    def compute_probability_state(df):
        num, den = 0, 0
        for _, row in df.iterrows():
            num += row['confidence_1'] * row['coverage_1']
            den += row['coverage_1']
        return num / den if den > 0 else 0

    # Création de la racine
    root = Node('Root')
    
    # Chaque élément de pending est un tuple : (noeud_parent, B_Granules_local, remaining_objects_local, depth)
    pending = [(root, B_Granules.copy(), set(info_table.index), 0)]
    
    while pending:
        current_node, current_B, remaining_objects, depth = pending.pop(0)
        
        # Si la profondeur maximale est atteinte, on calcule la probabilité d'état
        if depth >= max_depth:
            prob_state = compute_probability_state(current_B)
            current_node.name = current_node.name + f"\nProbabilité d'état = {prob_state:.3f}"
            continue
        
        # Tant qu'il reste des objets à couvrir et des granules disponibles
        while remaining_objects and not current_B.empty:
            # Sélection des granules déterminatives (Entropy == 0)
            det_mask = current_B['Entropy'] == 0
            det_formulas = current_B.loc[det_mask, 'Formula']
            
            if not det_formulas.empty:
                for idx, formule in det_formulas.items():
                    # Définition de la classe selon confidence_1 (ici, 1 si égale à 1, sinon 0)
                    class_val = 1 if current_B.loc[idx, 'confidence_1'] == 1 else 0
                    Node(f"{formule}\nClass = {class_val}", parent=current_node)
                    # Mise à jour des objets couverts
                    granule_objs = set(current_B.loc[idx, 'Granule'])
                    remaining_objects -= granule_objs
                # Retrait des granules déterminatives du DataFrame pour cette branche
                current_B = current_B[~det_mask]
                # Puis, on continue à traiter tant qu'il reste des objets non couverts
                continue
            
            # Mise à jour des métriques pour la branche
            getGenerality(current_B, info_table)
            getConfidence(current_B, info_table)
            getCoverage(current_B, info_table)
            getEntropy(current_B, info_table)
            
            # Calcul de l'index de Jaccard pour chaque granule par rapport aux objets restants
            current_B = current_B.copy()  # éviter le SettingWithCopyWarning
            current_B['jaccard'] = current_B['Granule'].apply(lambda g: jaccard_index(g, remaining_objects))
            
            # Tri des granules par ordre décroissant de couverture (jaccard)
            sorted_B = current_B.sort_values(by='jaccard', ascending=False)
            
            # Création de nœuds indéterminés pour chaque granule qui couvre au moins un objet restant
            added_child = False
            for idx, row in sorted_B.iterrows():
                if row['jaccard'] > 0:
                    new_child = Node(f"{row['Formula']}\nNoeud indéterminé", parent=current_node)
                    branch_remaining = remaining_objects - set(row['Granule'])
                    branch_B = current_B.drop(idx)
                    pending.append((new_child, branch_B, branch_remaining, depth + 1))
                    added_child = True
            
            # Si aucun nœud indéterminé n'a été ajouté, on considère le nœud actuel comme final et on calcule sa probabilité d'état
            if not added_child:
                prob_state = compute_probability_state(current_B)
                current_node.name = current_node.name + f"\nProbabilité d'état = {prob_state:.3f}"
                break
            # On passe au prochain élément de la file d'attente pour poursuivre l'exploration
            break
    return root
