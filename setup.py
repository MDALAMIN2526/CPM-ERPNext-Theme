from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in cmp_erpnext_theme/__init__.py
from cmp_erpnext_theme import __version__ as version

setup(
	name="cmp_erpnext_theme",
	version=version,
	description="Business Theme for ERPNext / Frappe",
	author="Midocean Technologies Pvt Ltd",
	author_email="sagar@midocean.tech",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
