from setuptools import setup

from dfx_apiv2_protos import __version__

setup(
    name='dfx-apiv2-protos',
    author="NuraLogix Corporation",
    version=__version__,
    packages=['dfx_apiv2_protos'],
    install_requires=['protobuf>=3.12,<4'],
    setup_requires=['wheel'],
    description='dfx-apiv2-protos are compiled Python protos for the Nuralogix DeepAffex API.',
    license_file='LICENSE.txt',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
