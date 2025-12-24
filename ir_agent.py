import json
import subprocess
import sys

def respond(incident):
    itype = incident.get("type")

    if itype == "SSH_BRUTE_FORCE":
        ip = incident.get("source_ip")
        cmd = ["./block_ip.sh", ip]

    elif itype == "COMPROMISED_USER":
        user = incident.get("username")
        cmd = ["./disable_user.sh", user]

    elif itype == "SUSPICIOUS_SERVICE":
        service = incident.get("service")
        cmd = ["./stop_service.sh", service]

    else:
        print("[-] Unknown incident type")
        return

    print(f"[+] Executing response for {itype}")
    subprocess.run(cmd)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 ir_agent.py incident.json")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        incident = json.load(f)

    respond(incident)
