#!/bin/sh

set -x

rm -rf dist # Clean dist folder
python setup.py bdist_wheel --universal # Build package
gpg --detach-sign -a dist/* # Sign package
twine upload dist/* # Upload package and signature
