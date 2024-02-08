from setuptools import setup

setup(
    name='earl_benchmark',
    packages=['earl_benchmark'],
    version='0.0.1',
    install_requires=[
        'gym',
        'metaworld',
        'mujoco-py==2.1.2.14',
        'numpy',
        'matplotlib',
        'scipy',
        'pybullet==3.2.0',
        'termcolor==1.1.0'
    ],
    dependency_links=[
        'git+https://github.com/rlworkgroup/metaworld.git@master#egg=metaworld',
    ],
    include_package_data=True
)
