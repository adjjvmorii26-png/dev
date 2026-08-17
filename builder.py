def world_builder(sandbox):
    idea = sandbox.state.get("idea", "undefined concept")
    world = {
        "name": f"Realm_of_{idea.split()[-1]}",
        "rules": ["Physics-lite", "Narrative-driven", "Mutable"]
    }
    sandbox.update("world", world)
    return world