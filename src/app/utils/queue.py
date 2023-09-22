# non blocking method
def queue_nonblock(function):
    try:
        if function.queue.current_messages:
            return function.queue.receive()[0].decode()
    except:
        pass
    return None
