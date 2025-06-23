class UniversalTuringMachine:
    def __init__(self, transition_code: str, input_code: str, accept_states=['111']):
        self.transitions = self.parse_transitions(transition_code)
        self.tape = self.decode_input(input_code)
        self.state = '1'  # initial state q0 = 1
        self.head = 0
        self.blank = 'B'
        self.accept_states = accept_states

    def decode_unary(self, code):
        return len(code)

    def parse_transitions(self, code: str):
        transitions = {}
        for raw in code.split('000'):
            if not raw.strip():
                continue
            parts = raw.split('0')
            if len(parts) != 5:
                raise ValueError(f"Bad transition: {raw}")
            q, sym, p, new_sym, move = parts
            key = (q, sym)
            value = (p, new_sym, 'R' if move == '1' else 'L')
            transitions[key] = value
        return transitions

    def decode_input(self, code: str):
        parts = code.split('0')
        return parts if parts else []

    def step(self):
        if self.head < 0:
            self.tape.insert(0, self.blank)
            self.head = 0
        elif self.head >= len(self.tape):
            self.tape.append(self.blank)

        current_sym = self.tape[self.head]
        key = (self.state, current_sym)
        if key not in self.transitions:
            return False  # No rule → halt
        next_state, write_sym, direction = self.transitions[key]
        self.tape[self.head] = write_sym
        self.state = next_state
        self.head += 1 if direction == 'R' else -1
        return True

    def run(self, max_steps=1000):
        for _ in range(max_steps):
            if self.state in self.accept_states:
                return True
            if not self.step():
                return False
        return False  # timeout

    def print_tape(self):
        tape_str = ''.join(self.tape)
        head_marker = ' ' * self.head + '^'
        print(tape_str)
        print(head_marker)
