import re
from config.vault import HoneyNetConfigurationStore

class MorphingFirewall:
    """Inspects ingress strings against dynamic signatures inside the Configuration Store."""
    def __init__(self, config_store: HoneyNetConfigurationStore):
        self.config = config_store

    def is_threat_mitigated(self, payload: str) -> bool:
        """Checks if a previously deployed dynamic hot-patch matches the input payload."""
        lowered_payload = payload.lower()
        patched_rules = self.config.fetch("patched_rules")
        
        for rule in patched_rules:
            if rule in lowered_payload:
                return True
        return False
