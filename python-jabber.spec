
%define		module	jabber

Summary:	"jabber.py" Python module for Jabber applications
Summary(pl.UTF-8):	Moduły Pythona "jabber.py" dla aplikacji Jabber
Name:		python-%{module}
Version:	0.5
Release:	4
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/jabberpy/jabberpy-%{version}-0.tar.gz
# Source0-md5:	cbb9a1126bdc39ff49af605fb55c282e
URL:		http://jabberpy.sourceforge.net/
BuildRequires:	python-modules
BuildRequires:	python-devel
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jabber.py is a Python module for the Jabber instant messaging
protocol. jabber.py deals with the XML parsing and socket code,
leaving the programmer to concentrate on developing quality Jabber
based applications with Python.

%description -l pl.UTF-8
jabber.py to moduł Pythona do protokołu komunikatora Jabber. jabber.py
obsługuje analizowanie XML-a i gniazda, pozwalając programiście
skoncentrować się na tworzeniu w Pythonie wysokiej jakości aplikacji
opartych na Jabberze.

%prep
%setup -q -n jabberpy-%{version}-0

%build
# next version can contain __init__.py, so check if this workaround is
# still required, please
# see also:
# http://sourceforge.net/tracker/index.php?func=detail&aid=897527&group_id=30215&atid=398567
echo 'from jabber import *' > jabber/__init__.py
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/jabber/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README
%{py_sitescriptdir}/jabber
%dir %{_examplesdir}/%{name}-%{version}
%{_examplesdir}/%{name}-%{version}/*
