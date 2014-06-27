from setuptools import setup

setup(
    name='segment',
    version='0.0.1',
    url='http://github.com/mvj3/segment/',
    license='MIT',
    authors=['David Chen'],
    author_email=''.join(reversed("moc.liamg@emojvm")),
    description='segment',
    long_description='segment',
    packages=['segment', 'data'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
