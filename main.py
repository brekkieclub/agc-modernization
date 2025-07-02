# agc_modernized_fixed/main.py

from agc_simulator import AGCSimulator

if __name__ == "__main__":
    program = [
        0o1000,  # TC to 0 (jump to address 0) – example instruction in octal
        0o00000  # HALT
    ]
    agc = AGCSimulator(program)
    agc.run(max_cycles=10)
