from setuptools import setup

setup(
    name='ai bot',
    version='1.1.5',
    description='Discord chat bot using AIML artificial intelligence.',
    long_description=open('README.rst').read(),
    url='https://github.com/Rajisop/ai-bot',
    author='Rajisop',
    author_email='nanodano@devdungeon.com',
    license='GPL-3.0',
    packages=['cathy'],
    scripts=[
        'bin/cathy',
        'bin/cathy.bat',
    ],
    package_data={
        'cathy': [
            'std-startup.xml',
            'aiml/alice/*.aiml',
            'aiml/custom/*.aiml'
        ],
    },
    zip_safe=False,
    install_requires=[
        'docopt',
        'python-aiml',
        'discord.py==0.16.12',
        'requests',
    ],
    python_requires='<3.7',
)
