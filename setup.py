import ast
import re
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    install_requires = [r for r in f.read().strip().split("\n") if r]

_version_re = re.compile(r"__version__\s+=\s+(.*)")

with open("print_formats/__init__.py", "rb") as f:
    version = str(ast.literal_eval(_version_re.search(f.read().decode("utf-8")).group(1)))

setup(
    name="print_formats",
    version=version,
    description="Professional Print Formats for ERPNext",
    author="Marketplace Publisher",
    author_email="hello@example.com",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
