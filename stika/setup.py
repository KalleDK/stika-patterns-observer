from setuptools import setup

with open('LICENSE') as f:
    license_ = f.read()


with open('README.md') as f:
    readme = f.read()

setup(
    name='stika_patterns_observer',
    version='0.9',
    packages=['stika.patterns.observer'],
    url='https://github.com/KalleDK/stika-patterns-observer',
    license=license_,
    author='Kalle R. Møller',
    author_email='pypi@k-moeller.dk',
    description='Simple Observer Pattern',
    long_description=readme,
    zip_safe=False,
    install_requires=[
        'typing_extensions'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ]
)
