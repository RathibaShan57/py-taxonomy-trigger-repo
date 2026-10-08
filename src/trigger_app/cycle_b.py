from trigger_app.cycle_a import ping_a


def ping_b() -> str:
    return "b" + ping_a.__name__
