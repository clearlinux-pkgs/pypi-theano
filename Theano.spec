#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Theano
Version  : 0.8.0rc1
Release  : 1
URL      : https://pypi.python.org/packages/source/T/Theano/Theano-0.8.0rc1.tar.gz
Source0  : https://pypi.python.org/packages/source/T/Theano/Theano-0.8.0rc1.tar.gz
Summary  : Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: Theano-bin
Requires: Theano-python
BuildRequires : openblas
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
To install the package, see this page:
http://deeplearning.net/software/theano/install.html

%package bin
Summary: bin components for the Theano package.
Group: Binaries

%description bin
bin components for the Theano package.


%package python
Summary: python components for the Theano package.
Group: Default
Provides: theano-python

%description python
python components for the Theano package.


%prep
%setup -q -n Theano-0.8.0rc1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/theano-cache
/usr/bin/theano-nose
/usr/bin/theano-test

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
