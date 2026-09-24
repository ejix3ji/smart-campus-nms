#!/bin/bash
NEW_NAME=${1:-"Campus-Core-Router-Main"}
echo "[*] Updating Campus Core Router Hostname -> '$NEW_NAME' via RESTCONF PUT..."
curl -i -s -u "admin:admin" \
  -X PUT \
  -H "Content-Type: application/yang-data+json" \
  -d "{\"Cisco-IOS-XR-um-hostname-cfg:hostname\": {\"system-network-name\": \"$NEW_NAME\"}}" \
  "http://127.0.0.1:8080/restconf/ds/ietf-datastores:running/Cisco-IOS-XR-um-hostname-cfg:hostname"

echo -e "\n[*] Verifying updated state..."
bash ~/smart-campus-nms/restconf/get_hostname.sh
