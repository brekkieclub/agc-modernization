class AGC:
    def __init__(self):
        self.memory = [0] * 4096  # 12-bit address space
        self.PC = 0               # Program counter
        self.A = 0                # Accumulator
        self.running = True

    def fetch(self):
        instr = self.memory[self.PC]
        self.PC = (self.PC + 1) & 0xFFF
        return instr

    def decode_execute(self, instr):
        opcode = (instr >> 12) & 0xF
        address = instr & 0xFFF

        print(f"[AGC] Cycle: PC={self.PC - 1:04o} Executing {instr:05o}")

        if instr == 0o00000:
            self.running = False
            return True

        # Minimal opcode demo:
        if opcode == 0o0:
            print("[AGC] NOP or unrecognized no-op")
        elif opcode == 0o1:
            print("[AGC] Opcode 001 - Not yet implemented")
        else:
            print(f"[AGC] Unknown opcode {opcode:03o}, skipping.")

        return False

    def cycle(self):
        if not self.running:
            return True
        instr = self.fetch()
        return self.decode_execute(instr)
