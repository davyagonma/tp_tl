class MultiTapeTuringMachine:
    def _init_(self, k, transitions, start_state='q0', accept_states=None):
        self.k = k
        self.transitions = transitions  # dict: {(state, sym1,...,symk): (new_state, [newsym], [dir])}
        self.state = start_state
        self.accept_states = accept_states or ['q_accept']
        self.tapes = [['B'] for _ in range(k)]
        self.heads = [0 for _ in range(k)]
        self.trace = []

    def initialize_tape(self, tape_index, content):
        self.tapes[tape_index] = list(content) if isinstance(content, str) else content
        self.heads[tape_index] = 0

    def step(self):
        current_syms = tuple(
            self.tapes[i][self.heads[i]] if 0 <= self.heads[i] < len(self.tapes[i]) else 'B'
            for i in range(self.k)
        )
        key = (self.state,) + current_syms
        if key not in self.transitions:
            return False  # No valid transition

        new_state, new_syms, directions = self.transitions[key]

        for i in range(self.k):
            if 0 <= self.heads[i] < len(self.tapes[i]):
                self.tapes[i][self.heads[i]] = new_syms[i]
            else:
                self.tapes[i].append(new_syms[i])

            if directions[i] == 'R':
                self.heads[i] += 1
                if self.heads[i] >= len(self.tapes[i]):
                    self.tapes[i].append('B')
            elif directions[i] == 'L':
                self.heads[i] = max(0, self.heads[i] - 1)

        self.state = new_state
        self.trace.append(self.snapshot())
        return True

    def run(self, max_steps=1000):
        self.trace.append(self.snapshot())
        for _ in range(max_steps):
            if self.state in self.accept_states:
                return True
            if not self.step():
                return False
        return False

    def snapshot(self):
        return f"{self.state} | " + " || ".join(
            "".join(self.tapes[i])[:30] + f" (H{self.heads[i]})" for i in range(self.k)
        )