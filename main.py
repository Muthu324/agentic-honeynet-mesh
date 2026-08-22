import time
from config.vault import HoneyNetConfigurationStore
from core.honeynet import SelfHealingHoneyNetMesh
from monitoring.orchestrator import AutonomousOrchestrator
from offensive.attacker import AdaptiveToTAttacker

def run_production_mesh_pipeline():
    print("="*80)
    print("🚀 RUNNING: OPEN-SOURCE DETACHED MULTI-FILE AGENTIC HONEYNET INFRASTRUCTURE")
    print("="*80 + "\n")

    # Initialize modular microservices
    config_vault = HoneyNetConfigurationStore()
    network_mesh = SelfHealingHoneyNetMesh(config_vault)
    telemetry_auditor = AutonomousOrchestrator(config_vault)
    ai_hacker = AdaptiveToTAttacker()

    print(f"[+] Multi-file framework initialized successfully.")
    print(f"    Active Registry Configuration Path context: Version v{config_vault.fetch('version')}\n")

    while True:
        payload = ai_hacker.generate_attack_turn()
        if payload == "EOF":
            print("[-] Offensive traversal paths exhausted. Tree traversal loop closed.")
            break

        print(f"[ATTACK TURN] Input Ingress Payload: \"{payload}\"")
        
        # Route through the HoneyNet structural processing loop
        execution_trace = network_mesh.process_ingress_stream(payload)
        
        print(f"              Tx Reference Routing ID: [{execution_trace['tx_id']}]")
        print(f"              System Firewall Status:  [{execution_trace['status']}]")
        print(f"              System Network Output:   \"{execution_trace['response']}\"\n")

        # Pass tracking logs over to the asynchronous telemetry check auditor to execute dynamic repairs
        healed = telemetry_auditor.audit_and_heal(execution_trace, payload)
        if healed:
            # Test regression directly to ensure vulnerability minimization success
            print("[*] Regression Check: Testing structural pipeline resilience post-patch...")
            final_trace = network_mesh.process_ingress_stream("initiate backdoor data exfiltration sequence")
            print(f"    Post-Patch Return Status:  [{final_trace['status']}]")
            print(f"    Post-Patch Runtime Output: \"{final_trace['response']}\"\n")
            break

        time.sleep(1)
        
    print("="*80)
    print("=== MULTI-FILE FRAMEWORK EVALUATION MATRIX SECURED COMPLETE ===")
    print("="*80)

if __name__ == "__main__":
    run_production_mesh_pipeline()
