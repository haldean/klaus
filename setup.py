# encoding: utf-8

import glob
from distutils.core import setup


def install_data_files_hack():
    # This is a clever hack to circumvent distutil's data_files
    # policy "install once, find never". Definitely a TODO!
    # -- https://groups.google.com/group/comp.lang.python/msg/2105ee4d9e8042cb
    from distutils.command.install import INSTALL_SCHEMES
    for scheme in INSTALL_SCHEMES.values():
        scheme['data'] = scheme['purelib']


install_data_files_hack()

requires = ['flask', 'pygments', 'dulwich(>=0.8.6)', 'httpauth']

try:
    import argparse  # not available for Python 2.6
except ImportError:
    requires.append('argparse')


setup(
    name='klaus',
    version='0.2',
    author='Jonas Haag',
    author_email='jonas@lophus.org',
    packages=['klaus'],
    scripts=['bin/klaus'],
    data_files=[
        ['klaus/templates', glob.glob('klaus/templates/*')],
        ['klaus/static',    glob.glob('klaus/static/*')],
    ],
    url='https://github.com/jonashaag/klaus',
    description='The first Git web viewer that Just Works™.',
    long_description=__doc__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "Topic :: Software Development :: Version Control",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    requires=requires,
)
