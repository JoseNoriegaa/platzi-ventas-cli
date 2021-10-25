from setuptools import setup  # type: ignore

setup(
    name='pv',
    version='0.1',
    py_modules=['pv'],
    install_requires=[
        'Click',
        'tabulate',
    ],
    packages=['clients'],
    entry_points="""
        [console_scripts]
        pv=pv:cli
    """,
)
