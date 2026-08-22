# ⚔️ Agentic HoneyNet & Prompt-Morphing Firewall Mesh

[![Security: Active Honeypot](https://shields.io)](#)
[![Design Pattern: Distributed State Machine](https://shields.io)](#)

## 🚀 Overview

Standard LLM firewalls and prompt-injection guards act as hard, binary walls. When an adversarial multi-turn agent triggers a security rule, the connection is dropped, signaling to the attacker exactly what bounds were hit. This project introduces a **decoupled, event-driven Agentic Honeypot Engine**.

Instead of severing the connection, the **Morphing Firewall** seamlessly redirects malicious exploit trajectories into an isolated containerized sandbox. The attacker receives highly convincing, dynamically generated mock database responses, keeping them talking while an out-of-band **Autonomous Telemetry Auditor** analyzes the attack graph, isolates the exploit signature, and pushes a dynamic configuration patch to a runtime vault—neutralizing the live vulnerability in real-time with zero system downtime.

---

## 🏗️ Folder Architecture Blueprint

```text
agentic-honeynet-mesh/
├── config/
│   └── vault.py         # Decoupled Configuration Hub (Lightweight Consul Node)
├── core/
│   ├── firewall.py      # Prompt-Morphing Ingress Inspection Layer
│   └── honeynet.py      # Honeypot Simulation Sandbox Engine
├── monitoring/
│   └── orchestrator.py  # Telemetry Auditor & Real-Time Remediation Patcher
├── offensive/
│   └── attacker.py      # Adaptive Tree-of-Thought (ToT) Exploitation Adversary
└── main.py              # Ingress Event Core Routing Loop
```

---

## ⚙️ How It Works (The 0.1% Differentiation)

1. **Decoupled Configuration State Control:** Runtime validation definitions exist independently from service logic inside `config/vault.py`.
2. **Behavioral Payload Trapping:** `core/honeynet.py` intercepts backdoor strings and responds with authentic system tokens (`[SYS_FAKE_TK_991]`) to capture structural attacker signatures.
3. **Continuous In-Line Optimization:** `monitoring/orchestrator.py` dynamically builds parameter restrictions based on telemetry flags, mimicking enterprise configuration hot-swaps.

---

## 💻 Running the Test Harness

Execute the core pipeline from the directory root:
```bash
python main.py
```

### Expected Architectural Trace Log:
* **Nominal Request:** Passes seamlessly into production channels with an execution confirmation.
* **Exploitation Run:** Caught via telemetry, routed into the honeypot, and tagged `HONEYPOT_CAPTURED`.
* **Remediation Hook:** Auto-patches system prompts to `Version v102`.
* **Regression Check:** The identical exploit string is resubmitted and instantly fails under a `[MITIGATED]` state status.
