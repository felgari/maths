#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2015 Felipe Gallego. All rights reserved.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""A simple script to calculate the Greatest Common Divisor (GCD) and 
Least Common Multiple (LCM) of two integers.
"""

import sys

def check_argument_type_and_value(arg):
    """Check the argument is an integer not zero.
    """
    
    arg_ok = True
    value = 0
    
    try:
        value = int(arg)
        
        if value == 0:
            arg_ok = False
            print "Argument %s hasn't a valid value for calculation." % arg 
               
    except ValueError:
        arg_ok = False
        print "Argument %s is not an integer." % arg
        
    return arg_ok, value

def check_arguments():
    """Check number and type of program arguments.
    """
    
    all_args_ok = True
    values = []
    
    # Two arguments are needed.
    if len(sys.argv) == 3:
        
        for i in [1, 2]:        
            arg_ok, val = check_argument_type_and_value(sys.argv[i])
            
            if not arg_ok:        
                all_args_ok = False
                
            values.append(val)        
    else:
        all_args_ok = False
        print "Two arguments must be provided, not %d" % len(sys.argv) - 1
        
    return all_args_ok, values

def calculate(values):
    """Calculates the mcd and mcm of two integers.
    
    Args:
        values: The integers values to use for the calculation.
    """
    
    if values[0] >= values[1]:
        greatest, smallest = values
    else:
        smallest, greatest = values        
    
    while smallest:
        greatest, smallest = smallest, greatest % smallest
        
    gcd = greatest
    
    lcm = values[0] * values[1] / gcd
    
    print "For numbers %d and %d, GCD is %d and LCM is %d" % \
        (values[0], values[1], gcd, lcm)

if __name__ == "__main__":
    
    all_args_ok, values = check_arguments()
    
    if all_args_ok:
        calculate(values)