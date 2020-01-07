from setuptools import setup, find_packages

with open('README.md') as readme:
    readme = readme.read()

version = "0.1.0"

setup(
    name='ast-compat',
    version=version if isinstance(version, str) else str(version),
    keywords="ast compat",  # keywords of your project separated by comma ","
    description=
    "cross-version compatible ast library",  # a concise introduction of your project
    long_description=readme,
    long_description_content_type="text/markdown",
    license='mit',
    url='https://github.com/python-compiler-tools/ast-compat',
    author='thautwarm',
    author_email='twshere@outlook.com',
    packages=find_packages(),
    python_requires='>=3.5',
    entry_points={"console_scripts": []},
    install_requires=[],
    platforms="any",
    classifiers=[
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    zip_safe=False,
)
