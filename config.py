import os

NETCONF_HOST = os.getenv("NETCONF_HOST", "192.168.1.9")
NETCONF_PORT = int(os.getenv("NETCONF_PORT", "830"))

RESTCONF_HOST = os.getenv("RESTCONF_HOST", "192.168.1.9")
RESTCONF_PORT = int(os.getenv("RESTCONF_PORT", "8080"))

USERNAME = os.getenv("NMS_USERNAME", "admin")
PASSWORD = os.getenv("NMS_PASSWORD", "admin")
