from agc.cpu import AGC
from agc.loader import load_agc_memory

def main():
    agc = AGC()
    load_agc_memory(agc, "core_dump.agc")

    for cycle in range(50):
        halted = agc.cycle()
        if halted:
            print(f"[AGC] HALT at PC={agc.PC:04o}")
            break

if __name__ == "__main__":
    main()
