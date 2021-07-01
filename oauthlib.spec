#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oauthlib
Version  : 3.1.1
Release  : 60
URL      : https://files.pythonhosted.org/packages/9e/84/001a3f8d9680f3b26d5e7711e13d5ff92e4b511766a72ac6b4a4e5f06796/oauthlib-3.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/9e/84/001a3f8d9680f3b26d5e7711e13d5ff92e4b511766a72ac6b4a4e5f06796/oauthlib-3.1.1.tar.gz
Summary  : A generic, spec-compliant, thorough implementation of the OAuth request-signing logic
Group    : Development/Tools
License  : BSD-3-Clause
Requires: oauthlib-license = %{version}-%{release}
Requires: oauthlib-python = %{version}-%{release}
Requires: oauthlib-python3 = %{version}-%{release}
Requires: blinker
Requires: cryptography
BuildRequires : blinker
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : linecache2-python
BuildRequires : nose-python
BuildRequires : pyjwt-python
BuildRequires : python-mock
BuildRequires : six
BuildRequires : six-python
BuildRequires : traceback2-python
BuildRequires : unittest2-python

%description
OAuthLib - Python Framework for OAuth1 & OAuth2
===============================================

%package license
Summary: license components for the oauthlib package.
Group: Default

%description license
license components for the oauthlib package.


%package python
Summary: python components for the oauthlib package.
Group: Default
Requires: oauthlib-python3 = %{version}-%{release}

%description python
python components for the oauthlib package.


%package python3
Summary: python3 components for the oauthlib package.
Group: Default
Requires: python3-core
Provides: pypi(oauthlib)

%description python3
python3 components for the oauthlib package.


%prep
%setup -q -n oauthlib-3.1.1
cd %{_builddir}/oauthlib-3.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622560646
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oauthlib
cp %{_builddir}/oauthlib-3.1.1/LICENSE %{buildroot}/usr/share/package-licenses/oauthlib/5f350c5a2f0fb712d78b3203f40d1f9d3b399a31
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oauthlib/5f350c5a2f0fb712d78b3203f40d1f9d3b399a31

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
