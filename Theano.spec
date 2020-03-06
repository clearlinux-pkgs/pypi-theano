#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Theano
Version  : 1.0.4
Release  : 39
URL      : https://files.pythonhosted.org/packages/7d/c4/6341148ad458b6cd8361b774d7ee6895c38eab88f05331f22304c484ed5d/Theano-1.0.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/7d/c4/6341148ad458b6cd8361b774d7ee6895c38eab88f05331f22304c484ed5d/Theano-1.0.4.tar.gz
Summary  : Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
Group    : Development/Tools
License  : BSD-3-Clause-Clear
Requires: Theano-bin = %{version}-%{release}
Requires: Theano-license = %{version}-%{release}
Requires: Theano-python = %{version}-%{release}
Requires: Theano-python3 = %{version}-%{release}
Requires: numpy
Requires: openmpi
Requires: scipy
Requires: six
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : graphviz
BuildRequires : nose
BuildRequires : numpy
BuildRequires : ocl-icd
BuildRequires : ocl-icd-dev
BuildRequires : openblas
BuildRequires : opencl-headers-dev
BuildRequires : openmpi
BuildRequires : scipy
BuildRequires : six

%description
============================================================================================================
`MILA will stop developing Theano <https://groups.google.com/d/msg/theano-users/7Poq8BZutbY/rNCIfvAEAwAJ>`_.
============================================================================================================

%package bin
Summary: bin components for the Theano package.
Group: Binaries
Requires: Theano-license = %{version}-%{release}

%description bin
bin components for the Theano package.


%package license
Summary: license components for the Theano package.
Group: Default

%description license
license components for the Theano package.


%package python
Summary: python components for the Theano package.
Group: Default
Requires: Theano-python3 = %{version}-%{release}
Provides: theano-python

%description python
python components for the Theano package.


%package python3
Summary: python3 components for the Theano package.
Group: Default
Requires: python3-core
Provides: pypi(theano)
Requires: pypi(numpy)
Requires: pypi(scipy)
Requires: pypi(six)

%description python3
python3 components for the Theano package.


%prep
%setup -q -n Theano-1.0.4
cd %{_builddir}/Theano-1.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583523854
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Theano
cp %{_builddir}/Theano-1.0.4/LICENSE.txt %{buildroot}/usr/share/package-licenses/Theano/cb55ee0dc57eeb4cfc75424d615d0577a4a71c80
cp %{_builddir}/Theano-1.0.4/doc/LICENSE.txt %{buildroot}/usr/share/package-licenses/Theano/cb55ee0dc57eeb4cfc75424d615d0577a4a71c80
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/theano-cache
/usr/bin/theano-nose

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Theano/cb55ee0dc57eeb4cfc75424d615d0577a4a71c80

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
