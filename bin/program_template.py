#!/usr/bin/env python

r"""
See help text for details.
"""

from gen_arg import *
from gen_print import *
from gen_valid import *

parser = argparse.ArgumentParser(
    usage='%(prog)s [OPTIONS]',
    description="%(prog)s will...",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    prefix_chars='-+')

parser.add_argument(
    '--whatever',
    default='',
    help='bla, bla.')

# Populate stock_list with options we want.
stock_list = [("test_mode", 0), ("quiet", 0), ("debug", 0)]


def exit_function():
    r"""
    Execute whenever the program ends normally or with the signals that we catch (i.e. TERM, INT).
    """

    # This function will be called by gen_exit_function().  If you have no cleanup to do, you can delete
    # this function altogether.

    # Your cleanup code here.


def validate_parms():
    r"""
    Validate program parameters, etc.
    """

    # This function will be called by gen_setup().  If you have no validation to do, you can delete this
    # function altogether.

    # Your validation code here...
    # valid_value(whatever)


def main():

    gen_setup()

    # Your code here.


main()
