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
import string
import time
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

def gen_order_id(size=6):
    """Random string of size `size` consisting of upper case letters and numbers
    that can be used as order identifier

    :param size: The length of the order identifiers. 6 by default
    :type max_count: int
    :returns:  Order identifier
    """
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))

def gen_cc_number_masked():
    """Generates masked credit card number. It generates two types of numbers:
    - 16 digit sequence (****-****-****-NNNN) that match Visa and MasterCard
    credit card numbers
    - 15 digit sequence (****-******-*NNNN) that matches America Express credit
    card numbers

    :returns:  Masked credit card number as string
    """
    last_four = str(random.randint(1, 9999)).zfill(4)
    
    # introducing some randomization what kind of CC number is genrated
    if random.randint(1, 100) % 2 == 0:
        cc_number = '****-****-****-' + last_four
    else:
        cc_number = '****-******-*' + last_four
    
    return cc_number

def gen_purchase_amount(max_amount=1000):
    """Generates random number between 1 and `max_amount` that can be used as
    purchase amount for an order

    :param max_amount: The maximum amount for the purchases. Default is 1,000
    :type max_count: int
    :returns:  Purchase amount as float
    """
    return '{0:.2f}'.format(random.uniform(1, max_amount))

def convert_ISOdatestr_to_seconds(iso_date):
    """Converts ISO-8601 formatted string into Python `time` tuple and returns
    the seconds since Jan, 1st 1970. Accepted format for the date is `YYYY-MM-DD`
    Note: This function does not interpret the time part of the ISO-8601 and throws
    exception if the time part is specified

    :param iso_date: The ISO-8601 formatted date
    :type iso_date: string
    :returns:  The seconds since epoch
    :raises: ValueError - If the `iso_date` string cannot be parsed
    """
    till_date = time.strptime(iso_date, '%Y-%m-%d')
    seconds = time.mktime(till_date)
    return seconds

def gen_historical_timestamp(start_date, end_date):
    """Converts the input ISO-8601 formatted strings into Python `time` tuple and
    returns randomly generated ISO-8601 timestamp between those two dates.
    Accepted format for the date is `YYYY-MM-DD`
    Note: This function does not interpret the time part of the ISO-8601 and throws
    exception if the time part is specified

    :param start_date: The ISO-8601 formatted date
    :type start_date: string
    :param end_date: The ISO-8601 formatted date
    :type end_date: string
    :returns:  Random ISO-8601 timestamp between those dates as string
    :raises: ValueError - If the `start_date` and `end_date` strings cannot be parsed
    """
    start_date = convert_ISOdatestr_to_seconds(start_date)
    end_date = convert_ISOdatestr_to_seconds(end_date)
    result = time.gmtime(random.uniform(start_date, end_date))
    
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", result)

if __name__ == "__main__":
    separator = ','
    
    console_logger = logging.getLogger('logger.console')
    console_logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_logger.addHandler(console_handler)
    
    while True:
        olt_log_entry = gen_ip_address() + separator + gen_user_id() + separator + \
                        gen_historical_timestamp(1,2) + separator + gen_purchase_amount() + \
                        separator + gen_transaction_id() + separator + \
                        gen_cc_number_masked() + separator + gen_order_id()
        console_logger.info(olt_log_entry)
