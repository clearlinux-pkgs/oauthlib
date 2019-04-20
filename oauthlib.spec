#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : oauthlib
Version  : 3.0.1
Release  : 41
URL      : https://files.pythonhosted.org/packages/ec/90/882f43232719f2ebfbdbe8b7c57fc9642a25b3df30cb70a3701ea22622de/oauthlib-3.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/ec/90/882f43232719f2ebfbdbe8b7c57fc9642a25b3df30cb70a3701ea22622de/oauthlib-3.0.1.tar.gz
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
BuildRequires : linecache2-python
BuildRequires : nose-python
BuildRequires : pycrypto-python
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

%description python3
python3 components for the oauthlib package.


%prep
%setup -q -n oauthlib-3.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548385669
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/oauthlib
cp LICENSE %{buildroot}/usr/share/package-licenses/oauthlib/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/oauthlib/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
