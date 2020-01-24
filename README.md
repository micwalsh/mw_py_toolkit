# mw_toolkit
General utilities to assist in python programming

NOTE: The code in this repo was originally written for https://github.com/openbmc/openbmc-test-automation but was recognized as having general utility.

*Example usage*

```
git clone https://github.com/micwalsh/mw_toolkit -o github ./mw_toolkit
cd mw_toolkit/
export PATH=${PWD}/bin:$PATH
export PYTHONPATH=${PWD}/lib:$PYTHONPATH
```

Here is a sample program which uses many of the mw_toolkit functions.

```
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
    '--whatever',
    default='this',
    help='bla, bla.')

# Populate stock_list with options we want.
stock_list = [("test_mode", 0), ("quiet", 0), ("debug", 0)]

def validate_parms():
    r"""
    Validate program parameters, etc.
    """

    # This function will be called by gen_setup().  If you have no validation to do, you can delete this
    # function altogether.

    valid_value(whatever, ['this', 'that'])


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
```

The preceding program would produce output that looks something like this:

```

#(CST) 2020/01/22 13:06:31.489152 -    0.113499 - Running demo.py.
#(CST) 2020/01/22 13:06:31.489250 -    0.000098 - Program parameter values, etc.:

command_line:                                     $HOME/bin/demo.py
demo_py_pid:                                      23706
demo_py_pgid:                                     23706
uid:                                              320092 (johndoe)
gid:                                              536858 (johndoe)
host_name:                                        my_machine.xxx.com
DISPLAY:                                          :1
PYTHON_PGM_PATH:                                  /opt/rh/python27/root/usr/bin/python
python_version:                                   2.7.16 (default, Jun 28 2019, 12:52:56) [GCC 4.4.7 20120313 (Red Hat 4.4.7-23)]
debug:                                            0
test_mode:                                        0
quiet:                                            0
whatever:                                         this

--------------------------------------------------------------------------------------------------------------
#(CST) 2020/01/22 13:06:31.512322 -    0.023072 - Printing dashes.
--------------------------------------------------------------------------------------------------------------
my_int:                                           354
my_string:                                        Hello
my_boolean:                                       True
my_float:                                         3.14
my_dict:
  [three]:                                        3
  [two]:                                          2
  [one]:                                          1
my_list:
  [0]:                                            John
  [1]:                                            Jacob
  [2]:                                            Jingleheimerschmidt
my_tuple:
  [0]:                                            John
  [1]:                                            Jacob
  [2]:                                            Jingleheimerschmidt

#(CST) 2020/01/22 13:06:31.535949 -    0.023627 - Finished running demo.py.

demo_py_runtime:                                  0.160372


```

