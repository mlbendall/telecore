from setuptools import setup
import versioneer

requirements = [
    'scipy>=1.7',
    'pysam>=0.16',
    'pyranges'
]

setup(
    name='telecore',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Core classes, functions and algorithms for Telescope programs",
    license="MIT",
    author="Matthew L. Bendall",
    author_email='mlb4001@med.cornell.edu',
    url='https://github.com/mlbendall/telecore',
    packages=['telecore'],
    entry_points={
        'console_scripts': [
            'telecore=telecore.cli:cli'
        ]
    },
    install_requires=requirements,
    keywords='telecore',
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ]
)
