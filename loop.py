def agent_interaction_loop(sandbox):
    world = sandbox.state.get("world")
    agents = sandbox.state.get("agents", [])

    interactions = []
    for agent in agents:
        perception = agent.perceive(world)
        action = agent.act("explore")
        interactions.append((perception, action))

    sandbox.update("interactions", interactions)
    return interactions