from setuptools import find_packages, setup

setup(
    name='Ai_model',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==2.0.1',
        'tensorflow==2.5.0',
    ],
)