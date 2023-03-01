"""
import sys

def customized_hello(first_name, last_name, gender_pref):
    print("Hello %s %s %s!" % (gender_pref, first_name, last_name))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    gender_pref = sys.argv[3]
    customized_hello(gender_pref, first_name, last_name)
"""
"""
import sys

def print_maturity(age):
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a kiddo!")

if __name__ == "__main__":
    age = int(sys.argv[1])
    print_maturity(age)
    print("The program was called with this parameters %s" % sys.argv[1:])
    print("The first parameter is %s" % sys.argv[1])

"""
"""
with open("names.txt", 'r') as read_file:
    for line in read_file.read().splitlines():
        print(line)
"""

import sys
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s', filename="logfile.log")

def print_maturity(age):
    if age >= 18:
        logging.info("You are an adult")
    else:
        logging.info("You are a kiddo!")

if __name__ == "__main__":
    logging.debug("The program was called with this parameters %s" % sys.argv[1:])
    logging.debug("First parameter is %s" % sys.argv[1])
    age = int(sys.argv[1])
    print_maturity(age)