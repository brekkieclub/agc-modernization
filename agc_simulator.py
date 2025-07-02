# agc_modernized_fixed/agc_simulator.py

class AGCSimulator:
    def __init__(self, program=None):
        self.memory = [0] * 0o4000  # AGC had 4K words of memory (octal 4000 = 2048 decimal)
        self.PC = 0  # Program Counter
        self.running = True

        if program:
            for i, word in enumerate(program):
                self.memory[i] = word

    def fetch(self):
        return self.memory[self.PC]

    def decode_execute(self, instruction):
        opcode = (instruction >> 9) & 0o77  # Extract opcode (top 6 bits)
        address = instruction & 0o777  # Bottom 9 bits is address

        if instruction == 0o00000:
            print(f"[AGC] HALT at PC={self.PC:04o}")
            self.running = False

        elif opcode == 0o20:  # TC - Transfer Control
            print(f"[AGC] TC {address:04o} - Jumping to {address:04o}")
            self.PC = address - 1  # -1 because we'll increment PC after
        else:
            print(f"[AGC] Unknown opcode {opcode:03o}, skipping.")

    def step(self):
        instruction = self.fetch()
        print(f"[AGC] Cycle: PC={self.PC:04o} Executing {instruction:05o}")
        self.decode_execute(instruction)
        self.PC = (self.PC + 1) % len(self.memory)

    def run(self, max_cycles=100):
        cycle = 0
        while self.running and cycle < max_cycles:
            self.step()
            cycle += 1
