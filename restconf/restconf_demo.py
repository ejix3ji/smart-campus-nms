#!/usr/bin/env python3
"""
Smart Campus NMS - RESTCONF Subsystem
Demonstration: Programmatic State Query & Configuration via RESTful API
"""

import json
import sys
from pathlib import Path

import requests

# Allow importing the shared project configuration.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import RESTCONF_HOST, RESTCONF_PORT, USERNAME, PASSWORD


RESTCONF_BASE_URL = (
    f"http://{RESTCONF_HOST}:{RESTCONF_PORT}"
    "/restconf/ds/ietf-datastores:running"
)

HOSTNAME_URL = (
    RESTCONF_BASE_URL +
    "/Cisco-IOS-XR-um-hostname-cfg:hostname"
)

AUTH = (USERNAME, PASSWORD)

HEADERS_GET = {
    "Accept": "application/yang-data+json"
}

HEADERS_PUT = {
    "Content-Type": "application/yang-data+json"
}


def restconf_demo():
    print("=" * 60)
    print("RESTCONF DEMO: Campus Core Router")
    print("=" * 60)

    # 1. GET current hostname.
    print("[*] 1. Sending HTTP GET to retrieve running configuration...")

    try:
        response = requests.get(
            HOSTNAME_URL,
            auth=AUTH,
            headers=HEADERS_GET,
            timeout=15
        )

        if response.status_code == 200:
            data = response.json()

            current_name = data.get(
                "Cisco-IOS-XR-um-hostname-cfg:hostname",
                {}
            ).get(
                "system-network-name",
                "Not Set"
            )

            print(f"[+] Current Hostname: {current_name}")

        else:
            print(
                f"[-] GET failed: "
                f"{response.status_code} - {response.text}"
            )
            return

        # 2. PUT new hostname.
        new_name = "Campus-Core-Router-Prod"

        print(
            f"\n[*] 2. Sending HTTP PUT to update Hostname "
            f"-> '{new_name}'..."
        )

        payload = {
            "Cisco-IOS-XR-um-hostname-cfg:hostname": {
                "system-network-name": new_name
            }
        }

        response_put = requests.put(
            HOSTNAME_URL,
            auth=AUTH,
            headers=HEADERS_PUT,
            json=payload,
            timeout=15
        )

        if response_put.status_code in [200, 201, 204]:
            print(
                f"[+] HTTP {response_put.status_code} Success! "
                "Configuration updated."
            )
        else:
            print(
                f"[-] PUT failed: "
                f"{response_put.status_code} - {response_put.text}"
            )
            return

        # 3. GET again to verify.
        print(
            "\n[*] 3. Sending HTTP GET to verify "
            "updated configuration..."
        )

        response_verify = requests.get(
            HOSTNAME_URL,
            auth=AUTH,
            headers=HEADERS_GET,
            timeout=15
        )

        if response_verify.status_code == 200:
            verified_data = response_verify.json()

            print("[+] Verified Response (JSON):")
            print(json.dumps(verified_data, indent=2))

            print(
                f"\n[+] RESTCONF Demonstration Complete: "
                f"Hostname is now '{new_name}'."
            )
        else:
            print(
                f"[-] Verification GET failed: "
                f"{response_verify.status_code} - "
                f"{response_verify.text}"
            )

    except requests.RequestException as e:
        print(f"[-] RESTCONF connection error: {e}", file=sys.stderr)
        sys.exit(1)

    except ValueError as e:
        print(f"[-] Invalid JSON response: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    restconf_demo()
