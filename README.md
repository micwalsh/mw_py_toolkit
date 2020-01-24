# mw_toolkit
General utilities to assist in python programming

NOTE: The code in this repo was originally written for https://github.com/openbmc/openbmc-test-automation but was recognized as having general utility.

# Example installation

From a linux bash shell:

```
git clone https://github.com/micwalsh/mw_toolkit -o github ./mw_toolkit
cd mw_toolkit/
export PATH=${PWD}/bin:$PATH
export PYTHONPATH=${PWD}/lib:$PYTHONPATH
```

The bin/demo.py program demonstrates the use of several of the mw_toolkit functions.  At the time this document was written, the bin/demo.py file looked like this.


```
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
```

The preceding program would produce output that looks something like this:

```

#(CST) 2020/01/24 13:52:30.895823 -    1.636184 - Running demo.py.
#(CST) 2020/01/24 13:52:30.895921 -    0.000098 - Program parameter values, etc.:

command_line:                                     /afs/rchland.ibm.com/usr6/micwalsh/sandbox/apollodev/src/aipl/x86/demo.py
demo_py_pid:                                      31091
demo_py_pgid:                                     31091
uid:                                              111642 (csptest)
gid:                                              1 (bin)
host_name:                                        alcb203.aus.stglabs.ibm.com
DISPLAY:                                          :90
PYTHON_PGM_PATH:                                  /opt/rh/rh-python36/root/usr/bin/python
python_version:                                   3.6.3 (default, Apr 10 2019, 11:27:51) [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
pgm_type:                                         py
temp_dir_path:                                    /tmp/
test_mode:                                        0
quiet:                                            0
debug:                                            0

------------------------------------------------------------------------------------------------------------------------
Report:
var1:                                             57
------------------------------------------------------------------------------------------------------------------------

#(CST) 2020/01/24 13:52:30.955168 -    0.059247 - Demonstrating the use of the print_vars() function to print all types of variables:
last_name:                                        Doe
first_name:                                       John
age:                                              45
weight:                                           151.2
employed:                                         True

#(CST) 2020/01/24 13:52:30.996934 -    0.041766 - Demonstrating the use of the print_vars() function to print complex variables:
personal_attributes:
  [education]:
    [0]:
      [school_name]:                              Edison High
      [degree]:                                   High School Diploma
      [gpa]:                                      3.5
      [sports]:
        [0]:                                      basketball
        [1]:                                      volleyball
    [1]:
      [school_name]:                              Monsters University
      [degree]:                                   Bachelor of Science
      [gpa]:                                      3.6
      [sports]:
        [0]:                                      basketball
        [1]:                                      volleyball
        [2]:                                      pickleball
  [favorite_quotes]:
    [0]:                                          A stitch in time saves nine.
  [favorite_colors]:
    [0]:                                          red
    [1]:                                          purple
#(CST) 2020/01/24 13:52:31.021411 -    0.024478 - Issuing: hostname
alcb203.aus.stglabs.ibm.com
#(CST) 2020/01/24 13:52:31.034988 -    0.013577 - Doing special clean up.
#(CST) 2020/01/24 13:52:31.049303 -    0.014314 - Issuing: rm -rf /tmp/my_temp_file

#(CST) 2020/01/24 13:52:31.066765 -    0.017462 - Finished running demo.py.

demo_py_runtime:                                  1.807232
```

