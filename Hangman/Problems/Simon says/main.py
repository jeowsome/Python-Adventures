def what_to_do(instructions):
    if instructions.endswith("Simon says"):
        instructions = instructions.replace("Simon says", "")
        return "I " + instructions
    elif instructions.startswith("Simon says"):
        instructions = instructions.replace("Simon says", "")
        return "I" + instructions
    else:
        return "I won't do it!"
