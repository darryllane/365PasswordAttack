from setuptools import setup, find_packages

setup(
    name='365 Password Attacks',
    version='1.0',
    author='Darryl lane',
    author_email='DarrylLane101@gmail.com',
    url='https://github.com/darryllane/365PasswordAttack',
    packages=['365PasswordAttack'],
    include_package_data=True,
    license='LICENSE',
    description='''
    Used to carry out autodiscover and password attacks on Office 365 Web Mail''',
    long_description=open('README.md').read(),
    scripts=['365PasswordAttack/365PasswordAttack'],
    install_requires=[
        "selenium",
	"PyVirtualDisplay"
    ],
)
