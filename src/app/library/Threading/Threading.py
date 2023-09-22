from threading import Thread

class Threading:
    def run(self):
        def decorator(function):
            Thread(target=function).start()

        return decorator
