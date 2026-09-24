#!/usr/bin/env python3
"""
Smart Campus NMS - NETCONF Subsystem
Demonstration: Retrieve Running Configuration & Hostname
"""

from ncclient import manager
import xml.dom.minidom
import sys
from pathlib import Path

# Allow importing the shared project configuration.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from config import NETCONF_HOST, NETCONF_PORT, USERNAME, PASSWORD


def get_running_config():
    print(
        f"[*] Connecting to Campus Core Router "
        f"({NETCONF_HOST}:{NETCONF_PORT}) via NETCONF..."
    )

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
            print(f"[+] Connected! Session ID: {m.session_id}")
            print("[*] Sending <get-config> RPC for datastore: 'running'...\n")

            response = m.get_config(source='running')

            xml_str = xml.dom.minidom.parseString(
                response.xml
            ).toprettyxml(indent="  ")

            print("=" * 60)
            print("NETCONF <get-config> Response (XML):")
            print("=" * 60)

            lines = [line for line in xml_str.splitlines() if line.strip()]

            for line in lines[:35]:
                print(line)

            if len(lines) > 35:
                print(
                    f"  ... [truncated, {len(lines)} total lines "
                    f"of YANG/XML configuration] ..."
                )

            print("=" * 60)
            print("[+] NETCONF retrieval completed successfully.")

    except Exception as e:
        print(f"[-] Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    get_running_config()
