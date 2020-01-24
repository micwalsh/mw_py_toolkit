#!/usr/bin/env python

r"""
See help text for details.
"""

import sys
import collections

save_dir_path = sys.path.pop(0)

modules = ['gen_arg', 'gen_print', 'gen_valid', 'gen_misc', 'gen_cmd']
for module in modules:
    exec("from " + module + " import *")

sys.path.insert(0, save_dir_path)

valid_pgm_types = ['py', 'sh', 'pl']

parser = argparse.ArgumentParser(
    usage='%(prog)s [OPTIONS]',
    description="%(prog)s will demonstrate several of the tools found in the mw_tookit repo.",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    prefix_chars='-+')

parser.add_argument(
    '--pgm_type',
    default='py',
    help='The program types supported by this program.  The following values are supported: '
    + ', '.join(valid_pgm_types))

parser.add_argument(
    '--temp_dir_path',
    default='/tmp/',
    help='A directory for temporary objects.')


# Populate stock_list with options we want.
stock_list = [("test_mode", 0), ("quiet", 0), ("debug", 0)]


def exit_function():
    r"""
    Execute whenever the program ends normally or with the signals that we catch (i.e. TERM, INT).  This
    function will be called by gen_exit_function().
    """

    qprint_timen("Doing special clean up.")
    shell_cmd("rm -rf /tmp/my_temp_file")


def validate_parms():
    r"""
    Validate program parameters, etc.  This function will be called by gen_setup().
    """

    valid_value(pgm_type, valid_pgm_types)
    global temp_dir_path
    valid_dir_path(temp_dir_path)
    temp_dir_path = add_trailing_slash(temp_dir_path)
    set_pgm_arg(temp_dir_path)


def main():

    gen_setup()

    var1 = 57
    qprint_dashes(width=120)
    qprintn("Report:")
    qprint_var(var1)
    qprint_dashes(width=120)

    qprintn()
    qprint_timen("Demonstrating the use of the print_vars() function to print all types of variables:")

    last_name = "Doe"
    first_name = "John"
    age = 45
    weight = 151.2
    employed = True

    qprint_vars(last_name, first_name, age, weight, employed)

    qprintn()
    qprint_timen("Demonstrating the use of the print_vars() function to print complex variables:")

    personal_attributes = \
        {
            'education':
            [
                {
                    'school_name': 'Edison High',
                    'degree': 'High School Diploma',
                    'gpa': '3.5',
                    'sports': ['basketball', 'volleyball']
                },
                {
                    'school_name': 'Monsters University',
                    'degree': 'Bachelor of Science',
                    'gpa': '3.6',
                    'sports': ['basketball', 'volleyball', 'pickleball']
                }
            ],
            'favorite_quotes': ['A stitch in time saves nine.'],
            'favorite_colors': ['red', 'purple'],
        }

    qprint_vars(personal_attributes)

    rc, stdout = shell_cmd('hostname')


main()
