from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

from pro_print_formats import __version__ as version

setup(
	name="pro_print_formats",
	version=version,
	description="Professional Print Formats for ERPNext",
	author="Marketplace Publisher",
	author_email="hello@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
