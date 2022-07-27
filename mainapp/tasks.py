import dramatiq


@dramatiq.actor
def do_somthing():
    print("Async task")