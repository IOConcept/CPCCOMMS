from setuptools import setup

setup(
    name='CPCCOMMS',
    version='V3',
    packages=[''],
    url='',
    license='',
    author='Eric D. McCullar',
    author_email='ioconceptcontact@gmail.com',
    description='CPC Core Systems node',
    install_requires=[
        'Flask==2.1.0',
        'Jinja2==3.0.2',
        'MarkupSafe==2.0.1',
        'Werkzeug==2.0.1',
        'requests==2.26.0',
        'schedule==1.1.0',
    ]
)
