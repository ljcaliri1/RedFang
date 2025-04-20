# RedFang - Payload Generator

**RedFang** is the payload generator module within the Red Halo red team toolkit.  
It simulates the creation of reverse shell payloads for various platforms and is designed for educational use, training, and demonstration in offensive cybersecurity scenarios.

This is a safe, non-malicious, and simulation-only tool. Payloads generated are for demonstration purposes and do not establish real connections.

---

## Features

- CLI-based payload generator
- Supports:
- Bash reverse shell
- Netcat shell
- PowerShell shell
- Python reverse shell
- Custom IP and port arguments
- Optional output to text file
- Modular design for future upgrades (obfuscation, encoding, encryption)

---

## File Structure

RedFang/
├── redfang.py
├── README.md
├── LICENSE
├── requirements.txt
└── utils/
    └── payload_generator.py
---

## Requirements

RedFang currently requires no external packages.

To future-proof installs:

```bash
pip install -r requirements.txt

## Disclaimer

This tool is intended for **educational** and **authorized penetration testing** purposes only.  
The author does **not condone** any illegal or unethical activity carried out using this tool.  
Use RedFang **only** in environments where you have explicit permission to test.  

By using this tool, you agree that you are solely responsible for your actions.


## License

This project is licensed under the terms of the [MIT License](LICENSE).
