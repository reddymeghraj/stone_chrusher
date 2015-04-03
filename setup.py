from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='stone_crusher',
    version=version,
    description='Application For Stone Crusher',
    author='Wayzon Technology Services Pvt Ltd',
    author_email='reddymeghraj@wayzontech.in',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
