import random
import time

# Simulated Firewall Rules
firewall_rules = {
    "allow": ["80", "443"],  # HTTP and HTTPS allowed
    "deny": ["21", "23", "3389"]  # FTP, Telnet, RDP denied
}

# Simulated Network Devices
devices = ["Router", "Switch", "Firewall", "PC1", "PC2", "Attacker"]

def simulate_packet(src, dst, port):
    """Simulate packet transmission through firewall"""
    print(f"\n[INFO] Packet from {src} → {dst} on port {port}")
    time.sleep(0.5)
    
    if port in firewall_rules["deny"]:
        print(f"[FIREWALL] Blocked packet on port {port} ❌")
    elif port in firewall_rules["allow"]:
        print(f"[FIREWALL] Allowed packet on port {port} ✅")
    else:
        print(f"[FIREWALL] Unknown port {port}, dropped ⚠️")

def simulate_attack():
    """Simulate common attacks"""
    attacks = [
        "Port Scanning",
        "DDoS Attack",
        "Brute Force Login Attempt",
        "SQL Injection Attempt",
        "ARP Spoofing"
    ]
    attack = random.choice(attacks)
    print(f"\n[ALERT] Detected {attack} from Attacker 🚨")
    time.sleep(0.5)
    print("[ACTION] Firewall mitigated the attack ✅")

def main():
    print("=== Network Security Simulation Started ===")
    time.sleep(1)

    # Normal Traffic Simulation
    simulate_packet("PC1", "Router", "80")   # HTTP allowed
    simulate_packet("PC2", "Router", "443")  # HTTPS allowed
    simulate_packet("PC1", "Router", "21")   # FTP blocked
    simulate_packet("PC2", "Router", "23")   # Telnet blocked

    # Attack Simulation
    simulate_attack()

    print("\n=== Simulation Completed ===")

if __name__ == "__main__":
    main()
