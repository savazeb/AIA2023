import posix_ipc as ipc

class Queue:

    def __init__(self, qname, block=True):
        self.__queue = ipc.MessageQueue(qname, ipc.O_CREAT)
        self.__queue.block = block

    def cleanup(self):
        self.__queue.close()
        self.__queue.unlink()

    def check_message(self):
        return self.__queue.current_messages

    def receive_non_block(self):
        try:
            if self.check_message():
                return self.receive()
        except:
            pass

        return None

    def receive(self):
        return self.__queue.receive()[0].decode()

    def send(self, message):
        self.__queue.send(message)
