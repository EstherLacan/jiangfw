#!/usr/bin/python
# Filename: using_sys.py

import sys
print('The command line arguments are:')

for i in sys.argv:
    print(i)

print('\n\nThe Python path is ',sys.path,'\n')
print('\n\nThe Python api_version is ',sys.api_version,'\n')
print('\n\nThe Python base_exec_prefix is ',sys.base_exec_prefix,'\n')
print('\n\nThe Python base_prefix is ',sys.base_prefix,'\n')
print('\n\nThe Python builtin_module_names is ',sys.builtin_module_names,'\n')
print('\n\nThe Python byteorder is ',sys.byteorder,'\n')
print('\n\nThe Python callstats is ',sys.callstats,'\n')
print('\n\nThe Python copyright is ',sys.copyright,'\n')
print('\n\nThe Python hash_info is ',sys.hash_info,'\n')
sys.stdout.writelines("dddddddddddddddddd")
print(sys.argv.reverse.__doc__)
