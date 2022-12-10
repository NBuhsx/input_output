from setuptools import setup

setup(
    name='input_output',
    version='1.0',
    description='Input output yield',
    author='NBuhsx',
    author_email='sergey33sergey@yandex.com',
    packages=['input_output'],  # would be the same as name
    # external packages acting as dependencies
    install_requires=['wheel', 'bar', 'greek'],
)
