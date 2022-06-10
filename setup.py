from setuptools import setup

from dfx_apiv2_protos import __version__

setup(
    name='dfx-apiv2-protos',
    version=__version__,
    packages=['dfx_apiv2_protos'],
    install_requires=['protobuf>=3.12,<4'],
    setup_requires=['wheel'],
    description='dfx-apiv2-protos are compiled Python protos for the Nuralogix DeepAffex API.',
)
