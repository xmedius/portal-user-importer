from setuptools import setup

setup(
    name='xmcuserimporter',
    version='1.1.0',
    description='Pyhton module for importing user in XmediusCloud from a CSV file',
    long_description='See https://github.com/xmedius/xmc-user-importer for more information',
    url='https://github.com/xmedius/xmc-user-importer',
    author='XMedius R&D',
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
    packages=['xmcuserimporter', 'xmcuserimporter.portal'],
    install_requires=['requests>=2'],
    entry_points={
        'console_scripts': [
            'xmc-user-importer = xmcuserimporter.__main__:main'
        ]
    },
)
