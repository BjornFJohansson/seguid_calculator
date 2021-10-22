# create a deb file from a wxpython app

# interesting links:


# https://pypi.python.org/pypi/stdeb last release in 2015

# http://stackoverflow.com/questions/17401381/debianzing-a-python-program-to-get-a-deb/17402676#17402676
# https://github.com/cpbotha/stdeb-minimal-example


# https://github.com/paylogic/py2deb
# https://www.reddit.com/r/Python/comments/2x7s17/py2deb_python_to_debian_package_converter/
# https://py2deb.readthedocs.io/en/latest/comparisons.html

# https://www.debian.org/doc/packaging-manuals/python-policy/
# https://wiki.debian.org/Python/LibraryStyleGuide
# http://packaging.ubuntu.com/html/

# build source package https://help.launchpad.net/Packaging/PPA/BuildingASourcePackage
# upload to ppa with dput https://help.launchpad.net/Packaging/PPA/Uploading
# https://launchpad.net/~bjorn-johansson/+archive/ubuntu/seguid-calculator

# first install the python package containing wxpython:
# http://askubuntu.com/questions/758774/how-to-install-wxpython-ubuntu-16-04

# http://showmedo.com/videotutorials/video?name=linuxJensMakingDeb;fromSeriesID=37 dead
# https://launchpad.net/ubucompilator seems abandoned.
# http://ubuntuforums.org/showthread.php?t=51003 needs login

# sudo apt-get install python-wxgtk4.0 devscripts pip --- Uncomment this line if needed!

# Upgrade pip

sudo pip install --upgrade pip

sudo pip install stdeb

echo
echo
echo

which python

echo
echo
echo

python -c "import sys;print(sys.version);import wx;print('wxpython', wx.__version__)"

echo
echo
echo

python setup_deb.py --command-packages=stdeb.command sdist_dsc

echo
echo
echo

cd deb_dist/seguid_calculator-*
echo
echo
echo
debuild -uc -us

cd ../..

echo
echo
echo

ls ./deb_dist/*.deb

echo
echo
echo

#dput ppa:bjorn-johansson/seguid-calculator seguid-calculator_0.9.0-1_source.changes # not working yet...


$SHELL
