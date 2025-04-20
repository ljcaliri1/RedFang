#!usr/bin/env python3

"""
RedFang - Payload Generator (Public Version)
Part of the Red Halo Toolkit
"""
import argparse
from utils.payload_generator import generate_payload

def main():
    parser = argparse.ArgumentParser(description="RedFang -Payload Generator")
    parser.add_argument("--type", required=True, help="Payload type (bash, nc, pwershell, python)")
    parser.add_argument("--ip", required=True, help="Target IP address")
    parser.add_argument("--port", required=True, help="Target port")
    parser.add_argument("--output", help="Optional output file to save payload")

    args = parser.parse_args()

    payload = generate_payload(args.type, args.ip, args.port)
    if not payload:
        print("[-] Invalid payloadtype. Use bash, nc, powershell, or python.")
        return

    print(f"[+] Payload Type: {args.type}")
    print(f"[+] Generated Payload:\n{payload}")

    if args.output:
        try:
            with open(args.output, "w") as f:
                f.write(payload + "\n")
            print(f"[✓] Payload saved to {args.output}")
        except Exception as e:
            print(f"[-] Failed to save payload: {e}")

if __name__ == "__main__":
    main()

