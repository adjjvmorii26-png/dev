def self_debugger(sandbox, thought):
    refactor = thought.replace("can't", "can attempt to")
    sandbox.update("thought_refactor", refactor)
    return refactor