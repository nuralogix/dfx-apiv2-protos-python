import pathlib

from setuptools import setup

from dfx_apiv2_protos import __version__

long_description = (pathlib.Path(__file__).parent / "README.md").read_text()

setup(
    name='dfx-apiv2-protos',
    author="NuraLogix Corporation",
    url='https://github.com/nuralogix/dfx-apiv2-protos-python',
    version=__version__,
    packages=['dfx_apiv2_protos'],
    install_requires=['protobuf>=3.12,<4'],
    setup_requires=['wheel'],
    description='dfx-apiv2-protos are compiled Python protos for the Nuralogix DeepAffex API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license_file='LICENSE.txt',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
