import queue
import threading
from queue import Queue
from service.repository.repository import Repository
from utils.network import Network
from sensors import BaseSensor

N_MESSAGES = 5
DEFAULT_WAIT = 1            # Wait at most 1 sec

class Logging(threading.Thread):
    ''' Loggin service for devices and repository '''
    def __init__(self, repository: Repository, network: Network):
        self.repository: Repository = repository
        self.network: Network = network
        self.lock = threading.Lock()
        self.message_queue = Queue(maxsize=2*N_MESSAGES)
        self.subscribers = dict()

    def put(self, message: Message):
        with self.lock:
            try:
                self.message_queue.put(message, block=True, timeout=DEFAULT_WAIT)
            except queue.Full:
                # TODO Either wait or let the device use its cache \
                # At the moment this is undefined. It shouldn't go this far.
                pass

    def get(self, message: Message):
        with self.lock:
            try:
                self.message_queue.get(message, block=True, timeout=DEFAULT_WAIT)
            except queue.Empty:
                # TODO Either wait or let the device use its cache \
                # At the moment this is undefined. It shouldn't go this far.
                pass

    def subscribe(self, device: BaseSensor) -> None:
        ''' Subscription method to the logger '''
        if device.name not in self.subscribers.keys():
            self.subscribers.update({device.name: device})
            device.log_notifier_fn = self.put
        else:
            # TOCO: Notify that the device is already subscribed
            # It's not yet defined to where send the exceptions
            pass

    def unsubscribe(self, device: BaseSensor) -> None:
        ''' Unsubscribe device from the logger '''
        try:
            self.subscribers.pop(device.name)
        except KeyError:
            # TODO: Log that the device is already removed or not
            # the subscribers dictionary.
            pass

    def run(self) -> None:
        while True:
            #You most save data present on network here, keep on mind that network could have at maximum 5 messages
            #at the time.
            self.repository.save()