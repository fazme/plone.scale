try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()

from setuptools import setup, find_packages
import os

version = "1.0"

setup(name="plone.scale",
      version=version,
      description="Image scaling",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords="image scaling",
      author="Wichert Akkerman",
      author_email="wichert@simplon.biz",
      url="",
      license="GPL",
      packages=find_packages(exclude=["ez_setup"]),
      namespace_packages=["plone"],
      include_package_data=True,
      zip_safe=True,
      test_suite="plone.scale",
      install_requires=[
          "PIL",
          "setuptools",
      ],
      )