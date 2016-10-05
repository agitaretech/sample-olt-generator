# sample-olt-generator
This sample application generates Online Transaction log entries in the following format:

    [ip_address], [user_id], [timestamp], [purchase_amount], [transaction_id], [credit_card_no], [order_no]

where:
* `ip_address` is a valid IP address from the complete IP address space
* `user_id` is an integer between 1 and 100 Million by default; upper count can be changed
* `timestamp` is a timestamp in ISO 8601 format (yyyy-MM-ddTHH:MM:SSZ)
* `purchase_amount` is a float with two decimal points precision
* `transaction_id` is a UUID
* `credit_card_no` is a masked credit card number in the following format:
    * `****-****-****-NNNN` for MasterCard and Visa credit card numbers
    * `****-******-*NNNN` for American Express credit card numbers
* `order_no` is a 6 characters string with random digits and letters in uppercase

Example log entry looks like this:

    106.209.197.154,164605,2016-08-01T00:00:02Z,3093.82,684aa7fe-ab87-4862-b373-097375561aa1,****-****-****-0988,973EV1

The script works in two different modes:
* **Historical transactions generator** - Generates online transactions data between two specified dates. For this
mode you need to specify how many transaction entries you would like to generate (default is 1M). It sends the data
to the standard output but will stop when the maximum is reached
* **Stream of online transactions** - In this mode it continuously generates transactions with the current timestamp
and sends them to the standard output