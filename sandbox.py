def dashboard(sandbox):
    world = sandbox.state.get("world", {})
    agents = sandbox.state.get("agents", [])
    idea = sandbox.state.get("idea", "No idea generated")
    thought = sandbox.state.get("thought_refactor", "No thought refactor yet")
    interactions = sandbox.state.get("interactions", [])
    logs = sandbox.logs

    view = "\n=== SANDBOX DASHBOARD — ALL SYSTEMS ACTIVE ===\n"

    view += f"\nIDEA LAB OUTPUT:\n  {idea}\n"

    view += f"\nWORLD STATE:\n"
    view += f"  Name: {world.get('name', 'None')}\n"
    view += f"  Rules: {world.get('rules', [])}\n"

    view += "\nAGENTS:\n"
    for agent in agents:
        view += f"  - {agent.name}\n"
        view += f"    Actions: {agent.actions}\n"
        view += f"    Memory: {agent.memory}\n"

    view += f"\nSELF DEBUGGER OUTPUT:\n  {thought}\n"

    view += "\nINTERACTIONS:\n"
    for p, a in interactions:
        view += f"  * {p}\n    {a}\n"

    view += "\nLOGS:\n"
    for log in logs:
        view += f"  - {log}\n"

    sandbox.update("dashboard_view", view)
    return view