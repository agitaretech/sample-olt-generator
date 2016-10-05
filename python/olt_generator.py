#!/usr/bin/env python

"""
.. module:: olt_generator.py
:platform: Unix, Windows
:synopsis: Generates random online transaction data for testing and analysis
    purposes

.. moduleauthor:: Toddy Mladenov <toddysm@agitaretech.com>
"""
    
import logging
import random
import uuid

def gen_ip_address():
    """Generates random IP address from the complete IP address space. Returns
    a string with the IP address (ie NNN.NNN.NNN.NNN)

    :returns:  Random IP address as a string
    """
    ip_str = ''
    for i in range(1,5):
        ip_str += str(random.randint(0, 255))
        if i < 4:
            ip_str += '.'
    return ip_str

def gen_user_id(max_count=100000000):
    """Generates integer number in the range from 1 to `max_count` that can be
    used as user identifier

    :param max_count: The maximum count of user identifiers. 100,000,000 by default
    :type max_count: long int
    :returns:  Random integer
    """
    return str(random.randint(1, max_count))

def gen_transaction_id():
    """Random GUID that can be used as transaction ID

    :returns:  Random GUID as string
    """
    return str(uuid.uuid4())

if __name__ == "__main__":
    console_logger = logging.getLogger('logger.console')
    console_logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_logger.addHandler(console_handler)
    
    while True:
        olt_log_entry = gen_ip_address + ',' + gen_user_id
        console_logger.info()
