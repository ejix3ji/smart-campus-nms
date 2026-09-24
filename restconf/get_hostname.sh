#!/bin/bash
echo "[*] Querying Campus Core Router via RESTCONF GET..."
curl -s -u "admin:admin" \
  -H "Accept: application/yang-data+json" \
  "http://127.0.0.1:8080/restconf/ds/ietf-datastores:running/Cisco-IOS-XR-um-hostname-cfg:hostname" | python3 -m json.tool
