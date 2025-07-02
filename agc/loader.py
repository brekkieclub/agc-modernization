def load_agc_memory(agc, filename):
    try:
        with open(filename, 'r') as f:
            for line in f:
                if line.strip() and not line.startswith('#'):
                    parts = line.strip().split()
                    if len(parts) == 2:
                        address = int(parts[0], 8)
                        value = int(parts[1], 8)
                        agc.memory[address] = value
    except FileNotFoundError:
        print(f"[AGC] Error: {filename} not found.")
