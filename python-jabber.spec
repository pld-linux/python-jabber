%include	/usr/lib/rpm/macros.python

%define		module	jabber
%define		pre	rc6

Summary:	"jabber.py" Python module for Jabber applications
Summary(pl):	Modu³y Pythona "jabber.py" dla aplikacji Jabber
Name:		python-%{module}
Version:	0.5
Release:	1.%{pre}.2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/jabberpy/jabberpy-%{version}-%{pre}.tar.gz
# Source0-md5:	4254353b683f4a0af35eedac2d8d6d8f
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

%description -l pl
jabber.py to modu³ Pythona do protoko³u komunikatora Jabber. jabber.py
obs³uguje analizowanie XML-a i gniazda, pozwalaj±c programi¶cie
skoncentrowaæ siê na tworzeniu w Pythonie wysokiej jako¶ci aplikacji
opartych na Jabberze.

%prep
%setup -q -n jabberpy-%{version}-%{pre}

%build
# next version can contain __init__.py, so check if this workaround is
# still required, please
# see also:
# http://sourceforge.net/tracker/index.php?func=detail&aid=897527&group_id=30215&atid=398567
echo 'from jabber import *' > jabber/__init__.py
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}-%{pre}

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}-%{pre}

rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/jabber/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS README
%{py_sitescriptdir}/jabber
%dir %{_examplesdir}/%{name}-%{version}-%{pre}
%{_examplesdir}/%{name}-%{version}-%{pre}/*
