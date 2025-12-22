# Whitelist + firewall logic

from netaddr import IPAddress, IPNetwork
from src.core.config import WHITELIST

def is_ip_allowed(ip: str) -> bool:
    ip_addr = IPAddress(ip)
    return any(ip_addr in IPNetwork(net) for net in WHITELIST)
    