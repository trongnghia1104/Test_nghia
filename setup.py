from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in test_nghia/__init__.py
from test_nghia import __version__ as version

setup(
	name="test_nghia",
	version=version,
	description="nghia",
	author="nghia",
	author_email="nghia",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
