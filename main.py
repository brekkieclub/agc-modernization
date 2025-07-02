# Step 1: Basic Instruction Set (Mocked)
def load_instruction(code):
    return {"opcode": code, "exec": lambda: print(f"Executing {code}")}

# Step 2: Simple Memory Model
memory = [0] * 1024

# Step 3: Instruction Decoder (Mocked)
def decode_instruction(address):
    opcode = memory[address]
    return load_instruction(opcode)

if __name__ == "__main__":
    memory[0] = "TC"
    instr = decode_instruction(0)
    instr["exec"]()
