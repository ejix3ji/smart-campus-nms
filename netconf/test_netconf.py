#!/usr/bin/env python3

from ncclient import manager
import sys
from pathlib import Path

# Allow importing the shared project configuration.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import NETCONF_HOST, NETCONF_PORT, USERNAME, PASSWORD

print(f"[*] Connecting to {NETCONF_HOST}:{NETCONF_PORT} via NETCONF...")

try:
    with manager.connect(
        host=NETCONF_HOST,
        port=NETCONF_PORT,
        username=USERNAME,
        password=PASSWORD,
        hostkey_verify=False,
        device_params={'name': 'default'},
        timeout=15
    ) as m:
        print("[+] SUCCESS! Local NETCONF Session Established.")
        print(f"[+] Session ID: {m.session_id}")
        print(f"[+] Client capability: {m.client_capabilities}")

        print("\n--- Device YANG Capabilities (First 5) ---")
        for cap in list(m.server_capabilities)[:5]:
            print(f"  - {cap}")

except Exception as e:
    print(f"[-] Connection failed: {e}", file=sys.stderr)
    sys.exit(1)
