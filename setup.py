import setuptools
from pathlib import Path

setuptools.setup(
    name='android-passpoint',
    version='0.0.0',
    author='Jose A. Delgado Alfonso',
    description='',
    project_urls={
        'Source Code': 'https://github.com/hylang/simalq'},
    install_requires=[
        'jinja2 ~= 3.1.4',
        'fastapi ~= 0.111.0',
        'pydantic ~= 2.7.1',
        'uvicorn ~= 0.29.0'],
    packages=setuptools.find_packages(),
    package_data=dict(src=[
        str(p.relative_to('src'))
        for p in Path('simalq').rglob('*.hy')]),
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3'])
