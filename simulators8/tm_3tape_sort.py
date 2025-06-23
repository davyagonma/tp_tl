# tm_3tape_sort.py
def run(input_str):
    try:
        numbers = list(map(int, input_str.strip().split()))
    except:
        return [], ["Erreur: Entrez des nombres séparés par des espaces (ex: '5 2 7 1')"]

    trace = []
    
    # Initialisation des rubans
    tape1 = numbers.copy()  # Entrée
    tape2 = []              # Zone de travail
    tape3 = []              # Sortie triée
    
    trace.append("Initialisation:")
    trace.append(f"Ruban 1 (entrée): {tape1}")
    trace.append(f"Ruban 2 (travail): {tape2}")
    trace.append(f"Ruban 3 (sortie): {tape3}")
    trace.append("---")
    
    # Algorithme de tri par sélection
    while tape1:
        # Trouver le minimum dans tape1
        min_val = min(tape1)
        trace.append(f"Trouver le minimum: {min_val}")
        
        # Déplacer tous les éléments vers tape2 sauf le minimum
        tape2 = []
        found_min = False
        for num in tape1:
            if num == min_val and not found_min:
                tape3.append(num)
                found_min = True
                trace.append(f"Déplacer {num} vers ruban 3 (sortie)")
            else:
                tape2.append(num)
                trace.append(f"Déplacer {num} vers ruban 2 (travail)")
        
        tape1, tape2 = tape2, []
        
        trace.append(f"État après cette itération:")
        trace.append(f"Ruban 1: {tape1}")
        trace.append(f"Ruban 2: {tape2}")
        trace.append(f"Ruban 3: {tape3}")
        trace.append("---")
    
    return tape3, trace