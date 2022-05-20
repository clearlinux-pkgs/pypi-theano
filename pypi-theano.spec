#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-theano
Version  : 1.0.5
Release  : 57
URL      : https://files.pythonhosted.org/packages/6b/97/bcd5654ba60f35f180931afabbd3b4c46c0379852f961c7a2819ff897f5d/Theano-1.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/6b/97/bcd5654ba60f35f180931afabbd3b4c46c0379852f961c7a2819ff897f5d/Theano-1.0.5.tar.gz
Summary  : Optimizing compiler for evaluating mathematical expressions on CPUs and GPUs.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-theano-bin = %{version}-%{release}
Requires: pypi-theano-license = %{version}-%{release}
Requires: pypi-theano-python = %{version}-%{release}
Requires: pypi-theano-python3 = %{version}-%{release}
Requires: openmpi
BuildRequires : buildreq-distutils3
BuildRequires : pypi(cython)
BuildRequires : pypi(nose)
BuildRequires : pypi(numpy)
BuildRequires : pypi(requests)
BuildRequires : pypi(scipy)
BuildRequires : pypi(six)
BuildRequires : pypi(sympy)

%description
============================================================================================================
`MILA will stop developing Theano <https://groups.google.com/d/msg/theano-users/7Poq8BZutbY/rNCIfvAEAwAJ>`_.
============================================================================================================

%package bin
Summary: bin components for the pypi-theano package.
Group: Binaries
Requires: pypi-theano-license = %{version}-%{release}

%description bin
bin components for the pypi-theano package.


%package license
Summary: license components for the pypi-theano package.
Group: Default

%description license
license components for the pypi-theano package.


%package python
Summary: python components for the pypi-theano package.
Group: Default
Requires: pypi-theano-python3 = %{version}-%{release}

%description python
python components for the pypi-theano package.


%package python3
Summary: python3 components for the pypi-theano package.
Group: Default
Requires: python3-core
Provides: pypi(theano)
Requires: pypi(numpy)
Requires: pypi(scipy)
Requires: pypi(six)

%description python3
python3 components for the pypi-theano package.


%prep
%setup -q -n Theano-1.0.5
cd %{_builddir}/Theano-1.0.5
pushd ..
cp -a Theano-1.0.5 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653057485
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-theano
cp %{_builddir}/Theano-1.0.5/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-theano/fd05bc993b2d9e7637cd22914ed9eb7b0fae4213
cp %{_builddir}/Theano-1.0.5/doc/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-theano/fd05bc993b2d9e7637cd22914ed9eb7b0fae4213
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/theano-cache
/usr/bin/theano-nose

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-theano/fd05bc993b2d9e7637cd22914ed9eb7b0fae4213

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
