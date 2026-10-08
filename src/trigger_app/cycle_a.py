from trigger_app.cycle_b import ping_b


def ping_a() -> str:
    return "a" + ping_b.__name__
