#!/usr/bin/env python3
"""
Smart Campus NMS - RESTCONF Subsystem
Demonstration: Programmatic State Query & Configuration via RESTful API
"""

import requests
import json
import sys

URL = "http://127.0.0.1:8080/restconf/ds/ietf-datastores:running/Cisco-IOS-XR-um-hostname-cfg:hostname"
AUTH = ('admin', 'admin')
HEADERS_GET = {'Accept': 'application/yang-data+json'}
HEADERS_PUT = {'Content-Type': 'application/yang-data+json'}

def restconf_demo():
    print("=" * 60)
    print("RESTCONF DEMO: Campus Core Router")
    print("=" * 60)
    
    # 1. GET Current Hostname
    print("[*] 1. Sending HTTP GET to retrieve running configuration...")
    r = requests.get(URL, auth=AUTH, headers=HEADERS_GET)
    if r.status_code == 200:
        data = r.json()
        current_name = data.get("Cisco-IOS-XR-um-hostname-cfg:hostname", {}).get("system-network-name", "Not Set")
        print(f"[+] Current Hostname: {current_name}")
    else:
        print(f"[-] GET failed: {r.status_code} - {r.text}")
        return

    # 2. PUT New Hostname
    new_name = "Campus-Core-Router-Prod"
    print(f"\n[*] 2. Sending HTTP PUT to update Hostname -> '{new_name}'...")
    payload = {
        "Cisco-IOS-XR-um-hostname-cfg:hostname": {
            "system-network-name": new_name
        }
    }
    r_put = requests.put(URL, auth=AUTH, headers=HEADERS_PUT, json=payload)
    if r_put.status_code in [200, 201, 204]:
        print(f"[+] HTTP {r_put.status_code} Success! Configuration updated.")
    else:
        print(f"[-] PUT failed: {r_put.status_code} - {r_put.text}")
        return

    # 3. GET Again to Verify
    print("\n[*] 3. Sending HTTP GET to verify updated configuration...")
    r_verify = requests.get(URL, auth=AUTH, headers=HEADERS_GET)
    if r_verify.status_code == 200:
        verified_data = r_verify.json()
        print("[+] Verified Response (JSON):")
        print(json.dumps(verified_data, indent=2))
        print(f"\n[+] RESTCONF Demonstration Complete: Hostname is now '{new_name}'.")

if __name__ == '__main__':
    restconf_demo()
