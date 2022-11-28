
""" Network settings """

import re

SEGMENT_RANGE = 32
IP_ADDRESS_POS = 0
MASK_POS = 1
N_UNAVAILABLE = 3
LOWER_BOUND = 2
UPPER_BOUND = 254
network_regex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(/\d{1,2})?')


def check_segment(network: str) -> tuple:
    """ Validator for the Network base IP and its mask """
    segment, mask = network_regex.match(network)
    if any((segment, mask)) is None:
        raise ValueError('Network information incomplete')
    return segment, mask[1:]


class Network:
    """ Network representation """

    def __init__(self, *, segment:str = '192.168.0.1/32'):
        from math import nan
        self.network = segment
        self.address_range = 2 ** (SEGMENT_RANGE - self.network[MASK_POS]) \
                             - N_UNAVAILABLE
        self.used_addresses = [None] * (self.address_range + 2)
        # Remove prohibited address (0, 1 (router), 255)
        self.used_addresses[0:1], self.used_addresses[-1] = [nan]*2, nan

    @property
    def network(self) -> tuple:
        """ Return the base IP address and the network mask"""
        return self._network

    @network.setter
    def network(self, segment) -> None:
        """ Validate network segment is at list valid """
        self._network = check_segment(segment)

    def add_network_service(self, service):
        """ Assign a free ip address within the available network range"""
        try:
            free_slot = self._find_first_empty(low=2, high=len(self.used_addresses)-1)
        except IndexError:
            raise IndexError('The network is full. No more addresses available')
        else:
            self.used_addresses[free_slot] = service

    def _find_first_empty(self, *, low, high) -> int:
        """ Find the first empty slot in order to assign the address """
        # TODO: Use BFS in order to give some semblance of a search algorithm

        # Let's use random ips for the time being
        from random import randint
        if not self.used_addresses.count(None):
            raise IndexError('All addresses are occupied')

        while True:
            ips = {randint(LOWER_BOUND, UPPER_BOUND) for _ in range(10)}
            for ip in ips:
                if self.used_addresses[ip] is None:
                    return ip



