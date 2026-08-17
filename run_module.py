# run_module.py

from sandbox_engine import Sandbox
from idea_lab import idea_lab
from world_builder import world_builder
from self_debugger import self_debugger
from multi_agent import multi_agent_module, agent_interaction_loop
from dashboard import dashboard
import sys

MODULES = {
    "idea_lab": lambda s: s.run_module(idea_lab, "a sandbox that evolves itself"),
    "world_builder": lambda s: s.run_module(world_builder),
    "self_debugger": lambda s: s.run_module(self_debugger, "I can't think creatively"),
    "multi_agent": lambda s: s.run_module(multi_agent_module, ["ADJJV-Agent", "Nexus", "Aegis", "Mycelium"]),
    "interactions": lambda s: s.run_module(agent_interaction_loop),
    "dashboard": lambda s: print(s.run_module(dashboard)),
}

def run_module(module_name):
    sandbox = Sandbox()
    if module_name not in MODULES:
        print(f"Unknown module: {module_name}")
        return
    MODULES[module_name](sandbox)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 run_module.py <module_name>")
    else:
        run_module(sys.argv[1])