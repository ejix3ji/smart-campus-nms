from ncclient import manager
import sys
HOST = '127.0.0.1'
PORT = 830
USER = 'admin'
PASS = 'admin'
print(f"[*] Connecting to {HOST}:{PORT} via NETCONF...")
try:
    with manager.connect(
        host=HOST,
        port=PORT,
        username=USER,
        password=PASS,
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