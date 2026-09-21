#!/usr/bin/env python3
"""
Smart Campus NMS - NETCONF Subsystem
Demonstration: Safe Configuration Change (<edit-config> + <commit>)
"""
from ncclient import manager
import xml.dom.minidom
import sys
ROUTER_IP = '127.0.0.1'
NETCONF_PORT = 830
USERNAME = 'admin'
PASSWORD = 'admin'
NEW_HOSTNAME = 'Campus-Core-R1'
# NETCONF XML payload with explicit base namespace and YANG module namespace
CONFIG_PAYLOAD = f"""
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <hostname xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-um-hostname-cfg">
    <system-network-name>{NEW_HOSTNAME}</system-network-name>
  </hostname>
</config>
"""
# Subtree filter to query the hostname
FILTER_PAYLOAD = """
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" type="subtree">
  <hostname xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-um-hostname-cfg"/>
</filter>
"""
def edit_and_verify():
    print(f"[*] Connecting to Campus Core Router ({ROUTER_IP}:{NETCONF_PORT}) via NETCONF...")
    
    try:
        with manager.connect(
            host=ROUTER_IP,
            port=NETCONF_PORT,
            username=USERNAME,
            password=PASSWORD,
            hostkey_verify=False,
            device_params={'name': 'default'},
            timeout=20
        ) as m:
            print(f"[+] Connected! Session ID: {m.session_id}")
            
            # 1. Send <edit-config> targeting the candidate datastore
            print(f"[*] Sending <edit-config> to set Hostname -> '{NEW_HOSTNAME}'...")
            edit_reply = m.edit_config(target='candidate', config=CONFIG_PAYLOAD)
            print("[+] <edit-config> Accepted by device.")
            
            # 2. Commit the candidate configuration to running
            print("[*] Sending <commit> RPC (transactional commit)...")
            m.commit()
            print("[+] <commit> SUCCESS: Configuration applied to running datastore.")
            
            # 3. Verify by querying the running configuration with a filter
            print("\n[*] Verifying running datastore with subtree <filter>...")
            verify_reply = m.get_config(source='running', filter=FILTER_PAYLOAD)
            
            xml_str = xml.dom.minidom.parseString(verify_reply.xml).toprettyxml(indent="  ")
            print("=" * 60)
            print("Verified Running Configuration (XML):")
            print("=" * 60)
            for line in xml_str.splitlines():
                if line.strip():
                    print(line)
            print("=" * 60)
            print(f"[+] NETCONF Demonstration Complete: Hostname is now '{NEW_HOSTNAME}'.")
    except Exception as e:
        print(f"[-] Error: {e}", file=sys.stderr)
if __name__ == '__main__':
    edit_and_verify()