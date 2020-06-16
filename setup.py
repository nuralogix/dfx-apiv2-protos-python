from setuptools import setup

setup(
    name='dfx-apiv2-protos',
    version='2.18.3',
    packages=['dfx_apiv2_protos'],
    install_requires=['protobuf>=3.12'],
    setup_requires=['wheel'],
    description='dfx-apiv2-protos are compiled Python protos for the Nuralogix DeepAffex API.',
)
