#!/usr/bin/env python3
"""
Smart Campus NMS - NETCONF Subsystem
Demonstration: Retrieve Running Configuration & Hostname
"""

from ncclient import manager
import xml.dom.minidom
import sys

ROUTER_IP = '127.0.0.1'
NETCONF_PORT = 830
USERNAME = 'admin'
PASSWORD = 'admin'

def get_running_config():
    print(f"[*] Connecting to Campus Core Router ({ROUTER_IP}:{NETCONF_PORT}) via NETCONF...")
    
    try:
        with manager.connect(
            host=ROUTER_IP,
            port=NETCONF_PORT,
            username=USERNAME,
            password=PASSWORD,
            hostkey_verify=False,
            device_params={'name': 'default'},
            timeout=15
        ) as m:
            print(f"[+] Connected! Session ID: {m.session_id}")
            print("[*] Sending <get-config> RPC for datastore: 'running'...\n")
            
            # Send <get-config> RPC
            response = m.get_config(source='running')
            
            # Format and print the XML output nicely
            xml_str = xml.dom.minidom.parseString(response.xml).toprettyxml(indent="  ")
            
            # Show a concise preview of the configuration
            print("=" * 60)
            print("NETCONF <get-config> Response (XML):")
            print("=" * 60)
            
            lines = [l for l in xml_str.splitlines() if l.strip()]
            for line in lines[:35]:  # Display the first 35 lines for a clean demo output
                print(line)
            
            if len(lines) > 35:
                print(f"  ... [truncated, {len(lines)} total lines of YANG/XML configuration] ...")
            print("=" * 60)
            print("[+] NETCONF retrieval completed successfully.")

    except Exception as e:
        print(f"[-] Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    get_running_config()
