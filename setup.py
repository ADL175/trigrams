from setuptools import setup

setup(
    name="trigrams",
    description="A Python program",
    version="0.1",
    author="David Lim",
    author_email="armydavidlim@gmail.com",
    license="MIT",
    py_modules=['trigrams'],
    package_dir={'': 'src'},
    install_requires=[],
    extras_require={'test':['pytest','pytest-watch', 'pytest-cov']},
    entry_points={
        'console_scripts':[
            "trigrams = trigrams:main"
            ]
    }
    )