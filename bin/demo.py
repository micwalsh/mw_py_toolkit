#!/usr/bin/env python

r"""
See help text for details.
"""

import sys
import collections

save_dir_path = sys.path.pop(0)

modules = ['gen_arg', 'gen_print', 'gen_valid']
for module in modules:
    exec("from " + module + " import *")

sys.path.insert(0, save_dir_path)

parser = argparse.ArgumentParser(
    usage='%(prog)s [OPTIONS]',
    description="%(prog)s will demonstrate some of the tools found in the mw_tookit repo.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    prefix_chars='-+')

parser.add_argument(
    '--articles',
    default='this',
    help='bla, bla.')

# Populate stock_list with options we want.
stock_list = [("test_mode", 0), ("quiet", 0), ("debug", 0)]


def validate_parms():
    r"""
    Validate program parameters, etc.
    """

    # This function will be called by gen_setup().

    valid_value(articles, ['this', 'that'])


def main():

    gen_setup()

    qprint_dashes(width=110)
    qprint_timen("Printing dashes.")
    qprint_dashes(width=110)

    my_int = 354
    my_string = "Hello"
    my_boolean = True
    my_float = 3.14
    my_dict = dict(one=1, two=2, three=3)
    my_ord_dict = collections.OrderedDict([('one', 1), ('two', 2), ('three', 3)])
    my_list = ["John", "Jacob", "Jingleheimerschmidt"]
    my_tuple = ("John", "Jacob", "Jingleheimerschmidt")
    print_vars(my_int, my_string, my_boolean, my_float, my_dict, my_list, my_tuple)


main()
