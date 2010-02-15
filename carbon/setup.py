#!/usr/bin/env python

import os
from glob import glob

if os.environ.get('USE_SETUPTOOLS'):
  from setuptools import setup
else:
  from distutils.core import setup


storage_dirs = [ ('storage/whisper',[]), ('storage/lists',[]),
                 ('storage/log',[]), ('storage/rrd',[]) ]
conf_files = [ ('conf', glob('conf/*')) ]

setup(
  name='carbon',
  version='0.9.6',
  url='https://launchpad.net/graphite',
  author='Chris Davis',
  author_email='chrismd@gmail.com',
  license='Apache Software License 2.0',
  description='Backend data caching and persistence daemon for Graphite',
  package_dir={'' : 'lib'},
  packages=['carbon'],
  scripts=glob('bin/*'),
  data_files=storage_dirs + conf_files,
  install_requires=['twisted', 'txamqp'],
  zip_safe=0,
)
