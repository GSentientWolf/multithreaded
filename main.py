from logging.logging import Logging
from sensors.base_sensor import BaseSensor
from service.repository.repository import Repository
from utils.network import Network

if __name__ == '__main__':
    repository = Repository()
    network = Network()
    sensors = BaseSensor(network)
    logging = Logging(repository, network)
