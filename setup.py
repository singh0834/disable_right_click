from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in disable_right_click/__init__.py
from disable_right_click import __version__ as version

setup(
	name="disable_right_click",
	version=version,
	description="Disable right click add on",
	author="OneHash",
	author_email="digital@onehash.ao",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
