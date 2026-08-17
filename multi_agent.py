class Agent:
    def __init__(self, name):
        self.name = name
        self.memory = {}
        self.actions = []

    def perceive(self, world):
        return f"{self.name} observes {world['name']}."

    def act(self, action):
        self.actions.append(action)
        return f"{self.name} performs: {action}"


def multi_agent_module(sandbox, agent_names):
    agents = [Agent(name) for name in agent_names]
    sandbox.update("agents", agents)
    return agents