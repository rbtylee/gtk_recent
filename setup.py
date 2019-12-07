"""
gtk_recent - python script to add document to recently-used.xbel.
"""

from setuptools import setup

DEPS = ['pgi']


setup(
    name="gtk_recent",
    url="https://github.com/rbtylee/gtk_recent",
    license='LICENSE',
    author="Robert Wiley",
    author_email="ylee@bodhilinux.com",
    description='python script to add document to recently-used.xbel.',
    long_description=__doc__,
    zip_safe=False,
    platforms='any',
    install_requires=DEPS,
    scripts=['gtk_recent'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved ::'
        '"License :: OSI Approved :: GNU Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
