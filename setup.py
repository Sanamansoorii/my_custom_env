from setuptools import setup

setup(
    name='my_custom_env',
    version='0.0.1',
    install_requires=['gym', 'numpy'],
    # packages=['my_custom_env', 'my_custom_env.envs'],
    packages = find_packages()
)
