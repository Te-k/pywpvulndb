from setuptools import setup

setup(
    name='pywpvulndb',
    version='0.1.1',
    description='Python wrapper around the WP Vuln DB API',
    url='https://github.com/Te-k/pywpvulndb',
    author='Tek',
    author_email='tek@randhome.io',
    keywords='security',
    install_requires=['requests'],
    license='MIT',
    packages=['pywpvulndb'],
    entry_points= {
        'console_scripts': [ 'wpvulndb=pywpvulndb.cli:main' ]
    }
)
