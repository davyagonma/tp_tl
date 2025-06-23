from collections import deque  # N'oubliez pas cet import !
import time

class NondeterministicTuringMachine:
    def __init__(self, transitions, start_state='q0', accept_states=None):
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = set(accept_states or ['q_accept'])
        self.max_steps = 1000
        self.paths_explored = 0

    def simulate(self, input_tape):
        # Validation de l'entrée
        if input_tape is None:
            input_tape = ''  # ou raise ValueError("Input tape cannot be None")
        
        # Initialisation sécurisée de la queue
        initial_config = (
            self.start_state,
            list(input_tape),  # Convertit en liste
            0,                # Position initiale de la tête
            []                # Trace initiale vide
        )
        queue = deque([initial_config])  # Création du deque
        
        self.paths_explored = 0
        accepted_paths = []
        
        while queue and self.paths_explored < self.max_steps:
            state, tape, head, path = queue.popleft()
            self.paths_explored += 1
            
            # Vérification d'acceptation
            if state in self.accept_states:
                accepted_paths.append(path + [self._config(state, tape, head)])
                continue

            # Gestion des limites du ruban
            if head < 0:
                tape.insert(0, '_')
                head = 0
            elif head >= len(tape):
                tape.append('_')

            # Application des transitions
            current_symbol = tape[head]
            for new_state, write_sym, direction in self.transitions.get((state, current_symbol), []):
                new_tape = tape.copy()
                new_tape[head] = write_sym
                new_head = head + (1 if direction == 'R' else -1)
                new_path = path + [self._config(state, tape, head)]
                queue.append((new_state, new_tape, new_head, new_path))
        
        return {
            'accepted_paths': accepted_paths,
            'paths_explored': self.paths_explored,
            'timeout': len(queue) > 0
        }

    def _config(self, state, tape, head):
        """Formatage sécurisé de la configuration"""
        symbol = tape[head] if 0 <= head < len(tape) else '_'
        left = ''.join(tape[:head]) 
        right = ''.join(tape[head+1:])
        return f"{state}|{left}[{symbol}]{right}"

class DeterministicTuringMachine:
    def __init__(self, transitions, start_state='q0', accept_states=None):
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = set(accept_states or ['q_accept'])
        
    def simulate(self, input_tape):
        tape = list(input_tape)
        state = self.start_state
        head = 0
        path = []
        
        for _ in range(1000):
            # Configuration actuelle
            path.append(self._config(state, tape, head))
            
            if state in self.accept_states:
                return {'path': path}
                
            # Gestion des limites
            if head < 0:
                tape.insert(0, '_')
                head = 0
            elif head >= len(tape):
                tape.append('_')
                
            current_symbol = tape[head]
            transition = self.transitions.get((state, current_symbol))
            
            if not transition:
                return {'path': path, 'error': 'No transition'}
                
            state, write_sym, direction = transition
            tape[head] = write_sym
            head += 1 if direction == 'R' else -1
            
        return {'timeout': True, 'path': path}
    
    def _config(self, state, tape, head):
        # Gestion sécurisée des index
        symbol = tape[head] if 0 <= head < len(tape) else '_'
        left = ''.join(tape[:head]) if head > 0 else ''
        right = ''.join(tape[head+1:]) if head+1 < len(tape) else ''
        return f"{state}|{left}[{symbol}]{right}"