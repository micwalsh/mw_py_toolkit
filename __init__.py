import sys
import os
import argparse

# Add the mwtoolkit/lib subdirectory to sys.path to subordinate modules to import sister modules.
# Note: All directory path values will include a trailing slash.
package_base_dir_path = os.path.dirname(os.path.realpath(__file__)) + os.sep
sys.path.append(package_base_dir_path + "lib")

from .lib import gen_arg as ga, gen_print as gp, gen_valid as gv, gen_cmd as gc, gen_misc as gm, \
    var_funcs as vf, func_timer as ft, func_args as fa, var_stack as vs
