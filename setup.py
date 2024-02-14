from setuptools import setup, find_namespace_packages

setup(
    name='earl_benchmark',
    version='0.0.1',
    packages=find_namespace_packages(),
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
