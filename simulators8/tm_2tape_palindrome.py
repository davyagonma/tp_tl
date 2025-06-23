# tm_2tape_palindrome.py
def run(w):
    trace = []
    if "#" not in w:
        return False, ["Erreur : # manquant"]
    
    left, right = w.split("#")
    
    # Initialisation des rubans
    tape1 = list(w)  # Ruban d'entrée
    tape2 = list(left)  # Ruban de mémorisation
    pos1 = 0  # Position tête ruban 1
    pos2 = 0  # Position tête ruban 2
    
    trace.append(f"Initialisation:")
    trace.append(f"Ruban 1: {''.join(tape1)} (position {pos1})")
    trace.append(f"Ruban 2: {''.join(tape2)} (position {pos2})")
    trace.append("---")
    
    # Phase 1: Copie avant # sur ruban 2
    while pos1 < len(tape1) and tape1[pos1] != '#':
        trace.append(f"Étape {len(trace)}: Copie '{tape1[pos1]}' du ruban 1 au ruban 2")
        tape2[pos2] = tape1[pos1]
        pos1 += 1
        pos2 += 1
        trace.append(f"Ruban 1: {''.join(tape1)} (position {pos1})")
        trace.append(f"Ruban 2: {''.join(tape2)} (position {pos2})")
        trace.append("---")
    
    pos1 += 1  # Passer le #
    pos2 = 0  # Retour au début du ruban 2
    
    # Phase 2: Comparaison
    result = True
    while pos1 < len(tape1) and pos2 < len(tape2):
        trace.append(f"Étape {len(trace)}: Comparaison '{tape1[pos1]}' (ruban1) et '{tape2[pos2]}' (ruban2)")
        if tape1[pos1] != tape2[pos2]:
            result = False
            break
        pos1 += 1
        pos2 += 1
        trace.append(f"Ruban 1: {''.join(tape1)} (position {pos1})")
        trace.append(f"Ruban 2: {''.join(tape2)} (position {pos2})")
        trace.append("---")
    
    # Vérification longueurs égales
    if pos1 < len(tape1) or pos2 < len(tape2):
        result = False
    
    return result, trace