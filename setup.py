from setuptools import setup
import mcups
import sys

DESCRIPTION = "mcups: MCUPS is a CLI software that provides backup functionality for Minecraft servers developed by sonyaEarth (sonyakun)."
NAME = 'mcups'
AUTHOR = 'sonyaearth-dev'
AUTHOR_EMAIL = 'sonyakun217@gmail.com'
URL = 'https://github.com/sonyaearth-offical/backpak'
LICENSE = 'GNU General Public License v3.0'
DOWNLOAD_URL = 'https://github.com/sonyaearth-offical/backpak/releases'
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    'paramiko',
    'cleo'
]

CLASSIFIERS = [
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3 :: Only',
]

long_description_content_type = "https://github.com/sonyaearth-offical/backpak"

setup(
    name=NAME,
      version="0.1",
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description_content_type,
      license=LICENSE,
      url=URL,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      classifiers=CLASSIFIERS,
    entry_points={
        "console_scripts": [
            "mcups=mcups.app:main",
        ]
    },
)
