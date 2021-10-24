import os
import sys
from setuptools import setup, find_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')
def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LLAW33012021S2FLN3',
      version='0.0.1',
      description=('A docassemble extension.'),
      long_description='# docassemble.LLAW33012021S2FLN3\r\n\r\n## FLN3 : Paws Rights refusal for accomodation app\r\n\r\nThe FLN3 Paws Rights refusal application aids users in SA with disabilities to report instances of refusal-for entry into accomodation. The app helps build a repond of each refusal and it be ready to be sent to the DPTI. The app generates a PDF which is sent to the user via email.\r\n\r\n## Authors\r\n\r\nPeter Zhao, zhao0503@flinders.edu.au\r\nYi-lynn Teh, teh0047@flinders.edu.au\r\nAlex Habib, habi0041@flinders.edu.au\r\nMichelle Samuel, samu0055@flinders.edu.au\r\nCassandra Newsham, news0025@flinders.edu.au',
      long_description_content_type='text/markdown',
      author='Peter Zhao',
      author_email='zhao0503@flinders.edu.au',
      license='The MIT License (MIT)',
      url='https://github.com/LLAW3301/docassemble-LLAW33012021S2FLN3',
      packages=find_packages(),
      namespace_packages=['docassemble'],
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LLAW33012021S2FLN3/', package='docassemble.LLAW33012021S2FLN3'),
     )

